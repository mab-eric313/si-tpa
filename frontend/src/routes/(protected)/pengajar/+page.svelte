<script>
	import { onMount } from 'svelte';

	let daftarSiswa = $state([]);

	onMount(async () => {
		try {
			const response = await fetch("http://localhost:8000/siswa/");
			if (!response.ok) throw new Error("Failed to take data");
			daftarSiswa = await response.json();
		} catch(error) {
			console.error("Error fetching data: ", error);
		}
	});
</script>

<section>
	<div class="container text-center pb-5">
		<div class="row">
			<div class="col text-center d-flex align-items-center justify-content-center">
				<h2>1</h2>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center">
				<h2>2</h2>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center">
				<h2>3</h2>
			</div>
			<div class="col text-center d-flex align-items-center justify-content-center">
				<h2>4</h2>
			</div>
		</div>
	</div>
</section>

<main class="table-container">
	<h1>Data Siswa</h1>
	{#if daftarSiswa.length > 0}
		<table>
			<thead>
				<tr>
					<th>ID</th>
					<th>Name</th>
					<th>Gender</th>
					<th>Birth Date</th>
					<th>Address</th>
					<th>Wali ID</th>
					<th>Class ID</th>
				</tr>
			</thead>
			<tbody>
				{#each daftarSiswa as siswa}
					<tr>
						<td>{siswa.id}</td>
						<td>{siswa.nama}</td>
						<td>{siswa.jenis_kelamin}</td>
						<td>{siswa.tanggal_lahir}</td>
						<td>{siswa.alamat}</td>
						<td>{siswa.wali_id}</td>
						<td>{siswa.kelas_id}</td>
					</tr>
				{/each}
			</tbody>
		</table>
	{:else}
		<p>Sedang memuat data...</p>
	{/if}
</main>

<style>
	.table-container {
		overflow-x: auto;
		width: 100%;
	}
	table {
		width: 100%;
		border-collapse: collapse;
		text-align: left;
		font-family: sans-serif;
	}
	th, td {
		padding: 12px;
		border-bottom: 1px solid #e2e8f0;
	}
	th {
		background-color: #f8fafc;
		color: #64748b;
		font-weight: 600;
	}
	tr:hover {
		background-color: #f1f5f9;
	}

	.container {
		display: grid;
		margin-top: 10px;
	}

	.col {
		height: 150px;
		margin-right: 10px;
		margin-bottom: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		border-radius: 10px;
		padding: 20px;
	}

</style>
