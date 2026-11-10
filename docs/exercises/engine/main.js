import { AnswerAlternativeExercise } from "./answerAlternativeExercise.js";
import { SelectExercise } from "./selectExercise.js";

const exerciseTypesMap = {
    "answerAlternativeExercise": AnswerAlternativeExercise,
    "selectExercise": SelectExercise
}

function main() {
    const forms = Array.from(document.querySelectorAll("form"));
    for (const form of forms) {
        const exerciseType = form.dataset.exerciseType;
        const exerciseClass = exerciseTypesMap[exerciseType];
        new exerciseClass(form);
    }
}

document.addEventListener("DOMContentLoaded", main);