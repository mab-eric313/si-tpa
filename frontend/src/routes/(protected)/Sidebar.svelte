<script>
	import { page } from '$app/state';
	import { goto } from '$app/navigation';
	import { PUBLIC_API_BASE_URL } from '$env/static/public';

	let isLoggingOut = $state(false);
	let isSidebarOpen = $state(false);

	let role = $derived(page.url.pathname.split('/')[1]);

	const menuConfig = {
		admin: [
			{ href: '/admin', label: 'Beranda', icon: 'bi-house' },
			{ href: '/admin/kelola-pengguna', label: 'Kelola Pengguna', icon: 'bi-people' },
			{ href: '/admin/kelola-siswa', label: 'Kelola Siswa', icon: 'bi-person-vcard' },
			{ href: '/admin/kelola-calon-siswa', label: 'Kelola Calon Siswa', icon: 'bi-person-plus' },
			{ href: '/admin/kelola-kelas', label: 'Kelola Kelas', icon: 'bi-building' },
			{ href: '/pengajar', label: 'Ke Hal. Pengajar', icon: 'bi-arrow-right-circle' },
			{ href: '/bendahara/pencatatan', label: 'Ke Hal. Bendahara', icon: 'bi-arrow-right-circle' }
		],
		bendahara: [
			{ href: '/bendahara/pencatatan', label: 'Pencatatan', icon: 'bi-cash-stack' },
			/*
			{ href: '/bendahara/transaksi', label: 'Transaksi', icon: 'bi-receipt' },
			{ href: '/bendahara/laporan', label: 'Laporan', icon: 'bi-file-earmark-bar-graph' }
			*/
		],
		pengajar: [
			{ href: '/pengajar', label: 'Beranda', icon: 'bi-house' },
			{ href: '/pengajar/penilaian', label: 'Penilaian', icon: 'bi-journal-check' },
			{ href: '/pengajar/absensi', label: 'Absensi', icon: 'bi-calendar-check' }
		]
	};

	let currentMenu = $derived(menuConfig[role] || menuConfig.admin);

	function toggleSidebar() {
		isSidebarOpen = !isSidebarOpen;
	}

	function closeSidebar() {
		isSidebarOpen = false;
	}

	function isActive(href) {
		return page.url.pathname === href;
	}

	async function handleLogout(event) {
		event.preventDefault();
		if (isLoggingOut) return;
		
		isLoggingOut = true;
		try {
			const response = await fetch(`${PUBLIC_API_BASE_URL}/auth/logout/`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				credentials: "include"
			});
			if (!response.ok) throw new Error(`Error: ${response.statusText}`);
			goto("/login");
		} catch (error) {
			console.error("Logout gagal:", error);
			isLoggingOut = false;
		}
	}
</script>

<svelte:head>
	<title>Sistem Informasi TPA — {role.charAt(0).toUpperCase() + role.slice(1)}</title>
</svelte:head>


