<script>
	import { onMount } from 'svelte';
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let editStatus = $state(false);
	let isLoading = $state(false);

	let selectedKehadiran = $state({});

	let valueInputCatatan = $state({});
	function getLocalDate() {
		const now = new Date();
		const year = now.getFullYear();
		const month = String(now.getMonth() + 1).padStart(2, '0');
		const day = String(now.getDate()).padStart(2, '0');
		return `${year}-${month}-${day}`;
	}

	let selectedDate = $state(getLocalDate());
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

			daftarSiswa.forEach(siswa => {
				selectedKehadiran[siswa.id] = "";
				valueInputCatatan[siswa.id] = "";
			});

			resetKehadiranState();
			await fetchAbsensi(selectedDate);
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	function resetKehadiranState() {
		const newKehadiran = {};
		const newCatatan = {};
		daftarSiswa.forEach(siswa => {
			newKehadiran[siswa.id] = "";
			newCatatan[siswa.id] = "";
		});
		selectedKehadiran = newKehadiran;
		valueInputCatatan = newCatatan;
	}

	async function fetchAbsensi(tanggal) {
		try {
			isLoading = true;
			const res = await fetch(
				`${PUBLIC_API_BASE_URL}/absensi/tanggal/${tanggal}`, 
				{ credentials: "include" }
			);
			
			if (!res.ok) throw new Error("Gagal memuat data absensi");
			
			const data = await res.json();
			
			const newKehadiran = { ...selectedKehadiran };
			const newCatatan = { ...valueInputCatatan };
			
			data.forEach(absensi => {
				newKehadiran[absensi.siswa_id] = absensi.kehadiran;
				newCatatan[absensi.siswa_id] = absensi.note || "";
			});
			
			selectedKehadiran = newKehadiran;
			valueInputCatatan = newCatatan;
			
		} catch (error) {
			console.error("Error fetching absensi:", error);
			errorMessage = error.message;
		} finally {
			isLoading = false;
		}
	}

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

	function handleKehadiranChange(siswaId, value) {
		selectedKehadiran = {
			...selectedKehadiran,
			[siswaId]: value
		};
		if (value === "Hadir") {
			valueInputCatatan = {
				...valueInputCatatan,
				[siswaId]: ""
			};
		}
	}

	async function handleDateChange() {
		resetKehadiranState();
		await fetchAbsensi(selectedDate);
	}

	async function handleSubmit() {
		try {

			const belumDiisi = filteredSiswa.filter(s => selectedKehadiran[s.id] === "");
			if (belumDiisi.length > 0) {
				alert(`Masih ada ${belumDiisi.length} siswa yang belum diabsen!`);
				return;
			}

			const payload = {
				data: filteredSiswa.map(item => ({
					siswa_id: item.id,
					kehadiran: selectedKehadiran[item.id],
					catatan: valueInputCatatan[item.id] || null,
					tanggal: selectedDate
				}))
			};

			const res = await fetch(`${PUBLIC_API_BASE_URL}/absensi/bulk`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
				body: JSON.stringify(payload)
			});

			if (!res.ok) {
				const errorData = await res.json().catch(() => null);
				throw new Error(errorData?.detail || "Gagal menyimpan absensi");
			}
			
			alert("Absensi berhasil disimpan!");
			editStatus = false;
		} catch (error) {
			console.error(error);
			errorMessage = error.message;
		}
	}
</script>

<section class="sidebar-gap">
	<h1 class="my-4">Absensi - {selectedDate}</h1>

	<div class="container border rounded">

		<div class="d-flex justify-content-between">
			<div class="d-flex ms-2 my-3">
				<div class="mx-3">
					<span class="mb-2">Pilih Kelas</span>
					<select 
						class="form-select text-center" 
						bind:value={selectedKelasId}
						aria-label="Pilih kelas">
						<option value="">Semua Kelas</option>
						{#each daftarKelas as kelas}
							<option value={String(kelas.id)}>{kelas.nama}</option>
						{/each}
					</select>
				</div>
				<div>
					<span class="mb-2">Pilih Tanggal</span>
					<input 
						type="date" 
						class="form-control" 
						bind:value={selectedDate}
						onchange={handleDateChange}>
				</div>
			</div>

			<div class="me-2 mt-4">
				{#if editStatus === true}
					<button 
						class="btn btn-success" 
						onclick={handleSubmit}>
						{isLoading ? 'Menyimpan...' : 'Simpan Perubahan'}
					</button>
				{:else}
					<button 
						class="btn btn-primary" 
						onclick={() => editStatus = true}>
						Edit
					</button>
				{/if}
			</div>
		</div>

		<div>
			{#if errorMessage}
				<p class="text-danger">{errorMessage}</p>
			{:else if isLoading}
				<p>Memuat data...</p>
			{:else if daftarSiswa.length === 0}
				<p>Tidak ada data siswa...</p>
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
											id={"inputHadir-" + item.id}
											name={"kehadiran-" + item.id}
											value="Hadir"
											disabled={editStatus === false}
											checked={selectedKehadiran[item.id] === "Hadir"}
											onchange={() => handleKehadiranChange(item.id, "Hadir")}
											style="font-size: 25px;">
										<label 
											for={"inputHadir-" + item.id}
											class="form-check-label">
											Hadir
										</label>
									</div>

									<!-- Izin -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-yellowgreen">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputIzin-" + item.id}
											name={"kehadiran-" + item.id}
											value="Izin"
											disabled={editStatus === false}
											checked={selectedKehadiran[item.id] === "Izin"}
											onchange={() => handleKehadiranChange(item.id, "Izin")}
											style="font-size: 25px;">
										<label 
											for={"inputIzin-" + item.id}
											class="form-check-label">
											Izin
										</label>
									</div>

									<!-- Sakit -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-yellow">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputSakit-" + item.id}
											name={"kehadiran-" + item.id}
											value="Sakit"
											disabled={editStatus === false}
											checked={selectedKehadiran[item.id] === "Sakit"}
											onchange={() => handleKehadiranChange(item.id, "Sakit")}
											style="font-size: 25px;">
										<label 
											for={"inputSakit-" + item.id}
											class="form-check-label">
											Sakit
										</label>
									</div>

									<!-- Alpha -->
									<div class="form-check d-flex flex-column align-items-center justify-content-start h-100 bg-radio-red">
										<input 
										 	type="radio" 
											class="form-check-input ms-0"
											id={"inputAlpha-" + item.id}
											name={"kehadiran-" + item.id}
											value="Alpha"
											disabled={editStatus === false}
											checked={selectedKehadiran[item.id] === "Alpha"}
											onchange={() => handleKehadiranChange(item.id, "Alpha")}
											style="font-size: 25px;">
										<label 
											for={"inputAlpha-" + item.id}
											class="form-check-label">
											Alpha
										</label>
									</div>
								</td>
								<td>
									<input 
										type="text" 
										class="form-control text-center" 
										placeholder="Tambahkan catatan"
										bind:value={valueInputCatatan[item.id]}
										disabled={
											selectedKehadiran[item.id] === "Hadir" ||
											selectedKehadiran[item.id] === "" ||
											editStatus === false
										}
									/>
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
