<script>
	import favicon from '$lib/assets/favicon.svg';
	import './layout.css';
	import Sidebar from '../Sidebar.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<div class="app-layout">
	<Sidebar />
	<main class="main-content">
		{@render children()}
	</main>
</div>

<style>
	.app-layout {
		display: grid;
		grid-template-columns: 260px 1fr;
		height: 100dvh;
		min-height: 100vh;
		background-color: #f8f9fa;
	}

	.main-content {
		padding: 24px 32px;
		overflow-y: auto;
		background-color: #f4f6f8;
	}
</style>
