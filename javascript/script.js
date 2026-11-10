(() => {
    const root = document.documentElement;
    const header = document.querySelector('.site-header');
    const nav = document.getElementById('nav');
    const navLinks = nav.querySelectorAll('a');
    const menuBtn = document.getElementById('menu-toggle');
    const themeBtn = document.getElementById('theme-toggle');

    /* ---- Theme: follow the system until the visitor picks one ---- */
    const systemDark = window.matchMedia('(prefers-color-scheme: dark)');

    const currentTheme = () =>
        root.getAttribute('data-theme') || (systemDark.matches ? 'dark' : 'light');

    const labelThemeButton = () => {
        const next = currentTheme() === 'dark' ? 'light' : 'dark';
        themeBtn.setAttribute('aria-label', `Switch to ${next} theme`);
    };

    themeBtn.addEventListener('click', () => {
        const next = currentTheme() === 'dark' ? 'light' : 'dark';
        root.setAttribute('data-theme', next);
        try {
            localStorage.setItem('theme', next);
        } catch (e) {
            /* storage unavailable: the choice lasts for this visit only */
        }
        labelThemeButton();
    });

    systemDark.addEventListener('change', labelThemeButton);
    labelThemeButton();

    /* ---- Mobile menu ---- */
    const setMenu = (open) => {
        nav.classList.toggle('open', open);
        menuBtn.setAttribute('aria-expanded', String(open));
        menuBtn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
    };

    menuBtn.addEventListener('click', () => setMenu(!nav.classList.contains('open')));
    navLinks.forEach((link) => link.addEventListener('click', () => setMenu(false)));
    document.addEventListener('keydown', (event) => {
        if (event.key === 'Escape') setMenu(false);
    });

    /* ---- Header hairline once the page scrolls ---- */
    const onScroll = () => header.classList.toggle('scrolled', window.scrollY > 8);
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();

    /* ---- Highlight the nav link for the section in view ---- */
    const sections = document.querySelectorAll('main section[id]');
    const navObserver = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
            if (!entry.isIntersecting) return;
            const id = entry.target.id;
            navLinks.forEach((link) => {
                link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
            });
        });
    }, { rootMargin: '-45% 0px -50% 0px', threshold: 0 });

    sections.forEach((section) => navObserver.observe(section));
})();
