const navLinks = document.querySelectorAll('header nav a');
const sections = document.querySelectorAll('section[id]');
const menuIcon = document.querySelector('#menu-icon');
const navBar = document.querySelector('header nav');

document.querySelectorAll('.read-more-btn').forEach(button => {
    button.addEventListener('click', function () {
        const target = this.previousElementSibling;
        if (target.classList.contains('expanded')) {
            target.classList.remove('expanded');
            this.textContent = 'See more';
        } else {
            target.classList.add('expanded');
            this.textContent = 'See less';
        }
    });
});

menuIcon.addEventListener('click', () => {
    menuIcon.classList.toggle('bx-x');
    navBar.classList.toggle('active');
});

navLinks.forEach(link => {
    link.addEventListener('click', () => {
        menuIcon.classList.remove('bx-x');
        navBar.classList.remove('active');
    });
});

const navObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            const id = entry.target.id;
            navLinks.forEach(link => {
                link.classList.toggle('active', link.getAttribute('href') === `#${id}`);
            });
        }
    });
}, { rootMargin: '-50% 0px -50% 0px', threshold: 0 });

sections.forEach(section => navObserver.observe(section));

const resumeBtns = document.querySelectorAll('.resume-btn');

resumeBtns.forEach((btn, idx) => {
    btn.addEventListener('click', () => {
        const resumeDetail = document.querySelectorAll('.resume-detail');

        resumeBtns.forEach(btn => {
            btn.classList.remove('active');
        });
        btn.classList.add('active');

        resumeDetail.forEach(detail => {
            detail.classList.remove('active');
        });
        resumeDetail[idx].classList.add('active');
    });
});
