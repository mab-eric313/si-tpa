<section>
	<div class="title">
		<h1>Dashboard</h1>
		<p>Selamat datang di Sistem Informasi TPQ</p>
	</div>
	<div class="grid-wrapper">
		<div class="grid-top-left">
			<div class="small-card-1">
				<h2>1</h2>
			</div>
			<div class="small-card-2">
				<h2>2</h2>
			</div>
		</div>
		<div class="grid-top-right">
			<div class="small-card-3">
				<h2>3</h2>
			</div>
			<div class="small-card-4">
				<h2>4</h2>
			</div>
		</div>
		<div class="grid-bottom-left">
			<div class="card">
				<h2>5</h2>
			</div>
		</div>
		<div class="grid-bottom-right">
			<div class="card">
				<h2>6</h2>
			</div>
		</div>
	</div>
</section>

<style>
	h2 {
		color: black;
	}

	.title {
		margin-bottom: 10px;
	}

	.grid-wrapper {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(400px, 1fr));
		margin-top: 10px;
	}

	.grid-top-left {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
		margin-right: 10px;
		margin-bottom: 10px;
	}

	.grid-top-left .small-card-1{
		display: flex;
		height: 250px;
		margin-right: 10px;
		margin-bottom: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		border-radius: 10px;
		padding: 20px;
	}

	.grid-top-left .small-card-2 {
		display: flex;
		height: 250px;
		margin-left: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		padding: 20px;
	}
	
	.grid-top-right {
		display: grid;
		grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
		margin-left: 10px;
		margin-bottom: 10px;
	}

	.grid-top-right .small-card-3 {
		display: flex;
		height: 250px;
		margin-right: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		padding: 20px;
	}

	.grid-top-right .small-card-4 {
		display: flex;
		height: 250px;
		margin-left: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		padding: 20px;
	}
	
	.grid-bottom-left {
		height: 300px;
		margin-right: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		padding: 20px;
	}

	.grid-bottom-right {
		height: 300px;
		margin-left: 10px;
		margin-bottom: 10px;
		border-radius: 10px;
		box-shadow: 0 2px 8px rgba(0, 0, 0, 0.8);
		padding: 20px;
	}
</style>
