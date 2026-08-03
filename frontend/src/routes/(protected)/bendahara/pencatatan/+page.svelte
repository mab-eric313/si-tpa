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
		goto(`/bendahara/pencatatan/add`);
	}

	function handleEdit(id) {
		goto(`/bendahara/pencatatan/edit/${id}`);
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
<section class="content-section">
	<h1 class="mb-4">Data Pencatatan Finansial</h1>
	<div class="table-container border rounded bg-white">
		<div class="filter-section p-3 border-bottom">
			<div class="row g-3">
				<label class="form-label fw-bold" for="select-kategori">
					Pilih Kategori
				</label>
			</div>
			<div class="d-flex justify-content-between">
				<div class="col pe-2">
					<select 
						id="select-kategori"
						class="form-select" 
						bind:value={selectKategori}
						aria-label="Pilih kategori">
						<option value="semua">Semua</option>
						<option value="Pemasukan">Pemasukan</option>
						<option value="Pengeluaran">Pengeluaran</option>
					</select>
				</div>
				<div class="">
					<button 
						class="btn btn-primary"
						onclick={handleAdd}>
						Tambah Data
					</button>
				</div>
			</div>
		</div>
		{#if errorMessage}
			<div class="d-flex p-4 justify-content-center">
				<div class="card border-danger mb-3">
					<div class="card-header bg-danger text-white">
						<span>{errorMessage}</span>
					</div>
				</div>
			</div>
		{:else if daftarTransaksi.length === 0}
			<div class="d-flex justify-content-center p-4">
				<div class="spinner-border text-primary" role="status">
					<span class="visually-hidden">Loading...</span>
				</div>
			</div>
		{:else}
			<div class="table-responsive">
				<table class="table table-bordered text-center">
					<thead class="table-light">
					<tr>
						<th>No</th>
						<th>Nama</th>
						<th>Tanggal</th>
						<th>Kategori</th>
						<!-- TODO: Catatan must be in detail -->
						<!-- <th>Catatan</th> -->
						<th>Nominal</th>
						<th>Action</th>
					</tr>
					</thead>
					<tbody>
						{#each filteredTransaksi as transaksi, i}
						<tr>
							<td>{i+1}</td>
							<td class="fw-semibold">{transaksi.nama}</td>
							<td>{transaksi.tanggal}</td>
							<td>
								{#if transaksi.kategori === "Pemasukan"}
									<span class="badge bg-success">Pemasukan</span>
								{:else if transaksi.kategori === "Pengeluaran"}
									<span class="badge bg-danger">Pengeluaran</span>
								{:else}
									<span class="badge bg-secondary">-</span>
								{/if}
							</td>
							<!-- <td>{transaksi.note}</td> -->
							<td>{formatRupiah(transaksi.nominal)}</td>
							<td>
								<div class="btn-group-vertical btn-group-sm d-md-none">
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
								</div>
								<div class="btn-group d-none d-md-inline-flex">
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
								</div>
							</td>
						</tr>
						{/each}
					</tbody>
				</table>
			</div>
		{/if}
	</div>
</section>
{:else}
    <div style="display: flex; justify-content: center; align-items: center; height: 100vh;">
        <p>Memverifikasi akses...</p>
    </div>
{/if}

<style>
	.content-section {
		padding: 0;
	}

	h1 {
		font-size: 1.75rem;
		font-weight: 700;
		color: #1a3a2e;
	}

	.table-container {
		box-shadow: 0 2px 8px rgba(0,0,0,0.08);
	}

	.filter-section {
		background-color: #f8f9fa;
	}

	.table-responsive {
		overflow-x: auto;
		-webkit-overflow-scrolling: touch;
	}

	table {
		min-width: 500px;
	}

	th, td {
		font-size: 14px;
		padding: 12px 8px;
		vertical-align: middle;
	}

	th {
		font-weight: 600;
		text-transform: uppercase;
		font-size: 13px;
		letter-spacing: 0.5px;
	}

	.btn-group-vertical {
		width: 100%;
	}

	.btn-group-vertical .btn {
		width: 100%;
	}

	@media (max-width: 768px) {
		h1 {
			font-size: 1.5rem;
			text-align: center;
		}

		th, td {
			font-size: 13px;
			padding: 10px 6px;
		}

		.table-responsive {
			border-radius: 0 0 8px 8px;
		}
	}
</style>

