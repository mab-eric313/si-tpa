import * as hello from "./hello.js"

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

function firstLoad(staticPage) {
	loadStaticPage(staticPage)
	const activeNavItem = document.getElementById(staticPage.replace(".html", ""))
	activeNavItem.classList.add("active")
}

const navSidebarItems = document.querySelectorAll(".nav-sidebar-item")
navSidebarItems.forEach(item => {
    item.addEventListener("click", async (e) => {
        e.preventDefault()
        const anchor = item.querySelector("a.nav-item")
        const page = anchor.dataset.page
        await loadStaticPage(page)

        navSidebarItems.forEach(i => i.querySelector("a").classList.remove("active"))
        anchor.classList.add("active")
    })
})

firstLoad("dashboard.html")
console.log(hello.range)
