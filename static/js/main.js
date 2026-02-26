document.addEventListener("DOMContentLoaded", () => {

    // --- Mobile Nav Toggle ---
    const navToggle = document.querySelector(".nav-toggle");
    const navLinks = document.querySelector(".nav-links");

    if (navToggle) {
        navToggle.addEventListener("click", () => {
            navLinks.classList.toggle("active");
            // Switch icon between bars and X
            const icon = navToggle.querySelector("i");
            icon.classList.toggle("fa-bars");
            icon.classList.toggle("fa-times");
        });
    }

    // Close mobile nav when a link is clicked
    document.querySelectorAll(".nav-links a").forEach(link => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("active");
            const icon = navToggle.querySelector("i");
            icon.classList.add("fa-bars");
            icon.classList.remove("fa-times");
        });
    });


    // --- Navbar scroll effect ---
    const navbar = document.querySelector(".navbar");
    window.addEventListener("scroll", () => {
        if (window.scrollY > 50) {
            navbar.style.padding = "10px 0";
            navbar.style.boxShadow = "0 4px 20px rgba(0,0,0,0.3)";
        } else {
            navbar.style.padding = "16px 0";
            navbar.style.boxShadow = "none";
        }
    });


    // --- Auto-dismiss flash messages after 5 seconds ---
    const flashMessages = document.querySelectorAll(".flash-message");
    flashMessages.forEach(msg => {
        setTimeout(() => {
            msg.style.animation = "slideOut 0.4s ease forwards";
            setTimeout(() => msg.remove(), 400);
        }, 5000);
    });

});

// Add slideOut animation dynamically
const style = document.createElement("style");
style.textContent = `
    @keyframes slideOut {
        to {
            transform: translateX(100%);
            opacity: 0;
        }
    }
`;
document.head.appendChild(style);
