document.addEventListener('DOMContentLoaded', function() {
    const galleryGrid = document.getElementById('galleryGrid');
    const galleryItems = document.querySelectorAll('.gallery-item');
    const loadMoreBtn = document.getElementById('loadMoreBtn');
    
    function updateGalleryDisplay() {
        // Calculate how many items are in one row
        const gridComputedStyle = window.getComputedStyle(galleryGrid);
        const gridWidth = galleryGrid.getBoundingClientRect().width;
        const itemWidth = galleryItems[0].getBoundingClientRect().width;
        const gap = parseInt(gridComputedStyle.columnGap);
        const itemsPerRow = Math.floor((gridWidth + gap) / (itemWidth + gap));
        
        // Show first two rows
        const itemsToShow = itemsPerRow * 2;
        
        // Hide all items first
        galleryItems.forEach((item, index) => {
            if (index < itemsToShow) {
                item.classList.remove('hidden');
            } else {
                item.classList.add('hidden');
            }
        });

        // Update current count
        currentlyShown = itemsToShow;

        // Show/hide load more button
        if (galleryItems.length <= itemsToShow) {
            loadMoreBtn.classList.add('hidden');
        } else {
            loadMoreBtn.classList.remove('hidden');
        }
    }

    // Initial setup
    updateGalleryDisplay();

    // Update on window resize
    window.addEventListener('resize', updateGalleryDisplay);

    // Load more button click handler
    loadMoreBtn.addEventListener('click', function() {
        const gridComputedStyle = window.getComputedStyle(galleryGrid);
        const gridWidth = galleryGrid.getBoundingClientRect().width;
        const itemWidth = galleryItems[0].getBoundingClientRect().width;
        const gap = parseInt(gridComputedStyle.columnGap);
        const itemsPerRow = Math.floor((gridWidth + gap) / (itemWidth + gap));
        
        // Show next two rows
        const nextItemsToShow = itemsPerRow * 2;
        
        for (let i = currentlyShown; i < currentlyShown + nextItemsToShow && i < galleryItems.length; i++) {
            galleryItems[i].classList.remove('hidden');
        }
        
        currentlyShown += nextItemsToShow;

        if (currentlyShown >= galleryItems.length) {
            loadMoreBtn.classList.add('hidden');
        }
    });

    // Enhanced Modal Image functionality
    const modal = document.getElementById('imageModal');
    const modalImg = document.getElementById('modalImg');
    const closeBtn = document.querySelector('.close-modal');
    let isZoomed = false;
    let isDragging = false;
    let startPos = { x: 0, y: 0 };
    let currentTranslate = { x: 0, y: 0 };

    document.querySelectorAll('.gallery-item img').forEach(img => {
        img.onclick = function(e) {
            modal.classList.add('active');
            modalImg.src = this.src;
            document.body.style.overflow = 'hidden';
            resetZoom();
        }
    });

    function resetZoom() {
        isZoomed = false;
        isDragging = false;
        currentTranslate = { x: 0, y: 0 };
        modalImg.classList.remove('zoomed');
        modalImg.style.transform = '';
    }

    modalImg.onclick = function(e) {
        if (!isDragging) {
            e.stopPropagation();
            isZoomed = !isZoomed;
            this.classList.toggle('zoomed');
            if (!isZoomed) {
                resetZoom();
            }
        }
    }

    // Dragging functionality
    modalImg.addEventListener('mousedown', dragStart);
    modalImg.addEventListener('mousemove', drag);
    modalImg.addEventListener('mouseup', dragEnd);
    modalImg.addEventListener('mouseleave', dragEnd);

    function dragStart(e) {
        if (isZoomed) {
            isDragging = true;
            modalImg.classList.add('dragging');
            startPos = {
                x: e.clientX - currentTranslate.x,
                y: e.clientY - currentTranslate.y
            };
        }
    }

    function drag(e) {
        if (isDragging && isZoomed) {
            e.preventDefault();
            currentTranslate = {
                x: e.clientX - startPos.x,
                y: e.clientY - startPos.y
            };
            modalImg.style.transform = `scale(1.5) translate(${currentTranslate.x}px, ${currentTranslate.y}px)`;
        }
    }

    function dragEnd() {
        isDragging = false;
        modalImg.classList.remove('dragging');
    }

    function closeModal() {
        modal.classList.remove('active');
        document.body.style.overflow = 'auto';
        resetZoom();
    }

    closeBtn.onclick = closeModal;
    modal.onclick = function(e) {
        if (e.target === modal) {
            closeModal();
        }
    };

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape' && modal.classList.contains('active')) {
            closeModal();
        }
    });

    // Secondary Navigation functionality
    const primaryNav = document.querySelector('.navbar');
    const secondaryNav = document.getElementById('secondaryNav');
    const primaryNavHeight = primaryNav.offsetHeight;
    const secondaryNavHeight = secondaryNav.offsetHeight;

    // Update active section in nav
    function updateActiveSection() {
        const sections = document.querySelectorAll('section[id]');
        const scrollPosition = window.scrollY + secondaryNavHeight + 10;

        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.secondary-nav a[href="#${sectionId}"]`);

            if (scrollPosition >= sectionTop && scrollPosition < sectionTop + sectionHeight) {
                navLink?.classList.add('active');
            } else {
                navLink?.classList.remove('active');
            }
        });
    }

    // Handle fixed navigation
    function handleFixedNav() {
        if (window.scrollY >= primaryNavHeight) {
            secondaryNav.classList.add('fixed-nav');
            document.body.classList.add('fixed-nav-active');
        } else {
            secondaryNav.classList.remove('fixed-nav');
            document.body.classList.remove('fixed-nav-active');
        }
    }

    // Smooth scroll to section
    document.querySelectorAll('.secondary-nav a[^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            const targetElement = document.querySelector(targetId);
            const offsetTop = targetElement.offsetTop - secondaryNavHeight;

            window.scrollTo({
                top: offsetTop,
                behavior: 'smooth'
            });
        });
    });

    // Event listeners
    window.addEventListener('scroll', () => {
        handleFixedNav();
        updateActiveSection();
    });

    // Initial check
    handleFixedNav();
    updateActiveSection();
});