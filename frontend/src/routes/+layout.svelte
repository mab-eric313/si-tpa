<script>
	import 'bootstrap/dist/css/bootstrap.min.css';

	import { browser } from '$app/environment';
	if (browser)
		import('bootstrap/dist/js/bootstrap.bundle.min.js');

	let { children } = $props();
</script>

{@render children()}
