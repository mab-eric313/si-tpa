<script>
	import Header from './Header.svelte';

	let { children } = $props();
</script>

<div class="app">
	<Header />
	<main>
		{@render children()}
	</main>
</div>

<style>
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: "Inter", sans-serif;
  }

  :root {
    --warna-hijau-gelap: #1a4a20;
    --warna-hijau-terang: #2b7a33;
    --warna-teks-hijau: #268041;
    --warna-abu-tua: #24292e;
    --warna-menu-aktif: #9ea39e;
  }
</style>
