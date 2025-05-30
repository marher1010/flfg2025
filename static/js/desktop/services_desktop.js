document.addEventListener('DOMContentLoaded', function () {
    // Get the video element with the class "background-video"
    var video = document.querySelector('.background-video');

    // Check if the video element exists
    if (video) {
        // Play the video on page load
        video.play();
    }
});


// Expand/Collapse Article
document.querySelectorAll("#infographic article").forEach((article) => {
    article.addEventListener("click", () => {
        article.classList.toggle("active");
    });
});

// Always Collapse Article on click outside
document.addEventListener("mouseup", (e) => {
    document.querySelectorAll("article.active").forEach((article) => {
        if (article.contains(e.target)) return;
        if (article === e.target) return;
        article.classList.remove("active");
    });
});

// Activate artciles through prev/next interactions
document.querySelectorAll("#infographic article .btn").forEach((btn) => {
    btn.addEventListener("click", (e) => {
        e.preventDefault();
        var isprev =
            e.target === e.target.parentElement.firstElementChild ? true : false;
        var article = btn.closest("article");
        var step = parseInt(article.getAttribute("data-step"));
        var next = document.querySelector(
            `[data-step="${isprev ? step - 1 : step + 1}"]`
        );
        next.classList.add("active");
        next.scrollIntoView({
            behavior: "smooth",
            block: "nearest"
        });
    });
});
