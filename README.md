# 🎨 Pintacaras Facepainting - Web Renewal Project

Este repositorio contiene el código fuente para la renovación total del sitio web de **Pintacaras Facepainting Madrid**. 

El objetivo del proyecto es migrar una web antigua basada en WordPress (2014) a una solución moderna, performante y hecha a medida (**Vanilla HTML/CSS/JS**), mejorando la experiencia de usuario (UX), el SEO técnico y la velocidad de carga (Core Web Vitals).

## 🚀 Tecnologías y Herramientas

Este proyecto sigue una filosofía **"No-Framework"** (por el momento) para asegurar un control total sobre el DOM y el rendimiento, consolidando fundamentos de Ingeniería Web.

* **HTML5 Semántico:** Estructura optimizada para accesibilidad y SEO (`<header>`, `<main>`, `<section>`, `<article>`).
* **CSS3 Moderno:**
    * **CSS Variables (Custom Properties):** Para gestión de temas y mantenibilidad.
    * **Flexbox:** Para layouts unidimensionales (Menú de navegación, Hero section).
    * **CSS Grid:** Para layouts bidimensionales complejos (Galería de imágenes responsive).
    * **Metodología BEM (Inspiración):** Naming convention para clases CSS limpias.
* **JavaScript (ES6+):** Lógica del lado del cliente (en desarrollo).
* **Control de Versiones:** Git & GitHub.
* **Entorno:** VS Code + Live Server.

## 🛠️ Estructura del Proyecto

```text
/
├── assets/
│   ├── img/          # Imágenes optimizadas (WebP/JPG comprimidos)
│   └── icons/        # Iconos SVG
├── css/
│   └── style.css     # Hoja de estilos principal (Mobile First approach)
├── js/
│   └── main.js       # Scripts de interacción
├── index.html        # Landing Page principal
└── README.md         # Documentación
```

## 🎯 Objetivos de Ingeniería (KPIs)

* **Performance:** Alcanzar una puntuación de **95+** en Google Lighthouse (Performance & Best Practices).
* **SEO:** Implementación correcta de jerarquía de encabezados (`h1`-`h6`), atributos `alt` y metaetiquetas.
* **Responsividad:** Diseño fluido que se adapta desde móviles (320px) hasta pantallas 4K.
* **Clean Code:** Código legible, comentado y escalable.

## 📦 Instalación y Despliegue Local

Para visualizar este proyecto en tu máquina local:

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/juansagaro/pintacaras-web.git](https://github.com/juansagaro/pintacaras-web.git)
    ```

2.  **Navega al directorio:**
    ```bash
    cd pintacaras-web
    ```

3.  **Abre el proyecto** en tu editor favorito (recomendado VS Code).

4.  **Ejecuta el servidor:** Usa la extensión **Live Server** para lanzar el entorno local.

## 🚧 Estado del Proyecto

- [x] Configuración inicial y estructura de carpetas.
- [x] Header y Navegación Responsive (Flexbox).
- [x] Hero Section con imagen de fondo y Overlay.
- [x] Galería de trabajos (CSS Grid + auto-fit).
- [ ] Sección de Servicios detallada.
- [ ] Formulario de Contacto y validación JS.
- [ ] Footer legal.
- [ ] Despliegue en producción (Netlify/Vercel).

---
**Autor:** Juan Sagaro