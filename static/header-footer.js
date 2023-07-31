const buttonMenu = document.querySelector('.header_block-menutel'),
 menu = document.querySelector('.header_menu2'),
 header = document.querySelector('.header');

const footerUnvisibleBlock = document.querySelector('#unvisible'),
 footerClickBlock = document.querySelector('#click'),
 footerBlockImg = document.querySelector('.footer_block-img');


document.addEventListener('DOMContentLoaded', (e) => {
    buttonMenu.addEventListener('click', (e) => {
        e.preventDefault();
        const isMenuVisible = menu.className.includes('show');
        if (isMenuVisible) {
            menu.className = menu.className.replace('show', '');
            header.className = header.className.replace('gradient', '');
        } else {
            menu.className += ' show';
            header.className += ' gradient';
        };
    });
    

    footerClickBlock.addEventListener('click', (e) => {
        e.preventDefault();
        const isFooterBlockVisible = footerUnvisibleBlock.className.includes('unvisible');
        if (isFooterBlockVisible) {
            footerUnvisibleBlock.className = footerUnvisibleBlock.className.replace('unvisible', ' show');
            footerBlockImg.className += ' down';
        } else {
            footerUnvisibleBlock.className = footerUnvisibleBlock.className.replace('show', ' unvisible');
            footerBlockImg.className = footerBlockImg.className.replace('down', '');
        };
    });

})


