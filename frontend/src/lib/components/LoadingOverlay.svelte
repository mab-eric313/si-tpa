<script>
    /**
     * @typedef {Object} Props
     * @property {boolean} visible - Tampilkan/sembunyikan loading
     * @property {string} message - Teks yang ditampilkan
     * @property {'primary'|'secondary'|'success'|'danger'|'warning'|'info'} color - Warna spinner
     */
    let visible = $props();
    let color = $state('primary');
</script>

{#if visible}
	<div class="loading-overlay">
		<div class="loading-box">
			<div class="spinner-border text-primary my-2" role="status">
				<span class="visually-hidden">Loading...</span>
			</div>
			<p class="mt-2 mb0 text-muted small">Sedang memuat data...</p>
		</div>
	</div>
{/if}

<style>
	.loading-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0,0,0,.4);
		display: flex;
		justify-content: center;
		align-items: center;
		z-index: 9999;
	}

	.loading-box {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
		background-color: white;
		padding: 24px 32px;
		border-radius: 12px;
		box-shadow: 0 10px 25px rgba(0, 0, 0, 0.25); 
	}
</style>