{#if isSidebarOpen}
	<div class="sidebar-overlay" onclick={closeSidebar}></div>
{/if}

<button class="hamburger-btn" onclick={toggleSidebar} aria-label="Toggle menu">
	<i class="bi bi-list"></i>
</button>

<nav class="sidebar-container" class:open={isSidebarOpen}>
	<div class="sidebar-logo">
		<i class="bi bi-book-half me-2"></i>
		<h1>{role.charAt(0).toUpperCase() + role.slice(1)}</h1>
		<button class="close-btn d-md-none" onclick={closeSidebar}>
			<i class="bi bi-x-lg"></i>
		</button>
	</div>

	<ul class="sidebar-section">
		{#each currentMenu as item}
			<a 
				href={item.href} 
				class="nav-link" 
				class:active={isActive(item.href)}
				onclick={closeSidebar}
			>
				<i class="bi {item.icon}"></i>
				<span>{item.label}</span>
			</a>
		{/each}
	</ul>

	<div class="sidebar-footer">
		<a href="/login" class="nav-link text-danger" onclick={handleLogout}>
			<i class="bi bi-box-arrow-right"></i>
			<span>{isLoggingOut ? 'Memproses...' : 'Logout'}</span>
		</a>
	</div>
</nav>

<style>
	.sidebar-overlay {
		position: fixed;
		top: 0;
		left: 0;
		width: 100%;
		height: 100%;
		background-color: rgba(0, 0, 0, 0.5);
		z-index: 1029;
		display: none;
	}

	.hamburger-btn {
		display: none;
		position: fixed;
		top: 15px;
		left: 15px;
		z-index: 1031;
		background-color: #1a3a2e;
		color: white;
		border: none;
		padding: 10px 15px;
		border-radius: 8px;
		font-size: 20px;
		cursor: pointer;
		box-shadow: 0 2px 8px rgba(0,0,0,0.2);
	}

	.close-btn {
		background: none;
		border: none;
		color: white;
		font-size: 24px;
		cursor: pointer;
		padding: 5px;
		margin-left: auto;
	}

	.sidebar-container {
		width: 260px;
		height: 100%;
		min-height: 100vh;
		background-color: #1a3a2e;
		display: flex;
		flex-direction: column;
		z-index: 1030;
		position: fixed;
		top: 0;
		left: 0;
		transform: translateX(-100%);
		transition: transform 0.3s ease;
	}

	.sidebar-logo {
		display: flex;
		align-items: center;
		color: white;
		padding: 20px;
		flex-shrink: 0;
		border-bottom: 1px solid rgba(255, 255, 255, 0.1);
		gap: 10px;
	}

	.sidebar-logo h1 {
		font-size: 24px;
		font-weight: bold;
		margin: 0;
		flex: 1;
	}

	.sidebar-logo i {
		font-size: 28px;
	}

	.sidebar-section {
		flex: 1;
		overflow-y: auto;
		min-height: 0;
		padding: 10px 15px;
		display: flex;
		flex-direction: column;
		gap: 8px;
		margin: 0;
		list-style: none;
		
		/*
		scrollbar-width: thin;
		scrollbar-color: rgba(255, 255, 255, 0.3) transparent;
		*/
	}

	.sidebar-section::-webkit-scrollbar {
		width: 6px;
	}
	.sidebar-section::-webkit-scrollbar-track {
		background: transparent;
	}
	.sidebar-section::-webkit-scrollbar-thumb {
		background-color: rgba(255, 255, 255, 0.3);
		border-radius: 3px;
	}
	.sidebar-section::-webkit-scrollbar-thumb:hover {
		background-color: rgba(255, 255, 255, 0.5);
	}

	.nav-link {
		display: flex;
		align-items: center;
		gap: 12px;
		color: rgba(255, 255, 255, 0.85);
		text-decoration: none;
		padding: 12px 15px;
		border-radius: 8px;
		font-size: 15px;
		font-weight: 500;
		transition: all 0.2s ease;
		flex-shrink: 0;
	}

	.nav-link i {
		font-size: 18px;
		width: 24px;
		text-align: center;
	}

	.nav-link:hover {
		background-color: rgba(255, 255, 255, 0.1);
		color: white;
	}

	.nav-link.active {
		background-color: #2d6a4f;
		color: white;
		font-weight: 600;
	}

	.sidebar-footer {
		flex-shrink: 0;
		padding: 20px 15px;
		border-top: 1px solid rgba(255, 255, 255, 0.1);
	}

	.nav-link.text-danger {
		color: #ff6b6b;
	}
	
	.nav-link.text-danger:hover {
		background-color: rgba(255, 107, 107, 0.1);
		color: #ff5252;
	}

	/* =========================================
	   RESPONSIVE - MOBILE (max-width: 768px)
	   ========================================= */
	@media (max-width: 768px) {
		.hamburger-btn {
			display: block;
			z-index: 50;
		}

		.sidebar-overlay {
			display: block;
		}

		.sidebar-container.open {
			transform: translateX(0);
		}

		:global(.main-content) {
			padding-top: 70px;
		}
	}

	/* =========================================
	   RESPONSIVE - DESKTOP (min-width: 769px)
	   ========================================= */
	@media (min-width: 769px) {
		.sidebar-container {
			transform: translateX(0);
			position: relative;
		}

		.hamburger-btn,
		.close-btn,
		.sidebar-overlay {
			display: none !important;
		}
	}
</style>
