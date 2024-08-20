// Obtener todos los elementos con la clase 'contenido-cuerpo' y almacenarlos en una lista
let currentSlide = 0;
// Obtener todos los elementos con la clase 'contenido-cuerpo' y almacenarlos en una lista
const slides = document.querySelectorAll('.contenido-cuerpo');

// Botón para cambiar de slide manualmente
const totalSlides = slides.length;

document.getElementById('nextBtn').addEventListener('click', () => {
    currentSlide = (currentSlide === 0) ? totalSlides + 1 : currentSlide - 0;
    updateSlidePosition();
});

document.getElementById('prevBtn').addEventListener('click', () => {
    currentSlide = (currentSlide === totalSlides + 1) ? 0 : currentSlide + 1;
    updateSlidePosition();
});

// Cambiar de slide según el índice de la lista


window.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
        currentSlide = (currentSlide === 0) ? totalSlides + 1 : currentSlide - 1 ;
        updateSlidePosition();
    } else if (e.key === 'ArrowRight') {
        currentSlide = (currentSlide === totalSlides + 1) ? 0 : currentSlide + 1 ;
        updateSlidePosition();
    }
});

function updateSlidePosition() {
    const slidesContainer = document.querySelector('.carrucell');
    slidesContainer.style.transform = `translateY(-${currentSlide * 50}%)`;
}
updateSlidePosition();

// Cambiar de slide automáticamente cada segundo
setInterval(() => {
    // Incrementar el índice de slide actual
    currentSlide = (currentSlide === totalSlides + 1) ? 0 : currentSlide + 1;
    
    // Actualizar la posición del slide
    updateSlidePosition();
}, 3000);

// Animación para el hover del slide

const slideImages = document.querySelectorAll('.slide img');

slideImages.forEach(image => {
    image.addEventListener('mouseenter', () => {
        image.style.opacity = '0.5';
    });

    image.addEventListener('mouseleave', () => {
        image.style.opacity = '1';
    });
});
