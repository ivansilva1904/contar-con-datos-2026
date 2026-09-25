// Manejo del ciclo de vida y eventos del modal de advertencia preventiva
document.addEventListener('DOMContentLoaded', () => {
  const modalOverlay = document.getElementById('warning-modal');
  const btnContinue = document.getElementById('btn-continue-reading');
  const btnExit = document.getElementById('btn-quick-exit');

  // Clave para guardar la confirmación durante la sesión del navegador
  const STORAGE_KEY = 'suicide_report_disclaimer_accepted';

  // Verificar si el usuario ya aceptó el aviso en esta sesión
  const hasAccepted = sessionStorage.getItem(STORAGE_KEY);

  if (!hasAccepted && modalOverlay) {
    // Desplegar el modal si no ha sido aceptado
    modalOverlay.classList.add('active');
    document.body.style.overflow = 'hidden'; // Evitar scroll de fondo mientras esté activo
  }

  // Evento: Continuar a la lectura del informe
  if (btnContinue && modalOverlay) {
    btnContinue.addEventListener('click', () => {
      sessionStorage.setItem(STORAGE_KEY, 'true');
      modalOverlay.classList.remove('active');
      document.body.style.overflow = ''; // Restaurar desplazamiento normal
    });
  }

  // Evento: Salida rápida hacia un sitio neutro o de contención
  if (btnExit) {
    btnExit.addEventListener('click', () => {
      // Redirección inmediata fuera del reporte
      window.location.href = 'https://www.google.com';
    });
  }
});