anime({
    targets: 'div.circle',
    scale: {
        value: 1.7,
        duration: 1600,
        delay: 800,
        easing: 'easeInOutQuart'
    },
    rotate: '1turn',
    duration: 2000,
});
anime({
    targets: 'div.circle-module',
    rotate: '1turn',
    scale: 1.9,
    duration: 2000,
});
anime({
    targets: 'div.error-img',
    translateX: [120,-120],
    rotate: '1turn',
    easing: 'easeInOutQuart',
    direction: 'alternate',
    duration: 15000,
    loop: true,
});
