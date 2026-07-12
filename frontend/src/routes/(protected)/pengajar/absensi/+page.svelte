<script>
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let selectedTabelPenilaian = $state("jilid");

	let errorMessage = $state("");

	let selectedKehadiran = $state([]);
	let valueInputCatatan = $state({});

	$inspect(valueInputCatatan);

	let daftarSiswa = $state([]);
	let daftarKelas = $state([]);

	onMount(async () => {
		try {
			const [resSiswa, resKelas] = await Promise.all([
				fetch(`${PUBLIC_API_BASE_URL}/siswa/`, { 
					credentials: "include",
				}),
				fetch(`${PUBLIC_API_BASE_URL}/kelas/`, { 
					credentials: "include",
				}),
			]);
			if (!resSiswa.ok) throw new Error(`Error: ${resSiswa.statusText}`);
			if (!resKelas.ok) throw new Error(`Error: ${resKelas.statusText}`);

			daftarSiswa = await resSiswa.json();
			daftarKelas = await resKelas.json();

			selectedKehadiran = daftarSiswa.map(() => "Hadir");
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	let selectedKelasId = $state("");
	let filteredSiswa = $derived(
		daftarSiswa.filter(siswa => {
			const matchKelas = selectedKelasId === "" || siswa.kelas_id === Number(selectedKelasId);
			// TODO: check if siswa is active
			// const matchStatus = selectedStatus === "" || siswa.status === selectedStatus;
			// return matchKelas && matchStatus;
			return matchKelas;
		})
	);

	function handleAdd() {
		goto(`siswa/add`);
	}

	function handleEdit(id, siswa_id) {
		goto(`siswa/edit/${id}?penilaian=${selectedTabelPenilaian}&siswa_id=${siswa_id}`);
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

</script>

<section class="sidebar-gap">
	<h1 class="my-4">Absensi</h1>

	<div class="container border rounded">

		<div class="d-flex justify-content-between">
			<div class="ms-2 my-3">
				<span class="mb-2">Pilih Kelas</span>
				<!-- TODO: Change this and take the data from kelas table -->
				<select 
					class="form-select text-center" 
					bind:value={selectedKelasId}
					aria-label="Default select example">
					<option value="">Semua Kelas</option>
					{#each daftarKelas as kelas}
						<option value={String(kelas.id)}>{kelas.nama}</option>
					{/each}
				</select>
			</div>
			<!--
			<div class="me-2 my-3">
				<span class="mb-2">Pilih Status</span>
				<select 
					class="form-select text-center" 
					bind:value={selectedStatus}
					aria-label="Pilih tabel penilian">
					<option value="">Semua Status</option>
					<option value="Aktif">Aktif</option>
					<option value="Tidak Aktif">Tidak Aktif</option>
				</select>
			</div>
			-->
		</div>

		<div>
			{#if errorMessage}
				<p class="text-danger">{errorMessage}</p>
			{:else if daftarSiswa.length === 0}
				<p>Sedang memuat data atau tidak ada data...</p>
			{:else}
				<table class="table table-bordered text-center">
					<thead>
						<tr>
							<th>No</th>
							<th>Nama</th>
							<th>Kehadiran</th>
							<th>Catatan</th>
						</tr>
					</thead>
					<tbody>
						{#each filteredSiswa as item, i (item.id)}
							<tr>
								<td>{i + 1}</td>
								<td>{item.nama}</td>
								<td class="d-flex justify-content-center">

									<!-- Hadir -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-green">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputHadir-" + i}
											name={"kehadiran-" + i}
											value="Hadir"
											bind:group={selectedKehadiran[i]}
											style="font-size: 25px;">
										<label 
											for={"inputHadir-" + i}
											class="form-check-label">
											Hadir
										</label>
									</div>

									<!-- Izin -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-yellowgreen">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputIzin-" + i}
											name={"kehadiran-" + i}
											value="Izin"
											bind:group={selectedKehadiran[i]}
											style="font-size: 25px;">
										<label 
											for={"inputIzin-" + i}
											class="form-check-label">
											Izin
										</label>
									</div>

									<!-- Sakit -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-yellow">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputSakit-" + i}
											name={"kehadiran-" + i}
											value="Sakit"
											bind:group={selectedKehadiran[i]}
											style="font-size: 25px;">
										<label 
											for={"inputSakit-" + i}
											class="form-check-label">
											Sakit
										</label>
									</div>

									<!-- Alpha -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-red">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputAlpha-" + i}
											name={"kehadiran-" + i}
											value="Alpha"
											bind:group={selectedKehadiran[i]}
											style="font-size: 25px;">
										<label 
											for={"inputAlpha-" + i}
											class="form-check-label">
											Alpha
										</label>
									</div>
								</td>
								<td>
									{#if selectedKehadiran[i] == "Hadir"}
										<input 
											type="text" 
											class="form-control text-center" 
											placeholder="Tambahkan catatan"
											value=""
											disabled>
									{:else}
										<input 
											type="text" 
											class="form-control text-center" 
											placeholder="Tambahkan catatan"
											bind:value={valueInputCatatan[item.id]}>
									{/if}
								</td>
							</tr>
						{/each}
					</tbody>
				</table>
			{/if}
		</div>
	</div>
</section>

<style>
	.sidebar-gap {
		padding-left: 240px; 
		position: relative; 
		min-height: 100vh;
	}

	tr:hover {
		background-color: #f1f5f9;
	}

	.select-width {
		width: 20%;
	}

	.fs-small {
		font-size: 15px;
	}

	.bg-radio-green .form-check-input:checked {
		background-color: green;
		border-color: green;
	}

	.bg-radio-yellowgreen .form-check-input:checked {
		background-color: yellowgreen;
		border-color: yellowgreen;
	}

	.bg-radio-yellow .form-check-input:checked {
		background-color: yellow;
		border-color: yellow;
	}

	.bg-radio-red .form-check-input:checked {
		background-color: red;
		border-color: red;
	}
</style>
