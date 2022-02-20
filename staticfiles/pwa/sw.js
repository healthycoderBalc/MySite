// sw de static

var CACHE_NAME = 'pwa-cache-v1';
	var urlsToCache = [
		'/offline',
		// '/static/pwa/images/dino.gif',
		// 'sw de static'
		'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',
		
		'https://cdn.jsdelivr.net/npm/@popperjs/core@2.10.2/dist/umd/popper.min.js',
		// 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.min.js',


        // 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css',


        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/bootstrap-icons.css',
        'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js',
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/fonts/bootstrap-icons.woff2?30af91bf14e37666a085fb8a161ff36d',
        'https://cdn.jsdelivr.net/npm/bootstrap-icons@1.7.2/font/fonts/bootstrap-icons.woff?30af91bf14e37666a085fb8a161ff36d',
        'static/pwa/img/AyM.png',
        'static/pwa/img/AyM-internet.png',
		'/sw.js',
		'/app.js',
		'/manifest.json',

		];
	const self = this;
	
	// Install SW
	self.addEventListener('install', (event) =>{
		event.waitUntil(
			caches.open(CACHE_NAME)
				.then((cache) => {
					console.log('Opend Cache.');
					
					return cache.addAll(urlsToCache);
				})
			)
	});

	// Listen For requests
	self.addEventListener('fetch', (event) =>{
		event.respondWith(
			caches.match(event.request)
				.then(() => {
					return fetch(event.request)
						.catch(() => caches.match('/offline'))
				})
		)
	});

	// Activate
	self.addEventListener('activate', (event) =>{
		const cacheWhitelist = [];
		cacheWhitelist.push(CACHE_NAME);
	 	event.waitUntil(
			caches.keys().then((cacheNames) => Promise.all(
				cacheNames.map((cacheName) => {
					if (!cacheWhitelist.includes(cacheName)) {
						return caches.delete(cacheName);
						}
					})
				))
			)
	});