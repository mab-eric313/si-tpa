<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";
	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let daftarCalonSiswa = $state([]);
	let daftarKelas = $state([]);
	let daftarSiswa = $state([]);
	let daftarWali = $state([]);

	onMount(async () => {
		try {
			const [resSiswa, resKelas, resWali] = await Promise.all([
				fetch(`${PUBLIC_API_BASE_URL}/siswa/`, { credentials: "include" }),
				fetch(`${PUBLIC_API_BASE_URL}/kelas/`, { credentials: "include" }),
				fetch(`${PUBLIC_API_BASE_URL}/wali/`, { credentials: "include" }),
			]);
			if (!resSiswa.ok) throw new Error(`Error: ${resSiswa.statusText}`);
			if (!resKelas.ok) throw new Error(`Error: ${resKelas.statusText}`);
			if (!resWali.ok) throw new Error(`Error: ${resWali.statusText}`);

			daftarSiswa = await resSiswa.json();
			daftarKelas = await resKelas.json();
			daftarWali = await resWali.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	function getNamaKelas(id) {
		return daftarKelas.find(k => k.id == id)?.nama ?? "-";
	}

	function getNamaWali(id) {
		return daftarWali.find(k => k.id == id)?.nama ?? "-";
	}

	function getAlamatWali(id) {
		return daftarWali.find(k => k.id == id)?.alamat ?? "-";
	}

	function getNoHpWali(id) {
		return daftarWali.find(k => k.id == id)?.no_hp ?? "-";
	}

	function handleEdit(id) {
		goto(`/admin/kelola-siswa/edit/${id}`);
	}

	async function handleDelete(id) {
		const messageConfirm = 
			"Sistem tidak akan menghapus data ini, sebaliknya sistem " +
			"akan mengubah statusnya menjadi \"Tidak Aktif\". Yakin ingin " +
			"menonaktifkan data ini?";
		const konfirmasi = confirm(messageConfirm);
		if (!konfirmasi) return;

		try {
			const res = await fetch(
				`${PUBLIC_API_BASE_URL}/siswa/${id}`, {
				method: "PATCH",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify({ "status": "Tidak Aktif" }),
			});
			if (!res.ok) throw new Error(`${res.statusText}`);

			const siswaIndex = daftarSiswa.findIndex(item => item.id === id);
			if (siswaIndex !== -1) {
				daftarSiswa[siswaIndex].status = "Tidak Aktif";
				daftarSiswa = [...daftarSiswa]; 
			}
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorMessage = error.message;
		}
	}

	let selectedKelasId = $state("");
	let selectedStatus = $state("");

	let filteredSiswa = $derived(
		daftarSiswa.filter(siswa => {
			const matchKelas = selectedKelasId === "" || siswa.kelas_id === Number(selectedKelasId);
			const matchStatus = selectedStatus === "" || siswa.status === selectedStatus;
			return matchKelas && matchStatus;
		})
	);
</script>

<section class="content-section">
	<h1 class="mb-4">Kelola Data Siswa</h1>

	<div class="table-container border rounded bg-white">
		<div class="filter-section p-3 border-bottom">
			<div class="row g-3">
				<div class="col-md-6">
					<label class="form-label fw-bold" for="select-kelas">
						Pilih Kelas
					</label>
					<select 
						id="select-kelas"
						class="form-select" 
						bind:value={selectedKelasId}
						aria-label="Pilih kelas">
						<option value="">Semua Kelas</option>
						{#each daftarKelas as kelas}
							<option value={String(kelas.id)}>{kelas.nama}</option>
						{/each}
					</select>
				</div>
				<div class="col-md-6">
					<label class="form-label fw-bold" for="select-status">
						Pilih Status
					</label>
					<select 
						id="select-status"
						class="form-select" 
						bind:value={selectedStatus}
						aria-label="Pilih status">
						<option value="">Semua Status</option>
						<option value="Aktif">Aktif</option>
						<option value="Tidak Aktif">Tidak Aktif</option>
					</select>
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
		{:else if daftarSiswa.length === 0}
			<div class="d-flex justify-content-center p-4">
				<div class="spinner-border text-primary" role="status">
					<span class="visually-hidden">Loading...</span>
				</div>
			</div>
		{:else}
			<div class="table-responsive">
				<table class="table table-bordered table-hover mb-0">
					<thead class="table-light">
						<tr>
							<th>No</th>
							<th>Nama Siswa</th>
							<th>Tanggal Lahir</th>
							<!-- <th>Alamat Siswa</th> -->
							<th>Nama Wali</th>
							<!-- <th>Alamat Wali</th> -->
							<th>No HP Wali</th>
							<th>Kelas</th>
							<th>Status</th>
							<th class="text-center">Action</th>
						</tr>
					</thead>
					<tbody>
						{#each filteredSiswa as siswa, i}
							<tr>
								<td>{i + 1}</td>
								<td class="fw-semibold">{siswa.nama}</td>
								<td>{siswa.tanggal_lahir}</td>
								<!-- <td>{siswa.alamat ?? '-'}</td> -->
								<td>{getNamaWali(siswa.wali_id)}</td>
								<!-- <td>{getAlamatWali(siswa.wali_id)}</td> -->
								<td>{getNoHpWali(siswa.wali_id)}</td>
								<td>{getNamaKelas(siswa.kelas_id)}</td>
								<td class="text-center">
									{#if siswa.status === "Aktif"}
										<span class="badge bg-success">Aktif</span>
									{:else}
										<span class="badge bg-secondary">Tidak Aktif</span>
									{/if}
								</td>
								<td class="text-center">
									<div class="btn-group-vertical btn-group-sm d-md-none">
										<button
											class="btn btn-primary" 
											onclick={() => handleEdit(siswa.id)}>
											<i class="bi bi-pencil-fill me-1"></i>
											Edit
										</button>
										{#if siswa.status === "Aktif"}
											<button
												class="btn btn-danger"
												onclick={() => handleDelete(siswa.id)}>
												<i class="bi bi-trash-fill me-1"></i> Hapus
											</button>
										{/if}
									</div>
									<div class="btn-group d-none d-md-inline-flex">
										<button
											class="btn btn-sm btn-primary"
											onclick={() => handleEdit(siswa.id)}>
											<i class="bi bi-pencil-fill"></i>
											Edit
										</button>
										{#if siswa.status === "Aktif"}
											<button
												class="btn btn-sm btn-danger"
												onclick={() => handleDelete(siswa.id)}>
												<i class="bi bi-trash-fill"></i> Hapus
											</button>
										{/if}
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
