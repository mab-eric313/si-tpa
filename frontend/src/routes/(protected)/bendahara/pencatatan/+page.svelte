<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	import { formatRupiah } from '$lib/utils';
	import { authState } from '$lib/authStore.svelte.js';
	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	$effect(() => {
        if (!authState.isLoggedIn || 
			(authState.role !== 'Admin' && authState.role !== 'Bendahara')) {
            goto('/login');
        }
    });

	let errorMessage = $state("");
	let daftarTransaksi = $state([]);
	let selectKategori = $state("semua");

	onMount(async () => {
		try {
			const res = await fetch(`${PUBLIC_API_BASE_URL}/trg-transaksi/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);
			daftarTransaksi = await res.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	let filteredTransaksi = $derived(
		selectKategori === "semua"
			? daftarTransaksi
			: daftarTransaksi.filter(transaksi => transaksi.kategori === selectKategori)
	);

	function handleAdd() {
		goto(`transaksi/add`);
	}

	function handleEdit(id) {
		goto(`transaksi/edit/${id}`);
	}

	async function handleDelete(id) {
		const konfirmasi = confirm("Yakin ingin menghapus data ini?");
		if (!konfirmasi) return;

		try {
			const res = await fetch(
				`${PUBLIC_API_BASE_URL}/trg-transaksi/${id}`, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`${res.statusText}`);

			daftarTransaksi = daftarTransaksi.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorMessage = error.message;
		}
	}
</script>

{#if authState.isLoggedIn && (authState.role === 'Admin' || authState.role === 'Bendahara')}
<section class="sidebar-gap">
	<h1 class="mt-5">Data Pencatatan Finansial TPA</h1>
	<p class="mb-5">Kelola seluruh pencatatan transaksi pemasukan dan pengeluaran</p>

	<div class="container border rounded">
		<div class="d-flex justify-content-between">
			<div class="ms-2 my-3 select-width">
				<span class="mb-2">Pilih Kategori</span>
				<select 
					class="form-select text-center" 
					bind:value={selectKategori}
					aria-label="Pilih kategori">
					<option value="semua">Semua</option>
					<option value="Pemasukan">Pemasukan</option>
					<option value="Pengeluaran">Pengeluaran</option>
				</select>
			</div>
			<div class="me-2 mt-5">
				<button 
					class="btn btn-primary"
					onclick={handleAdd}>
					Tambah Data
				</button>
			</div>
		</div>
		{#if errorMessage}
			<p class="text-danger">{errorMessage}</p>
		{:else if daftarTransaksi.length === 0}
			<p>Sedang memuat data...</p>
		{:else}
			<table class="table table-bordered text-center">
				<thead>
				<tr>
					<th>No</th>
					<th>Nama</th>
					<th>Tanggal</th>
					<th>Kategori</th>
					<th>Catatan</th>
					<th>Nominal</th>
					<th class="text-center">Action</th>
				</tr>
				</thead>
				<tbody>
					{#each filteredTransaksi as transaksi, i}
					<tr>
						<td>{i+1}</td>
						<td>{transaksi.nama}</td>
						<td>{transaksi.tanggal}</td>
						<td>{transaksi.kategori}</td>
						<td>{transaksi.note}</td>
						<td>{formatRupiah(transaksi.nominal)}</td>
						<td class="text-center">
							<button
								class="btn btn-sm btn-primary" 
								aria-label="Edit"
								onclick={() => handleEdit(transaksi.id)}>
								<i class="bi bi-pencil-fill"></i>
								Edit
							</button>
							<button
								class="btn btn-sm btn-danger"
								aria-label="Delete"
								onclick={() => handleDelete(transaksi.id)}>
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
{:else}
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <p>Memverifikasi akses...</p>
    </div>
{/if}

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

