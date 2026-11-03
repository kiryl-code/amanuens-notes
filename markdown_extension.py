"""
This module contains extensions for Markdown parser
to make sure the custom Markdown syntax is converted properly.
"""

import re
import xml.etree.ElementTree as eTree

from markdown.blockprocessors import BlockProcessor
from markdown.postprocessors import Postprocessor
from markdown.treeprocessors import Treeprocessor
from markdown.inlinepatterns import InlineProcessor

from markdown import Extension


def parse_blocks(end: str, blocks: list[str]) -> list[str]:
    """
    Parses a content inside a custom markdown-block.
    :param end: A regular expression that can be used to identify the end of the block.
    :param blocks: A part of the document that should be parsed.
    :return: List of lines inside the block
    """
    content_blocks = []
    found_end = False
    consumed_blocks = 0

    for block_idx, block in enumerate(blocks):
        block_lines = block.split('\n')

        start_line = 1 if block_idx == 0 else 0

        current_block_lines = []
        for line_idx in range(start_line, len(block_lines)):
            if re.search(end, block_lines[line_idx]):
                found_end = True
                consumed_blocks = block_idx + 1
                break
            current_block_lines.append(block_lines[line_idx])

        if current_block_lines:
            content_blocks.append("\n".join(current_block_lines))

        if found_end:
            break

    if not found_end:
        raise ValueError("No end found")

    for _ in range(consumed_blocks):
        blocks.pop(0)

    return content_blocks


class InlineColorProcessor(InlineProcessor):
    """
    Process custom inline color syntax.
    """

    COLOR_PATTERN = r"::(.*?)\|(.*?)::"

    def handleMatch(self, match, data):
        color = match.group(1).strip()
        text = match.group(2).strip()

        span = eTree.Element("span")
        span.set("style", f"color: {color};")
        span.text = text

        return span, match.start(0), match.end(0)


class CollapsibleProcessor(BlockProcessor):
    """
    Processes custom expandable block syntax.
    """

    RE_START = r'^ *\^{4,}(.*)'
    RE_END = r'\^{4,}\s*$'

    def test(self, parent, block):
        return re.match(self.RE_START, block)

    def run(self, parent, blocks) -> bool | None:
        lines = blocks[0].split('\n')
        match = re.match(self.RE_START, lines[0])
        title_text = match.group(1).strip() if match else ""

        try:
            content_blocks = parse_blocks(self.RE_END, blocks)
        except ValueError:
            return False

        details = eTree.SubElement(parent, 'details')
        summary = eTree.SubElement(details, 'summary')
        summary.text = title_text
        div = eTree.SubElement(details, 'div')
        div.set('class', 'collapsible-content')

        self.parser.parseBlocks(div, content_blocks)
        return True


class SideBlockProcessor(BlockProcessor):
    """
    Processes custom side block syntax.
    """

    RE_START = r'^!{4,}(.*)'
    RE_END = r'!{4,}\s*$'
    BLOCK_TYPES = {
        "info": "#FFC000",
        "message": "#3A53BB",
        "success": "#2B8D50",
        "warning": "#C85550",
        "red": "#C85550",
        "green": "#2B8D50",
        "blue": "#3A53BB",
        "yellow": "#FFC000"
    }

    def test(self, parent, block):
        return re.match(self.RE_START, block)

    def run(self, parent, blocks) -> bool | None:
        lines = blocks[0].split('\n')
        match = re.match(self.RE_START, lines[0])
        side_block_type = match.group(1).strip().lower() if match and match.group(1).strip() else "message"
        side_block_color = self.BLOCK_TYPES.get(side_block_type, side_block_type)

        try:
            content_blocks = parse_blocks(self.RE_END, blocks)
        except ValueError:
            return False

        div = eTree.SubElement(parent, "div")
        div.set("class", "side-block")
        div.set("style", f"border-left-color:{side_block_color};")
        self.parser.parseBlocks(div, content_blocks)
        return True


class CodeblockPostProcessor(Postprocessor):
    """
    Modify the codeblock HTML structure to match Canvas
    representation to avoid visual issues and enable proper
    styling.
    """

    def run(self, text: str) -> str:
        text = re.sub(r'<pre><span></span><code[^>]*>', '<pre>', text)
        text = text.replace('</code></pre>', '</pre>')
        return text


class LinkTreeProcessor(Treeprocessor):
    """
    For the non-anchor links sets ``target`` attribute to ``_blank`` to
    open external links in a new tab.
    """

    def run(self, root):
        for a in root.iter('a'):
            link = a.get('href')
            if link and not link.startswith('#'):
                a.set('target', '_blank')
        return root


class ExtensionsRegister(Extension):
    """
    Register all custom extensions and overrides for the Markdown package.
    """

    def extendMarkdown(self, md) -> None:
        """
        Register extensions and processors.
        :param md: Markdown instance
        """
        md.parser.blockprocessors.register(CollapsibleProcessor(md.parser), 'collapsible', 175)
        md.parser.blockprocessors.register(SideBlockProcessor(md.parser), "sideblock", 175)
        md.inlinePatterns.register(InlineColorProcessor(InlineColorProcessor.COLOR_PATTERN, md), "inline color", 175)
        md.treeprocessors.register(LinkTreeProcessor(md), 'links', 15)
        md.postprocessors.register(CodeblockPostProcessor(md), 'remove_code_tag', 5)



def makeExtension(**kwargs):
    return ExtensionsRegister(**kwargs)