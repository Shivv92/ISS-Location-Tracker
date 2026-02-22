const CACHE_NAME = 'pro-radar-v1';

// 1. When installed, force it to cache the core files
self.addEventListener('install', (e) => {
    e.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll([
                './',
                './index.html',
                './manifest.json'
            ]);
        })
    );
    self.skipWaiting();
});

// 2. Claim control immediately
self.addEventListener('activate', (e) => {
    e.waitUntil(clients.claim());
});

// 3. The Offline Network Trap (This proves to Chrome we are a real app)
self.addEventListener('fetch', (e) => {
    e.respondWith(
        fetch(e.request).catch(() => {
            return caches.match(e.request);
        })
    );
});