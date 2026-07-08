<!-- Header.svelte -->
<script>
	import { page } from '$app/state';

	import homeIcon from "$lib/assets/home.svg";
	import exitIcon from "$lib/assets/exit.svg";

	// TODO: Use Lucide Icons
	// import { NotebookPen, FileUser } from "@lucide/svelte";
	import { DollarSign } from "@lucide/svelte";
</script>

<svelte:head>
	<title>Sistem Informasi TPA</title>
</svelte:head>

<nav class="d-flex flex-column flex-shrink-0 min-vh-100 position-fixed">
	<ul class="nav-sidebar">
		<div class="nav-sidebar-main">
			<li class="logo">
				<h1 style="font-size: 33px;">Bendahara</h1>
			</li>
			<!--
			<li class="nav-sidebar-item">
				<a href="/bendahara" 
					class:active={page.url.pathname === "/bendahara"}>
					<img src={homeIcon} alt="">
					Beranda
				</a>
			</li>
			<li class="nav-sidebar-item">
				<a href="/bendahara/kelas" 
					class:active={page.url.pathname === "/bendahara/laporan"}>
					Laporan
				</a>
			</li>
			-->
			<li class="nav-sidebar-item">
				<a href="/bendahara/pencatatan"
				   class:active={page.url.pathname === "/bendahara/pencatatan"}>
					<div class="icon"><DollarSign /></div>
					Pencatatan
				</a>
			</li>
		</div>
		<li id="logout" class="nav-sidebar-item">
			<a href="/login">
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
