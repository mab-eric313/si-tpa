<svelte:head>
	<title>Login - TPA Ar-Rahmah</title>
	<link
		href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap"
		rel="stylesheet"
	/>
</svelte:head>

<section id="login-section">
	<!-- TODO: Login form is not same with the design -->
	<div class="contact-form container p-5">
		<h3 class="mb-4">Login</h3>
		<form class="mb-5">
			<div class="mb-3">
				<label for="username" class="form-label">Username</label>
				<input 
					type="text" 
					class="form-control"
					id="Username" 
					name="Username" 
					placeholder="Input your username">
			</div>
			<div class="mb-3">
				<label for="message" class="form-label">Password</label>
				<input
					type="password"
					class="form-control"
					id="password" 
					name="password" 
					placeholder="Input your Password">
			</div>
		</form>
		<button type="submit" class="container btn btn-primary">Submit</button>
	</div>
</section>
