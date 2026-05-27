const navLinks = document.querySelectorAll('header nav a');
const logoLinks = document.querySelector('.logo'); //rfere to class logo
const sections = document.querySelectorAll('section');
const menuIcon = document.querySelector('#menu-icon');
const navBar = document.querySelector('header nav');

document.querySelectorAll('.read-more-btn').forEach(button => {
    button.addEventListener('click', function () {
        const description = this.previousElementSibling; // Select the <p> element
        if (description.classList.contains('expanded')) {
            description.classList.remove('expanded');
            this.textContent = 'See more';
        } else {
            description.classList.add('expanded');
            this.textContent = 'See less';
        }
    });
});

document.querySelectorAll('.read-more-btn').forEach(button => {
    button.addEventListener('click', function () {
        const description = this.previousElementSibling.querySelector('.project-content'); // Get the .project-content div
        if (description.classList.contains('expanded')) {
            description.classList.remove('expanded');
            this.textContent = 'See more';
        } else {
            description.classList.add('expanded');
            this.textContent = 'See less';
        }
    });
});



menuIcon.addEventListener('click', () => {
    menuIcon.classList.toggle('bx-x');
    navBar.classList.toggle('active');
});

const activePage = () => {
    const header = document.querySelector('header')
    const barsBox = document.querySelector('.bars-box')

    header.classList.remove('active');
    setTimeout(() => {
        header.classList.add('active');
    }, 1100);

    navLinks.forEach(link => {
        link.classList.remove('active');
    });

    barsBox.classList.remove('active');
    setTimeout(() => {
        barsBox.classList.add('active');
    }, 1100);

    sections.forEach(section => {
        section.classList.remove('active');
    });

    menuIcon.classList.remove('bx-x');
    navBar.classList.remove('active');
}

navLinks.forEach((link, idx) => {
    link.addEventListener('click', () => {
        if (!link.classList.contains('active')) {
            activePage();
            link.classList.add('active');

            setTimeout(() => {
                sections[idx].classList.add('active');
            }, 1100);
        }
    });
});

logoLinks.addEventListener('click', () => {
    if (!navLinks(0).classList.contains('active')) {
        activePage();
        navLinks[0].classList.add('active');

        setTimeout(() => {
            sections[0].classList.add('active');
        }, 1100);
    }
});

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


