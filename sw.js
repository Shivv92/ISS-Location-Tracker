// This is the Service Worker that tricks the phone into thinking this is a native app
self.addEventListener('install', (e) => {
    console.log('[Service Worker] Installed');
});

self.addEventListener('fetch', (e) => {
    // A dummy fetch handler is required by Chrome to show the Install button
});