export class BaseExercise {
    constructor(form) {
        this.form = form;
        this.answers = Array.from(form.querySelectorAll(".answer"));
        this.resultField = form.querySelector(".explanations");
        this.correctResultField = form.querySelector(".resultCorrect");
        this.incorrectResultField = form.querySelector(".resultIncorrect");
        this.explanationCorrect = form.querySelector(".explanationCorrect");
        this.explanationIncorrect = form.querySelector(".explanationIncorrect");
        form.addEventListener("submit", this.onSubmit.bind(this));
        form.addEventListener("reset", this.reset.bind(this));
    }

    check() {
        throw new Error("Method not implemented.");
    }

    reset(e) {
        this.correctResultField.classList.add("hidden");
        this.incorrectResultField.classList.add("hidden");
        this.explanationCorrect.classList.add("hidden");
        this.explanationIncorrect.classList.add("hidden");
        this.resultField.classList.remove("incorrect");
        this.resultField.classList.remove("correct");
    }

    onSubmit(e) {
        e.preventDefault();
        this.check();
    }

    toggleResults(isCorrect) {
        this.correctResultField.classList.toggle("hidden", !isCorrect);
        this.incorrectResultField.classList.toggle("hidden",isCorrect);
        this.explanationCorrect.classList.toggle("hidden", !isCorrect);
        this.explanationIncorrect.classList.toggle("hidden", isCorrect);
        this.resultField.classList.toggle("incorrect", !isCorrect);
        this.resultField.classList.toggle("correct", isCorrect);
    }
}