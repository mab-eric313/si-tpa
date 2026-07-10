<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	let errorMessage = $state("");
	let daftarCalonSiswa = $state([]);
	let daftarKelas = $state([]);
	let daftarSiswa = $state([]);

	onMount(async () => {
		try {
			// TODO: change hardcoded url. Make URL variable placed in $lib dir
			const [resCalonSiswa, resKelas] = await Promise.all([
				fetch("http://localhost:8000/pendaftaran-siswa/", { 
					credentials: "include",
				}),
				fetch("http://localhost:8000/kelas/", { 
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
				`http://localhost:8000/siswa/${id}`, {
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
				`http://localhost:8000/pendaftaran-siswa/${id}`, {
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

<section class="sidebar-gap">
	<h1 class="py-5">Kelola Data Calon Siswa</h1>

	<div class="container border rounded">
		{#if errorMessage}
			<p class="text-danger">{errorMessage}</p>
		{:else if daftarCalonSiswa.length === 0}
			<p>Sedang memuat data atau tidak ada data calon siswa...</p>
		{:else}
			<table class="table table-bordered text-center">
				<thead>
				<tr>
					<th>No</th>
					<th>Nama Calon Siswa</th>
					<th>Tanggal lahir</th>
					<th>Alamat Calon Siswa</th>
					<th>Nama Wali</th>
					<th>Alamat Wali</th>
					<th>No Hp Wali</th>
					<th>Kelas</th>
					<th class="text-center">Action</th>
				</tr>
				</thead>
				<tbody>
					{#each daftarCalonSiswa.filter(
						calon => calon.status === "Pending"
					) as calonSiswa}
						<tr>
							<td>{calonSiswa.id}</td>
							<td>{calonSiswa.nama_siswa}</td>
							<td>{calonSiswa.tanggal_lahir_siswa}</td>
							<td>{calonSiswa.alamat_siswa ?? 'NULL'}</td>
							<td>{calonSiswa.nama_wali}</td>
							<td>{calonSiswa.alamat_wali ?? 'NULL'}</td>
							<td>{calonSiswa.no_hp_wali ?? 'NULL'}</td>
							<td>{getNamaKelas(calonSiswa.kelas_id)}</td>
							<td class="text-center">
								<button
									class="btn btn-sm btn-success" 
									aria-label="Tambah"
									onclick={() => handleAdd(calonSiswa.id)}>
									<i class="bi bi-plus"></i>
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

