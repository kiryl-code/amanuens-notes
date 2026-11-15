import { BaseExercise } from './baseExercise.js';

export class SelectExercise extends BaseExercise {
    constructor(form) {
        super(form);
    }

    check() {
        let isCorrect = this.answers.every(answer =>
            answer.value.toLowerCase().trim() === (answer.dataset.correct ?? "").toLowerCase().trim()
        )
        this.toggleResults(isCorrect);
    }
}
