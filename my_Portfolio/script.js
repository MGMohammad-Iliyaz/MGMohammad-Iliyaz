document.addEventListener('DOMContentLoaded', () => {

    // Typing effect for the hero section
    new Typed('.typing-effect', {
        strings: ['a Python Developer.', 'a Web Developer.', 'a Quick Learner.'],
        typeSpeed: 70,
        backSpeed: 50,
        loop: true
    });

    // Smooth scrolling for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });

});