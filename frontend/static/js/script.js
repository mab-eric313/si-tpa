async function loadStaticPage(staticPage) {
	try {
		const response = await fetch(`/static/static/html/${staticPage}`)
		if (!response.ok) throw new Error(`Halaman '${staticPage}' tidak ditemukan`)
		const html = await response.text()
		document.getElementById("content").innerHTML = html
	} catch (error) {
		document.getElementById("content").innerHTML = `
			<p>Error: ${error.message}</p>
		`
	}
}

const navItems = document.querySelectorAll(".nav-item")
navItems.forEach(item => {
	item.addEventListener("click", async (e) => {
		e.preventDefault()
		const page = e.target.dataset.page
		await loadStaticPage(page)
	})
})

loadStaticPage("dashboard.html")
