// ================================================
// BODY ART MADRID - Main JavaScript
// Mobile menu, dropdown, scroll header, FAQ accordion,
// gallery filters, lightbox, scroll reveal, form validation
// ================================================

document.addEventListener('DOMContentLoaded', () => {

    // ============================================
    // MENU MOVIL
    // ============================================
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mainNav = document.getElementById('main-navigation');
    const body = document.body;

    // Creamos el overlay dinamicamente
    const overlay = document.createElement('div');
    overlay.classList.add('nav-overlay');
    body.appendChild(overlay);

    function toggleMenu() {
        const isOpen = mainNav.classList.toggle('is-active');
        menuBtn.classList.toggle('is-active');
        overlay.classList.toggle('is-active');
        body.style.overflow = isOpen ? 'hidden' : '';
        menuBtn.setAttribute('aria-expanded', isOpen);
    }

    function closeMenu() {
        mainNav.classList.remove('is-active');
        menuBtn.classList.remove('is-active');
        overlay.classList.remove('is-active');
        body.style.overflow = '';
        menuBtn.setAttribute('aria-expanded', 'false');
    }

    menuBtn.addEventListener('click', toggleMenu);
    overlay.addEventListener('click', closeMenu);

    // Cerrar menu al clicar en un enlace (no dropdown toggle)
    mainNav.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', closeMenu);
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape') {
            if (mainNav.classList.contains('is-active')) closeMenu();
            if (lightbox && lightbox.classList.contains('is-active')) closeLightbox();
            closeAllDropdowns();
        }
    });

    // ============================================
    // DROPDOWN MENU
    // ============================================
    const dropdownToggles = document.querySelectorAll('.dropdown-toggle');

    function closeAllDropdowns() {
        document.querySelectorAll('.has-dropdown.is-open').forEach(dd => {
            dd.classList.remove('is-open');
            dd.querySelector('.dropdown-toggle').setAttribute('aria-expanded', 'false');
        });
    }

    dropdownToggles.forEach(toggle => {
        toggle.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            const parent = toggle.closest('.has-dropdown');
            const isOpen = parent.classList.contains('is-open');

            // Cerrar todos los demas
            closeAllDropdowns();

            if (!isOpen) {
                parent.classList.add('is-open');
                toggle.setAttribute('aria-expanded', 'true');
            }
        });
    });

    // Cerrar dropdown al clicar fuera
    document.addEventListener('click', (e) => {
        if (!e.target.closest('.has-dropdown')) {
            closeAllDropdowns();
        }
    });

    // ============================================
    // HEADER DINAMICO (scroll)
    // ============================================
    const header = document.getElementById('main-header');
    let ticking = false;

    function updateHeader() {
        if (window.scrollY > 50) {
            header.classList.add('is-scrolled');
        } else {
            header.classList.remove('is-scrolled');
        }
        ticking = false;
    }

    window.addEventListener('scroll', () => {
        if (!ticking) {
            window.requestAnimationFrame(updateHeader);
            ticking = true;
        }
    });

    updateHeader();

    // ============================================
    // SCROLL REVEAL (IntersectionObserver)
    // ============================================
    const revealElements = document.querySelectorAll('.reveal-fade, .reveal-slide-up');

    if (revealElements.length > 0 && 'IntersectionObserver' in window) {
        const revealObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    revealObserver.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.1,
            rootMargin: '0px 0px -40px 0px'
        });

        revealElements.forEach(el => revealObserver.observe(el));
    } else {
        // Fallback: mostrar todo si no hay soporte
        revealElements.forEach(el => el.classList.add('is-visible'));
    }

    // ============================================
    // FAQ ACCORDION (details/summary nativo)
    // ============================================
    // El HTML usa <details>/<summary> nativos, que ya funcionan.
    // Anadimos logica para cerrar otros items al abrir uno (accordion behavior)
    const faqItems = document.querySelectorAll('.faq-item');

    faqItems.forEach(item => {
        item.addEventListener('toggle', () => {
            if (item.open) {
                // Cerrar los demas
                faqItems.forEach(other => {
                    if (other !== item && other.open) {
                        other.open = false;
                    }
                });
            }
        });
    });

    // ============================================
    // GALLERY FILTERS
    // ============================================
    const filterBtns = document.querySelectorAll('.filter-btn');
    const galleryItems = document.querySelectorAll('.gallery-item[data-category]');

    if (filterBtns.length > 0 && galleryItems.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const filter = btn.dataset.filter;

                // Actualizar boton activo
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                // Filtrar items
                galleryItems.forEach(item => {
                    if (filter === 'all' || item.dataset.category === filter) {
                        item.classList.remove('hidden');
                    } else {
                        item.classList.add('hidden');
                    }
                });
            });
        });
    }

    // ============================================
    // LIGHTBOX
    // ============================================
    const lightbox = document.getElementById('lightbox');
    const lightboxImg = document.getElementById('lightbox-img');
    const lightboxCaption = document.getElementById('lightbox-caption');
    const lightboxClose = document.querySelector('.lightbox-close');
    const lightboxPrev = document.querySelector('.lightbox-prev');
    const lightboxNext = document.querySelector('.lightbox-next');

    let lightboxImages = [];
    let currentLightboxIndex = 0;

    function collectVisibleImages() {
        lightboxImages = [];
        document.querySelectorAll('.gallery-item:not(.hidden)').forEach(item => {
            const img = item.querySelector('img');
            const overlayText = item.querySelector('.gallery-overlay span');
            if (img) {
                lightboxImages.push({
                    src: img.src,
                    alt: img.alt,
                    caption: overlayText ? overlayText.textContent : img.alt
                });
            }
        });
    }

    function openLightbox(index) {
        if (!lightbox || lightboxImages.length === 0) return;
        currentLightboxIndex = index;
        updateLightboxImage();
        lightbox.classList.add('is-active');
        lightbox.setAttribute('aria-hidden', 'false');
        body.style.overflow = 'hidden';
    }

    function closeLightbox() {
        if (!lightbox) return;
        lightbox.classList.remove('is-active');
        lightbox.setAttribute('aria-hidden', 'true');
        body.style.overflow = '';
    }

    function updateLightboxImage() {
        if (!lightboxImg) return;
        const data = lightboxImages[currentLightboxIndex];
        lightboxImg.src = data.src;
        lightboxImg.alt = data.alt;
        if (lightboxCaption) lightboxCaption.textContent = data.caption;
    }

    function nextLightboxImage() {
        currentLightboxIndex = (currentLightboxIndex + 1) % lightboxImages.length;
        updateLightboxImage();
    }

    function prevLightboxImage() {
        currentLightboxIndex = (currentLightboxIndex - 1 + lightboxImages.length) % lightboxImages.length;
        updateLightboxImage();
    }

    // Bind gallery items to open lightbox
    if (lightbox) {
        document.querySelectorAll('.gallery-item').forEach((item, index) => {
            item.addEventListener('click', () => {
                collectVisibleImages();
                // Encontrar el indice correcto del item clickeado dentro de los visibles
                const img = item.querySelector('img');
                const clickedSrc = img ? img.src : '';
                const visibleIndex = lightboxImages.findIndex(i => i.src === clickedSrc);
                openLightbox(visibleIndex >= 0 ? visibleIndex : 0);
            });
        });

        if (lightboxClose) lightboxClose.addEventListener('click', closeLightbox);
        if (lightboxNext) lightboxNext.addEventListener('click', nextLightboxImage);
        if (lightboxPrev) lightboxPrev.addEventListener('click', prevLightboxImage);

        // Cerrar al clicar fuera de la imagen
        lightbox.addEventListener('click', (e) => {
            if (e.target === lightbox) closeLightbox();
        });

        // Navegacion con teclado
        document.addEventListener('keydown', (e) => {
            if (!lightbox.classList.contains('is-active')) return;
            if (e.key === 'ArrowRight') nextLightboxImage();
            if (e.key === 'ArrowLeft') prevLightboxImage();
        });
    }

    // ============================================
    // FORM VALIDATION
    // ============================================
    const forms = document.querySelectorAll('.contact-form');

    forms.forEach(form => {
        form.addEventListener('submit', (e) => {
            e.preventDefault();

            let isValid = true;
            const requiredFields = form.querySelectorAll('[required]');

            // Limpiar estados previos
            form.querySelectorAll('.form-error').forEach(el => el.remove());
            form.querySelectorAll('.is-invalid').forEach(el => el.classList.remove('is-invalid'));

            requiredFields.forEach(field => {
                const value = field.value.trim();
                let errorMsg = '';

                if (!value) {
                    errorMsg = 'Este campo es obligatorio';
                } else if (field.type === 'email' && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value)) {
                    errorMsg = 'Introduce un email valido';
                }

                if (errorMsg) {
                    isValid = false;
                    field.classList.add('is-invalid');
                    const errorEl = document.createElement('span');
                    errorEl.classList.add('form-error');
                    errorEl.textContent = errorMsg;
                    field.parentElement.appendChild(errorEl);
                }
            });

            if (isValid) {
                // Simulacion de envio (sin backend por ahora)
                const submitBtn = form.querySelector('.btn-submit');
                const originalText = submitBtn.textContent;
                submitBtn.textContent = 'Enviado!';
                submitBtn.disabled = true;
                submitBtn.style.backgroundColor = '#4caf50';

                setTimeout(() => {
                    submitBtn.textContent = originalText;
                    submitBtn.disabled = false;
                    submitBtn.style.backgroundColor = '';
                    form.reset();
                }, 3000);
            }
        });

        // Limpiar error al escribir
        form.querySelectorAll('input, textarea, select').forEach(field => {
            field.addEventListener('input', () => {
                field.classList.remove('is-invalid');
                const error = field.parentElement.querySelector('.form-error');
                if (error) error.remove();
            });
        });
    });

});
