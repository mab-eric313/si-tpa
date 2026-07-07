<script>
	import favicon from '$lib/assets/favicon.svg';
	import Header from './Header.svelte';
	import './layout.css';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="app">
	<Header />
	
	<main>
		{@render children()}
	</main>
</div>

<style>
	.app {
		display: flex;
		flex-direction: row;
	}

	main {
		flex: 1;
		padding: 20px;
	}
</style>
