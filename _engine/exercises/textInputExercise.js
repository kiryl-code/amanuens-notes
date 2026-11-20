import { BaseExercise } from './baseExercise.js';

export class TextInputExercise extends BaseExercise {
    constructor(form) {
        super(form);
    }

    normalize(text) {
        return text.trim().toLowerCase().replace(/\s+/g, " ");
    }

    check() {
        const isCorrect = this.answers.every(input => {
            const userValue = this.normalize(input.value);

            const correctAnswers = (input.dataset.correct || "")
                .split('|')
                .map(a => this.normalize(a));

            return correctAnswers.includes(userValue);
        });
        this.toggleResults(isCorrect);
    }
}
