// Funcionalidades principales de la web
document.addEventListener('DOMContentLoaded', () => {
  // 1. Inicializar botón de volver arriba
  setupScrollTop();

  // 2. Inicializar copia de números al portapapeles
  setupClickToCopy();

  // 3. Inicializar la reducción del cintillo al scrollear
  setupStickyHeader();

});

// Switcher para alternar entre la Vista General y el Informe Ejecutivo en Power BI
function setupDashboardTabs() {
  const tabButtons = document.querySelectorAll('.tab-btn');
  const iframe = document.getElementById('sexo-iframe');
  const container = document.getElementById('sexo-iframe-container');

  if (!tabButtons.length || !iframe || !container) return;

  tabButtons.forEach((button) => {
    button.addEventListener('click', () => {
      // Evitar recargar si ya está activa
      if (button.classList.contains('active')) return;

      const newUrl = button.getAttribute('data-url');
      const newAspect = button.getAttribute('data-aspect');
      const skeleton = container.querySelector('.skeleton-overlay');

      // 1. Actualizar estado visual de los botones
      tabButtons.forEach((btn) => btn.classList.remove('active'));
      button.classList.add('active');

      // 2. Reactivar el Skeleton Loader mientras se descarga la nueva vista
      if (skeleton) {
        skeleton.style.display = 'flex';
        skeleton.classList.remove('loaded');
      }

      // 3. Ajustar las proporciones del contenedor (16:9 o vertical)
      container.classList.remove('aspect-16-9', 'aspect-vertical');
      container.classList.add(newAspect);

      // 4. Cargar la nueva URL en el iframe
      iframe.src = newUrl;
    });
  });
}

// Reduce la altura del cintillo cuando el usuario hace scroll
function setupStickyHeader() {
  const headerWrapper = document.querySelector('.header-sticky-wrapper');

  if (headerWrapper) {
    window.addEventListener('scroll', () => {
      // Si el usuario scrollea más de 30px, añade la clase 'scrolled'
      if (window.pageYOffset > 30) {
        headerWrapper.classList.add('scrolled');
      } else {
        headerWrapper.classList.remove('scrolled');
      }
    });
  }
}

// Lógica del botón Volver Arriba
function setupScrollTop() {
  const scrollTopBtn = document.getElementById('scroll-top-btn');

  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.pageYOffset > 400) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });

    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }
}

// Lógica de copia rápida de números
function setupClickToCopy() {
  const copyElements = document.querySelectorAll('.copy-phone');

  copyElements.forEach((el) => {
    el.addEventListener('click', async () => {
      // Obtener el número desde el atributo data-phone o del texto contenido
      const textToCopy = el.getAttribute('data-phone') || el.innerText.trim();

      try {
        await navigator.clipboard.writeText(textToCopy);

        // Feedback visual al copiar con éxito
        const originalText = el.getAttribute('title') || 'Clic para copiar';

        el.setAttribute('title', '¡Número copiado!');
        el.classList.add('copied');

        setTimeout(() => {
          el.setAttribute('title', originalText);
          el.classList.remove('copied');
        }, 2000);
      } catch (err) {
        console.error('Error al copiar al portapapeles:', err);
      }
    });
  });
}