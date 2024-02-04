// Obtén todas las imágenes del carrusel
var slides = document.querySelectorAll('.carousel img');

// Índice de la imagen actual
var slideIndex = 0;

// Muestra la primera imagen
slides[slideIndex].style.display = 'block';

// Cambia a la siguiente imagen cada 2 segundos
setInterval(nextSlide, 2000);

function nextSlide() {
    // Oculta la imagen actual
    slides[slideIndex].style.display = 'none';

    // Incrementa el índice
    slideIndex++;

    // Si llegamos al final, vuelve al principio
    if (slideIndex >= slides.length) {
        slideIndex = 0;
    }

    // Muestra la siguiente imagen
    slides[slideIndex].style.display = 'block';
}
