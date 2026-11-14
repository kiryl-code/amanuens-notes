import { BaseExercise } from './baseExercise.js';

export class AnswerAlternativeExercise extends BaseExercise {
    constructor(form) {
        super(form);
        this.correctAnswers = Array.from(form.querySelectorAll(".correct"));
    }

    check() {
        const selectedAnswers = this.answers.filter(answer => !!answer.checked);
        const isCorrect = this.correctAnswers.every(answer => answer.checked) && selectedAnswers.length === this.correctAnswers.length;
        this.toggleResults(isCorrect);
    }
}
