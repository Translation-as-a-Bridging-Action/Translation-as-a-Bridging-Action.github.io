document.addEventListener('DOMContentLoaded', () => {
    const abstract = document.getElementById('abstract');
    const demos = document.getElementById('demos');
    const bridge = document.getElementById('bridge');
    const method = document.getElementById('method');
    if (abstract && demos) {
        abstract.insertAdjacentElement('afterend', demos);
    }
    if (bridge && method) {
        method.insertAdjacentElement('afterend', bridge);
    }

    document.querySelectorAll('.carousel').forEach((carousel) => {
        const track = carousel.querySelector('.video-track');
        const prev = carousel.querySelector('.carousel-btn.prev');
        const next = carousel.querySelector('.carousel-btn.next');
        if (!track || !prev || !next) return;
        const step = () => {
            const card = track.querySelector('.video-card');
            const gap = 20;
            return card ? card.offsetWidth + gap : 360;
        };
        const update = () => {
            const maxScroll = track.scrollWidth - track.clientWidth - 2;
            prev.disabled = track.scrollLeft <= 2;
            next.disabled = track.scrollLeft >= maxScroll;
        };
        prev.addEventListener('click', () => track.scrollBy({ left: -step(), behavior: 'smooth' }));
        next.addEventListener('click', () => track.scrollBy({ left: step(), behavior: 'smooth' }));
        track.addEventListener('scroll', update, { passive: true });
        window.addEventListener('resize', update);
        update();
    });

    const copyBtn = document.getElementById('copyBib');
    const bibText = document.getElementById('bibText');
    if (copyBtn && bibText) {
        copyBtn.addEventListener('click', async () => {
            try {
                await navigator.clipboard.writeText(bibText.innerText);
                copyBtn.textContent = 'Copied!';
                copyBtn.classList.add('copied');
                setTimeout(() => {
                    copyBtn.textContent = 'Copy';
                    copyBtn.classList.remove('copied');
                }, 1600);
            } catch (e) {
                copyBtn.textContent = 'Press Ctrl+C';
            }
        });
    }
});
