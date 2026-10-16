
# Suicidio en Datos: Análisis de la Mortalidad por Suicidio en Argentina

[![Sitio Web](https://img.shields.io/badge/Web-suicidioendatos.com.ar-0F766E?style=for-the-badge&logo=google-chrome&logoColor=white)](https://suicidioendatos.com.ar)
[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Power BI](https://img.shields.io/badge/Power_BI-Dashboards-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)](https://powerbi.microsoft.com/)
[![Tableau](https://img.shields.io/badge/Tableau-Mapas-E97627?style=for-the-badge&logo=tableau&logoColor=white)](https://www.tableau.com/)

> **AVISO DE CONTENIDO SENSIBLE Y LÍNEAS DE AYUDA**  
> Este repositorio contiene datos estadísticos, código de procesamiento y visualizaciones sobre **mortalidad por suicidio en Argentina**, desarrollados con fines estrictamente educativos, preventivos y de divulgación en salud pública.
> 
> **Si vos, un familiar o alguien cercano está atravesando una situación emocional difícil o una crisis, no estás solo/a. Existen canales de asistencia confidenciales y gratuitos disponibles las 24 horas:**
> - **Línea Nacional de Salud Mental:** `0800-999-0091` (Todo el país, 24 hs)
> - **Centro de Asistencia al Suicida (CAS):** `135` (CABA y GBA) o `(011) 5275-1135` (Todo el país)

---

## Propósito del Proyecto

El suicidio es una problemática de salud pública compleja, multicausal pero, sobre todo, **prevenible**. El proyecto **Suicidio en Datos** (desarrollado en el marco de *Contar con Datos 2026*) nace con el objetivo de transformar registros estadísticos oficiales y públicos en información accesible, transparente y accionable. 

Buscamos aportar claridad sobre la evolución histórica, distribución demográfica y geográfica de esta problemática en Argentina, acompañando los datos con recursos de concientización para derribar mitos y facilitar el acceso temprano a redes de contención.

**Explorá el informe interactivo en vivo:** [suicidioendatos.com.ar](https://suicidioendatos.com.ar)

---

## Diseño Ético y Sensible (UX/UI Preventiva)

Comunicar datos sobre el suicidio exige una gran responsabilidad. Siguiendo las recomendaciones para el abordaje responsable de la salud mental en entornos digitales, la plataforma web incorpora:

1. **Modal de Advertencia Preventiva (*Trigger Warning*):** Al ingresar al sitio, se informa al usuario sobre la naturaleza sensible del contenido antes de exponer cualquier gráfico, ofreciendo un botón de **"Salida rápida a un sitio seguro"** y números de asistencia inmediata.
2. **Cintillo de Ayuda Permanente (*Lifeline Banner*):** Una barra superior fija que acompaña la lectura en todo momento con los teléfonos de emergencia.
3. **Copiado Rápido al Portapapeles (*Click-to-Copy*):** Los números telefónicos de ayuda cuentan con interacción directa para ser copiados con un solo clic, facilitando su uso en situaciones de urgencia.
4. **Sección Educativa "Mitos vs. Realidades":** Componentes interactivos orientados a desarmar estigmas comunes en la comunidad.
5. **Accesibilidad Visual y Modo Oscuro:** Paleta de colores pensada para la salud visual (tonos *teal* de calma institucional y alertas en ámbar suave), con soporte nativo para tema claro y oscuro.

---

## Fuentes de Datos y Metodología

El análisis integra y contrasta tres fuentes principales de datos públicos y anonimizados de la República Argentina:

1. **DEIS (Dirección de Estadísticas e Información en Salud - Ministerio de Salud):**
   - **Período:** 2005 – 2024.
   - **Criterio de filtrado:** Defunciones registradas bajo los códigos **CIE-10: X60 a X84** (lesiones autoinfligidas intencionalmente).
   - **Nota metodológica:** Se excluyen registros con residencia en el extranjero (`PROVRES != 98`) para el análisis jurisdiccional, y se documentan hallazgos específicos de codificación (como registros con sexo indeterminado/desconocido).
   - [**Link**](https://www.argentina.gob.ar/salud/deis/datos/defunciones)

2. **SNIC (Sistema Nacional de Información Criminal - Ministerio de Seguridad):**
   - **Período:** 2000 – 2025.
   - **Criterio de filtrado:** Hechos registrados bajo el `codigo_delito_snic_id == "31"` (Suicidios consumados).
   - **Tratamiento temporal:** Normalización de registros mensuales y construcción de series temporales para el estudio de estacionalidad.
   - [**Link**](https://www.argentina.gob.ar/seguridad/estadisticascriminales/bases-de-datos) (Es el archivo CSV "SNIC - Departamentos. Mensual. Años 2000-2025")

3. **INDEC (Instituto Nacional de Estadística y Censos):**
   - **Período:** Proyecciones departamentales y provinciales 2010 – 2025 (Informe Demográfico N° 38).
   - **Uso:** Base poblacional para el cálculo de tasas estandarizadas cada 100.000 habitantes.
   - [**Link**](https://biblioteca.indec.gob.ar/bases/minde/4si20_38.pdf)

**Transparencia Analítica:** Uno de los ejes centrales del informe es visibilizar las discrepancias metodológicas y de volumen de casos registrados entre la fuente sanitaria (DEIS) y la fuente de seguridad (SNIC), brindando al lector el contexto necesario para interpretar ambas curvas con rigor estadístico.

---

## Visualizaciones y Dashboards Incluidos

La plataforma integra reportes interactivos desarrollados en **Microsoft Power BI** y **Tableau Public**:

- **Evolución Comparativa de Fuentes:** Contraste histórico de casos totales y variación interanual entre DEIS (2005-2024) y SNIC (2000-2025).
- **Reporte 2025:** Panel interactivo con los indicadores más recientes registrados por el SNIC.
- **Distribución por Grupos Etarios:** Análisis generacional y de franjas de edad más expuestas (DEIS 2005-2024).
- **Distribución por Sexo:** Comparativa histórica y desglose detallado a nivel provincial.
- **Distribución Geográfica (Tableau):** Mapa interactivo de tasas y concentraciones espaciales por provincia.
- **Análisis de Estacionalidad:** Estudio del comportamiento mensual (media y mediana) a lo largo de 25 años de registros.

---

## Estructura del Repositorio

```text
├── css/                                # Hojas de estilo modulares (CSS3 nativo y variables)
│   ├── accordion.css                   # Estilos del módulo Mitos vs. Realidades
│   ├── base.css                        # Reset y tipografía base (Plus Jakarta Sans)
│   ├── components.css                  # Cintillo de ayuda, botones, tabs y utilidades
│   ├── layout.css                      # Grillas, contenedores responsivos y footer
│   ├── loader.css                      # Skeleton loaders animados para los iframes
│   ├── modal.css                       # Ventana modal de advertencia de contenido
│   └── variables.css                   # Tokens de diseño y paleta (Modo Claro / Oscuro)
├── data/                               # Datos procesados y archivos de Business Intelligence
│   ├── dashboards/                     # Archivos fuente de Power BI (.pbix) y Tableau (.twbx)
│   ├── raw data/                       # Archivos .csv y .xlsx con los datos sin procesar
│   ├── deis_tabla.xlsx                 # Dataset limpio y unificado de DEIS (2005-2024)
│   ├── descdef1.xlsx                   # Diccionario de códigos y descriptores (DEIS)
│   ├── poblacion_estimaciones_tabla.xlsx # Proyecciones de población en formato tabular (INDEC)
│   └── snic_tabla.xlsx                 # Dataset limpio y filtrado del SNIC (2000-2025)
├── js/                                 # Lógica de cliente en Vanilla JavaScript
│   ├── accordion.js                    # Interactividad accesible (ARIA) de acordeones
│   ├── loader.js                       # Gestión de carga asíncrona de iframes y skeletons
│   ├── main.js                         # Scroll-to-top, sticky header y click-to-copy
│   ├── modal.js                        # Control de sesión (sessionStorage) del aviso preventivo
│   ├── navigation.js                   # Scrollspy para la barra de navegación
│   └── theme.js                        # Persistencia de tema claro/oscuro (localStorage)
├── scripts/                            # Pipelines ETL de limpieza de datos en Python
│   ├── procesado_tabla_deis.py         # Consolidación de 20 CSVs anuales y cruce de catálogos
│   ├── procesado_tabla_poblacion.py    # Transformación (melt) de proyecciones INDEC
│   └── procesado_tabla_snic.py         # Filtrado, limpieza e indexación temporal del SNIC
├── CNAME                               # Configuración de dominio personalizado
├── index.html                          # Punto de entrada de la aplicación web
└── README.md                           # Documentación del proyecto
```

---

## Contribuciones y Uso de la Información

Este es un proyecto de **código abierto** con fines comunitarios, académicos y periodísticos. Si encontrás algún error en el procesamiento de los datos, mejoras de accesibilidad web o sugerencias en la comunicación preventiva, podés abrir un **Issue** o enviar un **Pull Request**.
