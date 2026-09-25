// Gestión de estado de carga para iframes externos de Power BI o Tableau
document.addEventListener('DOMContentLoaded', () => {
  const iframeContainers = document.querySelectorAll('.iframe-container');

  iframeContainers.forEach((container) => {
    const iframe = container.querySelector('iframe');
    const skeleton = container.querySelector('.skeleton-overlay');

    if (!iframe || !skeleton) return;

    // Función para retirar la animación del skeleton
    const dismissSkeleton = () => {
      skeleton.classList.add('loaded');
      setTimeout(() => {
        skeleton.style.display = 'none';
      }, 400); // Tiempo alineado con la transición de opacidad en CSS
    };

    // Evento estándar: el contenido del iframe terminó de procesarse
    iframe.addEventListener('load', () => {
      dismissSkeleton();
    });

    // Respaldo de seguridad: ocultar el skeleton si pasan más de 10 segundos
    setTimeout(() => {
      if (!skeleton.classList.contains('loaded')) {
        dismissSkeleton();
      }
    }, 10000);
  });
});