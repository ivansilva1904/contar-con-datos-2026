// Manejo interactivo de los acordeones de Mitos y Realidades
document.addEventListener('DOMContentLoaded', () => {
  const triggers = document.querySelectorAll('.accordion-trigger');

  triggers.forEach((trigger) => {
    trigger.addEventListener('click', () => {
      const item = trigger.closest('.accordion-item');
      const content = item.querySelector('.accordion-collapse');
      const isOpen = item.classList.contains('open');

      if (isOpen) {
        // Cerrar el panel
        content.style.maxHeight = null;
        item.classList.remove('open');
        trigger.setAttribute('aria-expanded', 'false');
      } else {
        // Abrir el panel
        item.classList.add('open');
        content.style.maxHeight = `${content.scrollHeight}px`;
        trigger.setAttribute('aria-expanded', 'true');
      }
    });
  });
});