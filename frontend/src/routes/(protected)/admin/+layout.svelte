<script>
	import favicon from '$lib/assets/favicon.svg';
	import './layout.css';
	import Sidebar from '../Sidebar.svelte';

	let { children } = $props();
</script>

<svelte:head>
	<link rel="icon" href={favicon} />
</svelte:head>

<!-- <div class="app"> -->
<!-- 	<Header /> -->
<!---->
<!-- 	<main> -->
		<!-- {@render children()} -->
<!-- 	</main> -->
<!-- </div> -->

<div class="app-layout">
	<Sidebar />
	<main class="main-content">
		{@render children()}
	</main>
</div>

<style>
/*
	.app {
		display: flex;
		flex-direction: row;
	}

	main {
		flex: 1;
		padding: 20px;
	}
*/	
/*
	:global(body) {
		height: 100%;
		margin: 0;
		overflow: hidden;
	}
*/

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

	@media (max-width: 768px) {
		.app-layout {
			grid-template-columns: 1fr;
		}

		.main-content {
			padding: 80px 15px 24px 15px;
		}
	}
</style>
