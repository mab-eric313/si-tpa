<script>
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let selectedTabelPenilaian = $state("jilid");
	const endpointMap = {
		jilid: `${PUBLIC_API_BASE_URL}/penilaian-jilid/`,
		surat: `${PUBLIC_API_BASE_URL}/penilaian-surat/`,
		doa: `${PUBLIC_API_BASE_URL}/penilaian-doa/`,
	}

	let daftarPenilaian = $state([]);
	let errorMessage = $state("");

	/*
	onMount(async () => {
		try {
			const res = await fetch(endpointMap[selectedTabelPenilaian], {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			daftarPenilaian = await res.json();
		} catch(error) {
			console.error("Error fetching data: ", error);
			errorMessage = error.message;
		}
	});
	*/

	const kolomMap = {
		jilid: [
			{ key: "materi_bacaan", label: "Materi Bacaan" },
			{ key: "nilai_tajwid", label: "Nilai Tajwid" },
			{ key: "nilai_makhraj", label: "Nilai Makhraj" },
			{ key: "nilai_kelancaran", label: "Nilai Kelancaran" },
		],
		surat: [
			{ key: "nama_surat", label: "Nama Surat" },
			{ key: "kelancaran", label: "Kelancaran" },
			{ key: "ketepatan_bacaan", label: "Ketepatan Bacaan" },
		],
		doa: [
			{ key: "nama_doa", label: "Nama Doa" },
			{ key: "nilai", label: "Nilai" },
		],
	};
	let kolomAktif = $derived(kolomMap[selectedTabelPenilaian]);

	$effect(() => {
		const endpoint = endpointMap[selectedTabelPenilaian];
		fetch(endpoint, {
			method: "GET",
			headers: { "Content-Type": "application/json" },
			credentials: "include",
		})
			.then(res => {
				if (!res.ok) throw new Error(`Error: ${res.statusText}`);
				return res.json();
			})
			.then(data => daftarPenilaian = data)
			.catch(err => errorMessage = err.message);
	});

	function handleAdd() {
		goto(`/pengajar/penilaian/add`);
	}

	function handleEdit(id, siswa_id) {
		goto(`/pengajar/penilaian/edit/${id}?penilaian=${selectedTabelPenilaian}&siswa_id=${siswa_id}`);
	}

	async function handleDelete(id) {
		const konfirmasi = confirm("Yakin ingin menghapus data ini?");
		if (!konfirmasi) return;

		try {
			const endpoint = `${endpointMap[selectedTabelPenilaian]}${id}`;
			const res = await fetch(endpoint, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			})
			if (!res.ok) throw new Error(`Error: ${res.statusText}`);

			daftarPenilaian = daftarPenilaian.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorMessage = error.message;
		}
	}

	// TODO: Remove this unused code
	let selectedKelasId = $state("");
	let filteredSiswa = $derived(
		selectedKelasId === ""
			? daftarSiswa
			: daftarSiswa.filter(siswa => siswa.kelas_id === Number(selectedKelasId))
	)
</script>

<section class="content-section">
	<div class="my-4">
		<h1>Kelola Data Penilaian</h1>
	</div>

	<div class="table-container border rounded bg-white">
		<div class="filter-section p-3 border-bottom">
			<div class="row g-3">
				<label class="form-label fw-bold" for="select-penilaian">
					Pilih Penilaian
				</label>
				<div class="col-md-6">
					<select 
						id="select-penilaian"
						class="form-select" 
						bind:value={selectedTabelPenilaian}
						aria-label="Pilih tabel penilian">
						<option value="jilid">Bacaan Jilid</option>
						<option value="surat">Hafalan Surat</option>
						<option value="doa">Hafalan Doa</option>
					</select>
				</div>
				<div class="d-flex align-items-center col-md-6">
					<button 
						class="btn btn-primary"
						onclick={handleAdd}>
						Tambah Data
					</button>
				</div>
			</div>
		</div>

		<div>
			{#if errorMessage}
				<div class="d-flex p-4 justify-content-center">
					<div class="card border-danger mb-3">
						<div class="card-header bg-danger text-white">
							<span>{errorMessage}</span>
						</div>
					</div>
				</div>
			{:else if daftarPenilaian.length === 0}
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
								{#each kolomAktif as kolom}
									<th>{kolom.label}</th>
								{/each}
								<th>Status</th>
								<!-- TODO: Move to detail button -->
								<!-- <th>Note</th> -->
								<!-- TODO: Tanggal Setor must be a filter -->
								<!-- <th>Tanggal Setor</th> -->
								<th>Aksi</th>
							</tr>
						</thead>
						<tbody>
							{#each daftarPenilaian as item, i (item.id)}
								<tr>
									<td>{i + 1}</td>
									<td class="fw-semibold">{item.siswa.nama}</td>
									{#each kolomAktif as kolom}
										<td>{item[kolom.key]}</td>
									{/each}
									<td>
										{#if item.lulus_ulang === "Lulus"}
											<span class="badge bg-success">Lulus</span>
										{:else}
											<span class="badge bg-danger">Ulang</span>
										{/if}
									</td>
									<!-- <td>{item.note}</td> -->
									<!-- <td>{item.tanggal_setor}</td> -->
									<td>
										<div class="btn-group-vertical btn-group-sm d-md-none">
											<button 
												class="btn btn-sm btn-primary" 
												onclick={() => handleEdit(item.id, item.siswa_id)}>
												<i class='bi bi-pencil-fill'></i>
												Edit
											</button>
											<button 
												class="btn btn-sm btn-danger" 
												onclick={() => handleDelete(item.id)}>
												<i class='bi bi-trash-fill'></i>
												Hapus
											</button>
										</div>
										<div class="btn-group d-none d-md-inline-flex">
											<button 
												class="btn btn-sm btn-primary" 
												onclick={() => handleEdit(item.id, item.siswa_id)}>
												<i class='bi bi-pencil-fill'></i>
												Edit
											</button>
											<button 
												class="btn btn-sm btn-danger" 
												onclick={() => handleDelete(item.id)}>
												<i class='bi bi-trash-fill'></i>
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
	</div>
</section>

<style>
	tr:hover {
		background-color: #f1f5f9;
	}

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
