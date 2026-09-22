# Flores amarillas para mi amiga

Regalo de David para amiga · 21 de septiembre de 2026.

## Abrir

Abre `dist/index.html` directamente en Chrome, Edge, Firefox o Safari. La carpeta `dist` contiene la página completa: puedes copiarla y abrirla sin instalar nada y sin Internet. También puedes servirla con un servidor estático.

## Poner vuestras fotografías

1. Copia `memory-1.jpg` hasta `memory-6.jpg` en `dist/assets/images/memories/`.
2. Al principio de `dist/js/main.js`, cambia cada `src` en `MEMORIES` por `assets/images/memories/memory-1.jpg`, etc. Cambia también `alt` para describir vuestra foto y `caption` para personalizar el mensaje.
3. Conserva `fallback`: si una foto personal no existe, se muestra la flor de respaldo.

## Música

Incluye `assets/audio/ambient.wav`, una melodía original de 48 segundos creada por síntesis, sin muestras comerciales. Solo comienza tras una interacción. El botón de la esquina activa o silencia; volumen inicial 16 %.

Para usar otra pista, copia un archivo autorizado a `dist/assets/audio/music.mp3` y cambia `MUSIC_SOURCE` en `dist/js/main.js`. No se entrega un MP3 vacío para evitar errores.

## Organización

- `dist/index.html`: textos, escenas y diálogos.
- `dist/css/style.css`: diseño adaptable, animaciones y movimiento reducido.
- `dist/js/main.js`: apertura, ramo, tarjetas, galería, sobre, jardín, música y sorpresa.
- `dist/assets/images/`: seis fotografías locales optimizadas WebP.
- `dist/assets/fonts/`: Cormorant Garamond y Manrope locales.
- `dist/assets/icons/`: favicon.
- `IMAGE-CREDITS.json`: autor, enlace y licencia de cada fotografía.
- `prepare-resources.py`: fuentes y generación reproducible de la música.

No utiliza servicios externos durante la visita ni guarda información personal. Las animaciones respetan `prefers-reduced-motion`; las tarjetas y diálogos admiten teclado y Escape. El ramo y el jardín están dibujados en SVG según lo solicitado.

No había video de referencia en la carpeta recibida: se siguieron las indicaciones escritas de transiciones, profundidad y movimiento.
