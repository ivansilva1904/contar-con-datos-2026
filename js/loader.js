// Carga ágil sin retrasos artificiales
document.addEventListener('DOMContentLoaded', () => {
  const iframeContainers = document.querySelectorAll('.iframe-container');

  iframeContainers.forEach((container) => {
    const iframe = container.querySelector('iframe');
    const skeleton = container.querySelector('.skeleton-overlay');

    if (!iframe || !skeleton) return;

    // Ocultar el skeleton inmediatamente cuando el iframe responde
    const hideSkeleton = () => {
      skeleton.classList.add('loaded');
      setTimeout(() => {
        skeleton.style.display = 'none';
      }, 300); // Coincide con la transición fade-out de CSS
    };

    iframe.addEventListener('load', hideSkeleton);

    // Timeout de respaldo a los 8 segundos por si falla la red
    setTimeout(() => {
      if (!skeleton.classList.contains('loaded')) {
        hideSkeleton();
      }
    }, 8000);
  });
});