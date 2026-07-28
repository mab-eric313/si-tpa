import { sveltekit } from '@sveltejs/kit/vite';
import { defineConfig } from 'vite';

export default defineConfig({
	plugins: [
		sveltekit()
	],
	ssr: {
		noExternal: ['lucide', 'bits-ui', 'svelte-sonner']
	},
	server: {
		host: true,
		proxy: {
			'/api': 'http://localhost:8000',
			'/docs': 'http://localhost:8000',
			'/redoc': 'http://localhost:8000',
			'/openapi.json': 'http://localhost:8000',
		},
	},
	css: {
		preprocessorOptions: {
			scss: {
				silenceDeprecations: [
					'import',
					'mixed-decls',
					'color-functions',
					'global-builtin',
				],
			},
		},
	},
});
