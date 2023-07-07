// Function to smooth scroll to sections when clicking on the navbar links
document.addEventListener("DOMContentLoaded", function() {
    const navLinks = document.querySelectorAll("#links a");
    navLinks.forEach(function(link) {
        link.addEventListener("click", function(e) {
            e.preventDefault();
            const targetSection = document.querySelector(this.getAttribute("href"));
            window.scrollTo({
                top: targetSection.offsetTop - 50,
                behavior: "smooth"
            });
        });
    });
});