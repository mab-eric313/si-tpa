<script>
	import { browser } from '$app/environment';
	import 'bootstrap/dist/css/bootstrap.min.css';
	if (browser)
		import('bootstrap/dist/js/bootstrap.bundle.min.js');

	let { children } = $props();
</script>

{@render children()}
