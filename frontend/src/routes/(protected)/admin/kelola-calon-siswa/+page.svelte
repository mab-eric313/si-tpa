<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let daftarCalonSiswa = $state([]);
	let daftarKelas = $state([]);
	let daftarSiswa = $state([]);

	onMount(async () => {
		try {
			const [resCalonSiswa, resKelas] = await Promise.all([
				fetch(`${PUBLIC_API_BASE_URL}/pendaftaran-siswa/`, { 
					credentials: "include",
				}),
				fetch(`${PUBLIC_API_BASE_URL}/kelas/`, { 
					credentials: "include",
				}),
			]);
			if (!resCalonSiswa.ok) throw new Error(`Error: ${resCalonSiswa.statusText}`);
			if (!resKelas.ok) throw new Error(`Error: ${resKelas.statusText}`);

			daftarCalonSiswa = await resCalonSiswa.json();
			daftarKelas = await resKelas.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	function getNamaKelas(kelasId) {
		return daftarKelas.find(k => k.id == kelasId)?.nama ?? "-";
	};

	async function handleAdd(id) {
		const konfirmasi = confirm("Yakin ingin menambahkan calon siswa ini menjadi siswa baru?");
		if (!konfirmasi) return;

		try {
			const resSiswa = await fetch(
				`${PUBLIC_API_BASE_URL}/siswa/${id}`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include"
			});
			if (!resSiswa.ok) {
				const errorData = await resSiswa.json().catch(() => null);
				throw new Error(errorData?.detail || resSiswa.statusText);
			}

			const newSiswa = await resSiswa.json();
			daftarSiswa = [...daftarSiswa, newSiswa];
			const calon = daftarCalonSiswa.find(item => item.id === id);
			if (calon) calon.status = "Diterima";
			daftarCalonSiswa = daftarCalonSiswa.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error adding data: ", error);
			errorMessage = error.message;
		}
	}

	/* TODO: Add edit page for pendaftaran siswa
	function handleEdit(id) {
		goto(`/admin/calon-siswa/edit/${id}`);
	}
	*/

	async function handleDelete(id) {
		const konfirmasi = confirm("Yakin ingin menghapus data ini?");
		if (!konfirmasi) return;

		try {
			const res = await fetch(
				`${PUBLIC_API_BASE_URL}/pendaftaran-siswa/${id}`, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`${res.statusText}`);

			daftarCalonSiswa = daftarCalonSiswa.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="content-section">
	<h1 class="mb-4">Kelola Data Calon Siswa</h1>

	<div class="table-container border rounded bg-white">
		<!--
		<div class="filter-section p-3 border-bottom">
			<div class="row g-3">
			</div>
		</div>
		-->
		{#if errorMessage}
			<div class="d-flex p-4 justify-content-center">
				<div class="card border-danger mb-3">
					<div class="card-header bg-danger text-white">
						<span>{errorMessage}</span>
					</div>
				</div>
			</div>
		{:else if daftarCalonSiswa.length === 0}
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
						<th class="text-center">No</th>
						<th class="text-center">Nama Calon Siswa</th>
						<th class="text-center">Tanggal lahir</th>
						<!-- <th>Alamat Calon Siswa</th> -->
						<th class="text-center">Nama Wali</th>
						<!-- <th>Alamat Wali</th> -->
						<!-- <th>No Hp Wali</th> -->
						<th class="text-center">Kelas</th>
						<th class="text-center">Foto</th>
						<th class="text-center">Action</th>
					</tr>
					</thead>
					<tbody>
						{#each daftarCalonSiswa.filter(
							calon => calon.status === "Pending"
						) as calonSiswa, i}
							<tr>
								<td class="text-center">{i + 1}</td>
								<td class="text-center fw-semibold">
									{calonSiswa.nama_siswa}
								</td>
								<td class="text-center">
									{calonSiswa.tanggal_lahir_siswa}
								</td>
								<!-- <td>{calonSiswa.alamat_siswa ?? '-'}</td> -->
								<td class="text-center">{calonSiswa.nama_wali}</td>
								<!-- <td>{calonSiswa.alamat_wali ?? '-'}</td> -->
								<!-- <td>{calonSiswa.no_hp_wali ?? '-'}</td> -->
								<td class="text-center">
									{getNamaKelas(calonSiswa.kelas_id)}
								</td>
								<th class="text-center">
									<div class="dropdown">
										<button
											type="button"
											class="btn btn-sm btn-primary dropdown-toggle"
											data-bs-toggle="dropdown" aria-expanded="false"
											aria-label="Lihat Foto">
											Lihat
										</button>
										<ul class="dropdown-menu">
											<li>
												<a class="dropdown-item" 
												   href={calonSiswa.foto_kk}
												   target="_blank" 
												   rel="noopener noreferrer">
													Foto Kartu Keluarga
												</a>
											</li>
											<li>
												<a class="dropdown-item" 
												   href={calonSiswa.foto_ak}
												   target="_blank" 
												   rel="noopener noreferrer">
													Foto Akta Kelahiran
												</a>
											</li>
											<li>
												<a class="dropdown-item" 
												   href={calonSiswa.foto_pas}
												   target="_blank" 
												   rel="noopener noreferrer">
													Pas Foto
												</a>
											</li>
										</ul>
									</div>
								</th>
								<td class="text-center">
									<div class="btn-group-vertical btn-group-sm d-md-none">
										<button
											class="btn btn-sm btn-primary" 
											aria-label="Tambah"
											onclick={() => handleAdd(calonSiswa.id)}>
											<i class="bi bi-plus-lg" 
												style="font-size: 15px;">
											</i>
											Tambah
										</button>
										<!--
										<button
											class="btn btn-sm btn-primary" 
											aria-label="Edit"
											onclick={() => handleEdit(calonSiswa.id)}>
											<i class="bi bi-pencil-fill"></i>
											Edit
										</button>
										-->
										<button
											class="btn btn-sm btn-danger"
											aria-label="Delete"
											onclick={() => handleDelete(calonSiswa.id)}>
											<i class="bi bi-trash-fill"></i>
											Hapus
										</button>
									</div>
									<div class="btn-group d-none d-md-inline-flex">
										<button
											class="btn btn-sm btn-primary" 
											aria-label="Tambah"
											onclick={() => handleAdd(calonSiswa.id)}>
											<i class="bi bi-plus-lg" 
												style="font-size: 15px;">
											</i>
											Tambah
										</button>
										<!--
										<button
											class="btn btn-sm btn-primary" 
											aria-label="Edit"
											onclick={() => handleEdit(calonSiswa.id)}>
											<i class="bi bi-pencil-fill"></i>
											Edit
										</button>
										-->
										<button
											class="btn btn-sm btn-danger"
											aria-label="Delete"
											onclick={() => handleDelete(calonSiswa.id)}>
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

	/*
	.filter-section {
		background-color: #f8f9fa;
	}
	*/

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

