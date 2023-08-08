
document.addEventListener('DOMContentLoaded', (e) => {
  const text = document.querySelectorAll('#books_text-none');
  text.forEach((item) => {
    item.style.display = 'none';
});



  const readMoreButtons = document.querySelectorAll('.books_block-readmore');
  readMoreButtons.forEach((button) => {
    button.addEventListener('click', function () {
      const text = this.parentNode.parentNode.querySelector('#books_text-none');
      if (text.style.display === 'none') {
        text.style.display = 'inline';
        this.textContent = 'Сховати';
      } else {
        text.style.display = 'none';
        this.textContent = 'Читати Більше...';
      }
    });
  });
  const containerBooks = document.querySelector('#books_block-container')
    if(matchMedia) {
      let screen = window.matchMedia("(max-width:600px)");
      screen.addListener(changes);
      changes(screen);
    }
    function changes(screen) {
      if (screen.matches) {
        containerBooks.className = containerBooks.className.replace('books_block-container -container', 'books_block-container')
      } else {
        containerBooks.className = containerBooks.className.replace('books_block-container', 'books_block-container -container')
      }
    }
})