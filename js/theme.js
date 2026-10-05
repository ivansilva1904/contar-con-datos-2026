// Manejo del estado y preferencia del Modo Oscuro
document.addEventListener('DOMContentLoaded', () => {
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const STORAGE_KEY = 'suicide_report_theme_preference';

  // 1. Obtener preferencia guardada; por defecto SIEMPRE 'light'
  const getPreferredTheme = () => {
    const savedTheme = localStorage.getItem(STORAGE_KEY);
    if (savedTheme) {
      return savedTheme;
    }
    // Forzado a 'light' por defecto independientemente de la configuración del SO
    return 'light';
  };

  // 2. Aplicar el tema en el elemento <html> raíz
  const setTheme = (theme) => {
    if (theme === 'dark') {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
    localStorage.setItem(STORAGE_KEY, theme);
  };

  // Inicializar tema al cargar la página
  const currentTheme = getPreferredTheme();
  setTheme(currentTheme);

  // 3. Evento del botón selector de tema
  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const isDark = document.documentElement.getAttribute('data-theme') === 'dark';
      const newTheme = isDark ? 'light' : 'dark';
      setTheme(newTheme);
    });
  }
});