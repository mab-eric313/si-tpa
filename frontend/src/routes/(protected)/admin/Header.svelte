<!-- Header.svelte -->
<script>
	import { resolve } from "$app/paths";
	import { page } from '$app/state';
	import { goto } from "$app/navigation";

	// TODO: change icons to Lucide
	// Icons
	import accountIcon from "$lib/assets/account.svg";
	import calendarIcon from "$lib/assets/calendar4.svg";
	import checkSquareIcon from "$lib/assets/check2-square.svg";
	import currencyDollarIcon from "$lib/assets/currency-dollar.svg";
	import exitIcon from "$lib/assets/exit.svg";
	import faviconIcon from "$lib/assets/favicon.svg";
	import fileTextIcon from "$lib/assets/file-text.svg";
	import homeIcon from "$lib/assets/home.svg";
	import personsIcon from "$lib/assets/persons.svg";

	// Lucide Icons
	import { NotebookPen, FileUser } from "@lucide/svelte";

	async function handleLogout(event) {
		event.preventDefault();

		try {
			const response = await fetch("http://localhost:8000/auth/logout/", {
				method: "POST",
				headers: {"Content-Type": "application/json"},
				credentials: "include"
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);
			goto("/login");
		} catch (error) {
			console.error(error);
		}
	}
</script>

<svelte:head>
	<title>Sistem Informasi TPA — Admin</title>
</svelte:head>

<nav class="d-flex flex-column flex-shrink-0 min-vh-100 position-fixed">
	<ul class="nav-sidebar">
		<div class="nav-sidebar-main">
			<li class="logo">
				<h1>Admin</h1>
			</li>
			<li class="nav-sidebar-item">
				<a href="/admin" 
					class:active={page.url.pathname === "/admin"}>
					<img src={homeIcon} alt="">
					Beranda
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/admin/kelola-pengguna" 
					class:active={page.url.pathname === "/admin/kelola-pengguna"}>
					<img src={personsIcon} alt="">
					Kelola Pengguna
				</a>
			</li>
			<!--
			<li class="nav-sidebar-item">
				<a href="/pengajar/absensi"
				   class:active={page.url.pathname === "/pengajar/absensi"}>
					<img src={checkSquareIcon} alt="">
					Absensi
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/pengajar/rekap-nilai"
				   class:active={page.url.pathname === "/pengajar/rekap-nilai"}>
					<div class="icon"><NotebookPen /></div>
					Rekap Nilai
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/pengajar/rekap-absensi"
				   class:active={page.url.pathname === "/pengajar/rekap-absensi"}>
					<img src={fileTextIcon} alt="">
					Rekap Absensi
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/pengajar/ajukan-pergantian"
				   class:active={page.url.pathname === "/pengajar/ajukan-pergantian"}>
					<div class="icon"><FileUser /></div>
					Ajukan Pergantian
				</a>
			</li>
		</div>
			-->
		<li id="logout" class="nav-sidebar-item">
			<a href="/login" onclick={handleLogout}>
				<img src={exitIcon} alt="exit icon">
				Logout
			</a>
		</li>
	</ul>
</nav>

<style>
	nav {
		z-index: 1030;
	}

	.logo {
		padding: 20px 20px;
		color: white;
		list-style: none;
	}

	.nav-sidebar {
		display: flex;
		flex-direction: column;
		justify-content: space-between;
		background-color: #1a3a2e;
		float: left;
		padding: 0 15px;
		min-height: 100vh;
	}

	.nav-sidebar-item {
		display: flex;
		flex-direction: row;
		align-items: center;
		margin: 8px 0;
		border-radius: 10px;
		list-style: none;
	}

	.nav-sidebar-item img {
		width: 23px;
		margin-right: 10px;
		pointer-events: none;
	}

	.nav-sidebar-item a {
		display: flex;
		color: white;
		text-decoration: none;
		padding: 10px 20px;
		width: 100%;
		align-items: center;
	}

	.nav-sidebar-item:hover {
		background-color: rgba(45, 106, 79);
		cursor: pointer;
	}

	.nav-sidebar-item:has(a.active) {
		background-color: rgba(45, 106, 79);
	}

	.icon {
		margin-right: 10px;
	}
</style>
