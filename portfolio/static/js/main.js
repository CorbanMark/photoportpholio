document.addEventListener("DOMContentLoaded", () => {

   /* =========================================================
       1. PORTFOLIO Marquee Fade-Out on Scroll (Capped Movement)
       ========================================================= */
    const frontTitle = document.querySelector('.front-title');
    const redBlur = document.querySelector('.red-blur');

    window.addEventListener('scroll', () => {
        const scrollPosition = window.scrollY;
        const fadeDistance = 180; // Fades out completely before reaching bio card

        // 1. Calculate opacity
        let opacity = 1 - (scrollPosition / fadeDistance);
        if (opacity < 0) opacity = 0;

        // 2. Cap max downward movement to 60px so it never overflows
        let translateY = Math.min(scrollPosition * 0.25, 60);

        if (frontTitle) {
            frontTitle.style.opacity = opacity;
            frontTitle.style.transform = `translateY(${translateY}px)`;
        }

        if (redBlur) {
            redBlur.style.opacity = opacity * 0.7;
            redBlur.style.transform = `translateX(-50%) translateY(${translateY}px)`;
        }
    });


    /* =========================================================
       2. Grid Fade-In (Intersection Observer)
       ========================================================= */
    const gridItems = document.querySelectorAll('.grid-item');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.style.opacity = '1';
                entry.target.style.transform = 'translateY(0)';
            }
        });
    }, { threshold: 0.1 });

    gridItems.forEach(item => {
        item.style.opacity = '0';
        item.style.transform = 'translateY(20px)';
        item.style.transition = 'opacity 0.6s ease-out, transform 0.6s ease-out';
        observer.observe(item);
    });


    /* =========================================================
       3. Connected Hover Highlights (Read More + Title + Image)
       ========================================================= */
    const readMoreBtns = document.querySelectorAll('.read-more');

    readMoreBtns.forEach(btn => {
        const textBlock = btn.closest('.text-block');
        const imgBlock = textBlock ? textBlock.nextElementSibling : null;

        if (imgBlock && imgBlock.classList.contains('img-block')) {
            const title = textBlock.querySelector('h2');
            
            // Elements that trigger the combined highlight effect
            const triggerElements = [btn, title, imgBlock];

            triggerElements.forEach(el => {
                if (!el) return;

                el.addEventListener('mouseenter', () => {
                    textBlock.classList.add('hover-active');
                    imgBlock.classList.add('hover-active', 'draw-active');
                });

                el.addEventListener('mouseleave', () => {
                    textBlock.classList.remove('hover-active');
                    imgBlock.classList.remove('hover-active', 'draw-active');
                });
            });
        }
    });

});