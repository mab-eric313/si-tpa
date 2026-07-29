<script>
	import { onMount } from "svelte";
	import { goto } from "$app/navigation";

	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let errorMessage = $state("");
	let daftarUser = $state([]);

	onMount(async () => {
		try {
			const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);
			daftarUser = await response.json();
		} catch(error) {
			console.error(error);
			errorMessage = error.message;
		}
	});

	function handleAdd() {
		goto(`users/add`);
	}

	function handleEdit(id) {
		goto(`users/edit/${id}`);
	}

	async function handleDelete(id) {
		const konfirmasi = confirm("Yakin ingin menghapus data ini?");
		if (!konfirmasi) return;

		try {
			const resBiodata = await fetch(
				`${PUBLIC_API_BASE_URL}/biodata-user/by-user/${id}`, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!resBiodata.ok) throw new Error(`${resBiodata.statusText}`);

			const resUser = await fetch(`${PUBLIC_API_BASE_URL}/auth/${id}`, {
				method: "DELETE",
				headers: { "Content-Type": "application/json" },
				credentials: "include",
			});
			if (!resUser.ok) throw new Error(`${resUser.statusText}`);

			daftarUser = daftarUser.filter(item => item.id !== id);
		} catch (error) {
			console.error("Error deleting data: ", error);
			errorMessage = error.message;
		}
	}
</script>

<section class="content-section">
	<h1 class="mb-4">Kelola Data Pengguna</h1>

	<div class="table-container border rounded bg-white">
		<div class="filter-section p-3 border-bottom">
			<div class="row g-3">
				<div class="col-md-6">
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
		{:else if daftarUser.length === 0}
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
						<th>Username</th>
						<th>Nama Lengkap</th>
						<th>Nama Panggilan</th>
						<!-- <th>No Hp</th> -->
						<!-- <th>Alamat</th> -->
						<th>Role</th>
						<th>Status</th>
						<th>Action</th>
					</tr>
					</thead>
					<tbody>
						{#each daftarUser as user, i}
						<tr>
							<td>{i + 1}</td>
							<td class="fw-semibold">{user.username}</td>
							{#if user.biodata === null}
								<td>-</td>
								<td>-</td>
								<td>-</td>
								<td>-</td>
							{:else}
								<td>{user.biodata.nama_lengkap}</td>
								<td>{user.biodata.nama_panggilan}</td>
								<!-- <td>{user.biodata.no_hp}</td> -->
								<!-- <td>{user.biodata.alamat}</td> -->
							{/if}
							<td>
								{user.role.charAt(0).toUpperCase() + user.role.slice(1)}
							</td>
							{#if user.biodata === null}
								<td>-</td>
							{:else}
								<td class="text-center">
									{#if user.biodata.status === "Aktif"}
										<span class="badge bg-success">Aktif</span>
									{:else}
										<span class="badge bg-secondary">Tidak Aktif</span>
									{/if}
								</td>
							{/if}
							<td class="text-center">
								<div class="btn-group-vertical btn-group-sm d-md-none">
									<button
										class="btn btn-sm btn-primary" 
										onclick={() => handleEdit(user.id)}>
										<i class="bi bi-pencil-fill"></i>
										Edit
									</button>
									{#if user.biodata.status === "Aktif"}
										<button
											class="btn btn-sm btn-danger"
											onclick={() => handleDelete(user.id)}>
											<i class="bi bi-trash-fill"></i>
											Hapus
										</button>
									{/if}
								</div>
								<div class="btn-group d-none d-md-inline-flex">
									<button
										class="btn btn-sm btn-primary" 
										onclick={() => handleEdit(user.id)}>
										<i class="bi bi-pencil-fill"></i>
										Edit
									</button>
									{#if user.biodata.status === "Aktif"}
										<button
											class="btn btn-sm btn-danger"
											onclick={() => handleDelete(user.id)}>
											<i class="bi bi-trash-fill"></i>
											Hapus
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
		font-size: 15px;
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
