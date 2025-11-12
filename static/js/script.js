// HTMX - Loading simples
document.body.addEventListener('htmx:beforeRequest', function(e) {
    e.target.classList.add('loading');
});

document.body.addEventListener('htmx:afterRequest', function(e) {
    e.target.classList.remove('loading');
});

// Efeito digitação em loop infinito
document.addEventListener('DOMContentLoaded', function() {
    const title = document.querySelector('.hero-title');
    if (title) {
        const originalText = title.textContent;
        
        function typeWriter() {
            title.textContent = '';
            let i = 0;
            
            function type() {
                if (i < originalText.length) {
                    title.textContent += originalText[i];
                    i++;
                    setTimeout(type, 100);
                } else {
                    // Quando terminar, espera 2 segundos e recomeça
                    setTimeout(typeWriter, 2000);
                }
            }
            type();
        }
        
        // Inicia o loop
        typeWriter();
    }
});