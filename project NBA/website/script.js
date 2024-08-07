document.addEventListener("DOMContentLoaded", function() {
    var coll = document.querySelectorAll(".collapsible-button");
    coll.forEach(function(button) {
        button.addEventListener("click", function() {
            this.classList.toggle("active");
            var content = this.nextElementSibling;
            if (content.style.maxHeight) {
                content.style.maxHeight = null;
            } else {
                content.style.maxHeight = "250px";
                content.style.overflowY = "auto"; // Enable vertical scrolling
            }
        });
    });
});


document.addEventListener("click", function(event) {
    if (event.target.classList.contains("graph_img")) {
        event.target.classList.toggle("fullscreen");
    }
});
