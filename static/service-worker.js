self.addEventListener('install', function(e) {
  e.waitUntil(
    caches.open('calcolo-cache').then(function(cache) {
      return cache.addAll([
        '/',
        '/static/manifest.json',
        '/static/icons/icon-192.png',
        '/static/icons/icon-512.png'
        // puoi aggiungere altre risorse, css, js ecc.
      ]);
    })
  );
});

self.addEventListener('fetch', function(e) {
  e.respondWith(
    caches.match(e.request).then(function(response) {
      return response || fetch(e.request);
    })
  );
});
