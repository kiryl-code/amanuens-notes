import sys
from pathlib import Path

import markdown
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
from markupsafe import Markup

ROOT = Path(__file__).resolve().parent
SOURCE_DIR = ROOT / "exercises"
OUTPUT_DIR = ROOT / "docs" / "exercises"
TEMPLATE_DIR = ROOT / "templates"


def render_markdown(text, inline=False):
    if not text:
        return ""

    html = markdown.markdown(
        str(text),
        extensions=["fenced_code", "codehilite", "tables", "nl2br"]
    )

    if inline and html.startswith("<p>") and html.endswith("</p>"):
        html = html[3:-4]

    return Markup(html)


def parse_yaml_to_template_data(yaml_content, filename):
    title = yaml_content.get("title", f"Övning - {filename}")
    questions_data = []

    for q_idx, q in enumerate(yaml_content.get("questions", []), start=1):
        q_type = q.get("type", "answerAlternativeExercise")
        alternatives = []

        for a_idx, alt in enumerate(q.get("alternatives", []), start=1):
            if isinstance(alt, dict) and "text" in alt:
                alt_text = alt["text"]
                is_correct = alt.get("correct", False)
            elif isinstance(alt, dict):
                alt_text, props = next(iter(alt.items()))
                if isinstance(props, bool):
                    is_correct = props
                elif isinstance(props, dict):
                    is_correct = props.get("correct", False)
                else:
                    is_correct = False
            else:
                alt_text = str(alt)
                is_correct = False

            alternatives.append({
                "id": f"q{q_idx}_answer{a_idx}",
                "text": str(alt_text),
                "correct": is_correct
            })

        raw_correct = q.get("correct_answer", "")
        if isinstance(raw_correct, list):
            correct_answer = "|".join(str(item) for item in raw_correct)
        else:
            correct_answer = str(raw_correct) if raw_correct else ""

        questions_data.append({
            "type": q_type,
            "radio": q.get("radio", False),
            "name": f"question{q_idx}",
            "question": q.get("question", ""),
            "correct_answer": correct_answer,
            "alternatives": alternatives,
            "correct_explanation": q.get("correct_explanation", ""),
            "incorrect_explanation": q.get("incorrect_explanation", "")
        })

    return {
        "title": title,
        "questions": questions_data
    }


def process_file(source_path, env):
    try:
        with source_path.open(encoding="utf-8") as file:
            yaml_content = yaml.safe_load(file)
    except Exception as error:
        print(f"Failed to load {source_path}: {error}", file=sys.stderr)
        return

    data = parse_yaml_to_template_data(yaml_content, source_path.stem)
    template = env.get_template("exercises-template.html")

    rel_path = source_path.relative_to(SOURCE_DIR)
    output_path = OUTPUT_DIR / rel_path.with_suffix(".html")

    data["root_prefix"] = "../" * (len(rel_path.parts) - 1)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    html_output = template.render(data)
    output_path.write_text(html_output, encoding="utf-8")

    print(f"Created: {output_path.relative_to(ROOT)}")


def main():
    if not SOURCE_DIR.exists() or not TEMPLATE_DIR.exists():
        print(f"Could not find {SOURCE_DIR} or {TEMPLATE_DIR}", file=sys.stderr)
        sys.exit(1)

    env = Environment(
        loader=FileSystemLoader(TEMPLATE_DIR),
        autoescape=select_autoescape(["html", "xml"])
    )
    env.filters["md"] = lambda text: render_markdown(text, inline=False)
    env.filters["md_inline"] = lambda text: render_markdown(text, inline=True)

    for source_path in SOURCE_DIR.rglob("*.yaml"):
        process_file(source_path, env)


if __name__ == "__main__":
    main()
