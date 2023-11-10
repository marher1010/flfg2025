document.addEventListener("DOMContentLoaded", function () {
    const panels = document.querySelectorAll(".panel-container");
    const nextButtons = document.querySelectorAll(".next");
    const prevButtons = document.querySelectorAll(".prev");

    nextButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            if (index < panels.length - 1) {
                panels[index + 1].scrollIntoView({ behavior: "smooth" });
            }
        });
    });

    prevButtons.forEach((button, index) => {
        button.addEventListener("click", () => {
            if (index > 0) {
                panels[index - 1].scrollIntoView({ behavior: "smooth" });
            }
        });
    });
});
