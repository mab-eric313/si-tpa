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
				fetch(`${PUBLIC_API_BASE_URL}/siswa/`, { 
					credentials: "include",
				}),
				fetch(`${PUBLIC_API_BASE_URL}/kelas/`, { 
					credentials: "include",
				}),
				fetch(`${PUBLIC_API_BASE_URL}/wali/`, { 
					credentials: "include",
				}),
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
	};

	function getNamaWali(id) {
		return daftarWali.find(k => k.id == id)?.nama ?? "-";
	};

	function getAlamatWali(id) {
		return daftarWali.find(k => k.id == id)?.alamat ?? "-";
	};

	function getNoHpWali(id) {
		return daftarWali.find(k => k.id == id)?.no_hp ?? "-";
	};

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

<section class="sidebar-gap">
	<h1 class="py-5">Kelola Data Siswa</h1>

	<div class="container border rounded">
		<div class="d-flex justify-content-between">
			<div class="ms-2 my-3">
				<span class="mb-2">Pilih Kelas</span>
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
		</div>
		{#if errorMessage}
			<p class="text-danger">{errorMessage}</p>
		{:else if daftarSiswa.length === 0}
			<p>Sedang memuat data atau tidak ada data siswa...</p>
		{:else}
			<table class="table table-bordered text-center">
				<thead>
				<tr>
					<th>No</th>
					<th>Nama Siswa</th>
					<th>Tanggal lahir</th>
					<th>Alamat Siswa</th>
					<th>Nama Wali</th>
					<th>Alamat Wali</th>
					<th>No Hp Wali</th>
					<th>Kelas</th>
					<th>Status</th>
					<th class="text-center">Action</th>
				</tr>
				</thead>
				<tbody>
					{#each filteredSiswa as siswa, i}
						<tr>
							<td>{i + 1}</td>
							<td>{siswa.nama}</td>
							<td>{siswa.tanggal_lahir}</td>
							<td>{siswa.alamat ?? 'NULL'}</td>
							<td>{getNamaWali(siswa.wali_id)}</td>
							<td>{getAlamatWali(siswa.wali_id)}</td>
							<td>{getNoHpWali(siswa.wali_id)}</td>
							<td>{getNamaKelas(siswa.kelas_id)}</td>
							<td>
								{#if siswa.status === "Aktif"}
									<span class="badge bg-success">Aktif</span>
								{:else}
									<span class="badge bg-secondary">Tidak Aktif</span>
								{/if}
							</td>
							<td class="text-center">
								<button
									class="btn btn-sm btn-primary fs-small" 
									aria-label="Edit"
									onclick={() => handleEdit(siswa.id)}>
									<i class="bi bi-pencil-fill"></i>
									Edit
								</button>
								{#if siswa.status === "Aktif"}
									<button
										class="btn btn-sm btn-danger fs-small"
										aria-label="Delete"
										onclick={() => handleDelete(siswa.id)}>
										<i class="bi bi-trash-fill"></i>
										Hapus
									</button>
								{/if}
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

	.fs-small {
		font-size: 15px;
	}
</style>

