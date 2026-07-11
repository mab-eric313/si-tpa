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

<section class="sidebar-gap">
	<h1 class="py-5">Kelola Data Pengguna</h1>

	<div class="container border rounded">
		<div class="d-flex justify-content-end my-3">
			<button 
				class="btn btn-primary"
				onclick={handleAdd}>
				Tambah Data
			</button>
		</div>
		{#if errorMessage}
			<p class="text-danger">{errorMessage}</p>
		{:else if daftarUser.length === 0}
			<p>Sedang memuat data...</p>
		{:else}
			<table class="table table-bordered text-center">
				<thead>
				<tr>
					<th>No</th>
					<th>Username</th>
					<th>Nama Lengkap</th>
					<th>Nama Panggilan</th>
					<th>No Hp</th>
					<th>Alamat</th>
					<th>Role</th>
					<th>Status</th>
					<th class="text-center">Action</th>
				</tr>
				</thead>
				<tbody>
					{#each daftarUser as user}
					<tr>
						<td>{user.id}</td>
						<td>{user.username}</td>
						{#if user.biodata === null}
							<td>NULL</td>
							<td>NULL</td>
							<td>NULL</td>
							<td>NULL</td>
						{:else}
							<td>{user.biodata.nama_lengkap}</td>
							<td>{user.biodata.nama_panggilan}</td>
							<td>{user.biodata.no_hp}</td>
							<td>{user.biodata.alamat}</td>
						{/if}
						<td>{user.role.charAt(0).toUpperCase() + user.role.slice(1)}</td>
						{#if user.biodata === null}
							<td>NULL</td>
						{:else}
							<td>{user.biodata.status}</td>
						{/if}
						<td class="text-center">
							<button
								href="/admin/users/edit/{user.id}"
								class="btn btn-sm btn-primary" 
								aria-label="Edit"
								onclick={() => handleEdit(user.id)}>
								<i class="bi bi-pencil-fill"></i>
								Edit
							</button>
							<button
								href="/admin/users/delete/{user.id}"
								class="btn btn-sm btn-danger"
								aria-label="Delete"
								onclick={() => handleDelete(user.id)}>
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
