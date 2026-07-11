<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let daftarKelas = $state([]);

	onMount(async () => {
		try {
			const response = await fetch(`${PUBLIC_API_BASE_URL}/kelas/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);
			daftarKelas = await response.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	function handleAdd() {
		goto(`/admin/kelola-kelas/add`);
	}

	function handleEdit(id) {
		goto(`/admin/kelola-kelas/edit/${id}`);
	}

	async function handleDelete(id) {
		const konfirmasi = confirm("Yakin ingin menghapus data ini?");
		if (!konfirmasi) return;

		try {
			const res = await fetch(
				`${PUBLIC_API_BASE_URL}/kelas/${id}`, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`${res.statusText}`);

			daftarKelas = daftarKelas.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorMessage = error.message;
		}
	}

	function formatTime(time) {
		if (!time) return "-";

		return time.substring(0, 5);
	}

</script>

<section class="sidebar-gap">
	<h1 class="py-5">Kelola Kelas</h1>

	<div class="container border rounded">
		<div class="d-flex justify-content-end my-3">
			<button 
				class="btn btn-primary"
				onclick={handleAdd}>
				Tambah Data
			</button>
		</div>
		{#if errorMessage}
			<p class="text-danger">{errorMessage}</p>
		{:else if daftarKelas.length === 0}
			<p>Sedang memuat data...</p>
		{:else}
			<table class="table table-bordered text-center">
				<thead>
				<tr>
					<th>No</th>
					<th>Nama</th>
					<th>Hari</th>
					<th>Waktu</th>
					<th class="text-center">Action</th>
				</tr>
				</thead>
				<tbody>
					{#each daftarKelas as kelas, i}
					<tr>
						<td>{i + 1}</td>
						<td>{kelas.nama}</td>
						<td>{kelas.start_day}-{kelas.end_day}</td>
						<td>{formatTime(kelas.start_time)}-{formatTime(kelas.end_time)}</td>
						<td class="text-center">
							<button
								class="btn btn-sm btn-primary" 
								aria-label="Edit"
								onclick={() => handleEdit(kelas.id)}>
								<i class="bi bi-pencil-fill"></i>
								Edit
							</button>
							<button
								class="btn btn-sm btn-danger"
								aria-label="Delete"
								onclick={() => handleDelete(kelas.id)}>
								<i class="bi bi-trash-fill"></i>
								Hapus
							</button>
						</td>
					</tr>
					{/each}
				</tbody>
			</table>
		{/if}
	</div>
</section>

<style>
	.sidebar-gap {
		padding-left: 240px; 
		position: relative; 
		min-height: 100vh;
	}

	th, td, button{
		font-size: 15px;
	}
</style>
