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


document.addEventListener('DOMContentLoaded', function () {
    const addToCartButtons = document.querySelectorAll('.add-to-cart');

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function () {
            const productId = this.getAttribute('data-product-id');
            addToCart(productId);
        });
    });

    function addToCart(productId) {
        // Aquí puedes hacer una llamada AJAX para agregar el producto al carrito en el servidor
        console.log(`Producto ${productId} agregado al carrito`);

        // Ejemplo de actualización del carrito en el frontend
        const cartCount = document.getElementById('cart-count');
        cartCount.textContent = parseInt(cartCount.textContent) + 1;
    }
});

