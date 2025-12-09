// ========================================
// SUMEDH RAJARSHI PORTFOLIO - MAIN JS
// Interactive functionality and animations
// ========================================

document.addEventListener('DOMContentLoaded', function () {

    // ===NAVIGATION SCROLL EFFECT ===
    const navbar = document.getElementById('navbar');
    const navbarLinks = document.querySelectorAll('.navbar-link');

    window.addEventListener('scroll', function () {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }

        // Update active nav link based on scroll position
        updateActiveNavLink();
    });

    // Mobile menu toggle
    const menuToggle = document.getElementById('menuToggle');
    const navbarMenu = document.getElementById('navbarMenu');

    if (menuToggle) {
        menuToggle.addEventListener('click', function () {
            navbarMenu.classList.toggle('active');
        });

        // Close menu when clicking a link
        navbarLinks.forEach(link => {
            link.addEventListener('click', function () {
                navbarMenu.classList.remove('active');
            });
        });
    }

    // === SMOOTH SCROLL ===
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                const offset = 80; // navbar height
                const targetPosition = target.offsetTop - offset;
                window.scrollTo({
                    top: targetPosition,
                    behavior: 'smooth'
                });
            }
        });
    });

    // === ACTIVE NAV LINK UPDATE ===
    function updateActiveNavLink() {
        const sections = document.querySelectorAll('section[id]');
        const scrollY = window.pageYOffset;

        sections.forEach(section => {
            const sectionHeight = section.offsetHeight;
            const sectionTop = section.offsetTop - 100;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.navbar-link[href="#${sectionId}"]`);

            if (scrollY > sectionTop && scrollY <= sectionTop + sectionHeight) {
                navbarLinks.forEach(link => link.classList.remove('active'));
                if (navLink) {
                    navLink.classList.add('active');
                }
            }
        });
    }

    // === SCROLL PROGRESS BAR ===
    const scrollProgress = document.getElementById('scrollProgress');

    window.addEventListener('scroll', function () {
        const windowHeight = document.documentElement.scrollHeight - document.documentElement.clientHeight;
        const scrolled = (window.scrollY / windowHeight) * 100;
        scrollProgress.style.width = scrolled + '%';
    });

    // === INTERSECTION OBSERVER FOR ANIMATIONS ===
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const fadeElements = document.querySelectorAll('.fade-in-up, .fade-in-left, .fade-in-right, .fade-in, .scale-in');

    const fadeObserver = new IntersectionObserver(function (entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0) translateX(0) scale(1)';
                fadeObserver.unobserve(entry.target);
            }
        });
    }, observerOptions);

    fadeElements.forEach(element => {
        fadeObserver.observe(element);
    });

    // === FORM AGE GROUP FIELD VISIBILITY ===
    const interestTypeField = document.querySelector('[name="interest_type"]');
    const ageGroupField = document.getElementById('ageGroupField');

    if (interestTypeField && ageGroupField) {
        function toggleAgeGroupField() {
            const interestValue = interestTypeField.value;
            if (interestValue === 'academy' || interestValue === 'both') {
                ageGroupField.style.display = 'block';
            } else {
                ageGroupField.style.display = 'none';
            }
        }

        interestTypeField.addEventListener('change', toggleAgeGroupField);
        toggleAgeGroupField(); // Initial state
    }

    // === AUTO-DISMISS MESSAGES ===
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.animation = 'slideOutRight 0.3s ease forwards';
            setTimeout(() => {
                message.remove();
            }, 300);
        }, 5000);
    });

    // === PARALLAX EFFECT ON HERO/SECTIONS (SUBTLE) ===
    window.addEventListener('scroll', function () {
        const scrolled = window.pageYOffset;
        const hero = document.querySelector('.hero');
        if (hero) {
            hero.style.transform = `translateY(${scrolled * 0.5}px)`;
        }
    });

    // === IMAGE LAZY LOADING ===
    if ('loading' in HTMLImageElement.prototype) {
        const images = document.querySelectorAll('img[loading="lazy"]');
        images.forEach(img => {
            img.src = img.dataset.src || img.src;
        });
    } else {
        // Fallback for browsers that don't support lazy loading
        const script = document.createElement('script');
        script.src = 'https://cdnjs.cloudflare.com/ajax/libs/lazysizes/5.3.2/lazysizes.min.js';
        document.body.appendChild(script);
    }

    // === FORM VALIDATION ENHANCEMENT ===
    const contactForm = document.querySelector('.contact-form');
    if (contactForm) {
        contactForm.addEventListener('submit', function (e) {
            const inputs = contactForm.querySelectorAll('[required]');
            let isValid = true;

            inputs.forEach(input => {
                if (!input.value.trim()) {
                    isValid = false;
                    input.style.borderColor = '#ef4444';
                } else {
                    input.style.borderColor = 'rgba(255, 255, 255, 0.1)';
                }
            });

            if (!isValid) {
                e.preventDefault();
            }
        });
    }

    // === PREVENT ANIMATION REPLAY ON RESIZE ===
    let resizeTimer;
    window.addEventListener('resize', function () {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(function () {
            // Reset animations if needed
        }, 250);
    });

});

// === UTILITY FUNCTIONS ===

// Debounce function
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Throttle function
function throttle(func, limit) {
    let inThrottle;
    return function () {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}
