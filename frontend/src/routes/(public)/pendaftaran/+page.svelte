<script>
    import { onMount } from "svelte";
	import { PUBLIC_API_BASE_URL } from "$env/static/public";

	let namaSantri = $state('');
	let jenisKelamin = $state('');
	let tanggalLahir = $state('');
	let alamatSantri = $state('');
	let namaWali = $state('');
	let noHp = $state('');
	let alamatWali = $state('');
	let selectedKelas = $state('');

	let fotoKkFile = $state(null);
	let fotoAkFile = $state(null);
	let fotoPasFile = $state(null);

	let daftarKelas = $state([]);
	let errorMessage = $state('');
    let isSubmitting = $state(false);

	onMount(async () => {
		try {
			const res = await fetch(`${PUBLIC_API_BASE_URL}/kelas/`, {
				method: "GET",
				headers: { "Content-Type": "application/json" },
			});
			if (!res.ok) throw new Error(res.statusText);
			daftarKelas = await res.json();
		} catch (error) {
			console.error(error);
            errorMessage = "Gagal memuat data kelas.";
		}
	});

    function handleFileChange(fileStateSetter, e) {
        fileStateSetter(e.target.files[0] || null);
    }

	async function handleSubmit(e) {
		e.preventDefault();

        console.log("File KK:", fotoKkFile);
        console.log("File AK:", fotoAkFile);
        console.log("File Pas:", fotoPasFile);

        if (!namaSantri || !jenisKelamin || !tanggalLahir || !namaWali || !selectedKelas || !fotoKkFile || !fotoAkFile || !fotoPasFile) {
			errorMessage = 'Mohon lengkapi semua data wajib dan unggah semua foto.';
			return;
		}

        isSubmitting = true;
        errorMessage = '';

		try {
            const formData = new FormData();
            formData.append('nama_siswa', namaSantri);
            formData.append('status', 'Pending');
            formData.append('jenis_kelamin_siswa', jenisKelamin);
            formData.append('tanggal_lahir_siswa', tanggalLahir);
            formData.append('alamat_siswa', alamatSantri || '');
            formData.append('nama_wali', namaWali);
            formData.append('no_hp_wali', noHp || '');
            formData.append('alamat_wali', alamatWali || '');
            formData.append('kelas_id', selectedKelas);

            formData.append('foto_kk', fotoKkFile);
            formData.append('foto_ak', fotoAkFile);
            formData.append('foto_pas', fotoPasFile);

			const res = await fetch(
				`${PUBLIC_API_BASE_URL}/pendaftaran-siswa/form`, {
					method: "POST",
					body: formData
				}
			);
			if (!res.ok) {
                const errData = await res.json().catch(() => ({}));
                throw new Error(errData.detail || res.statusText);
			}

            alert('Pendaftaran berhasil dikirim! Admin akan segera menghubungi Anda.');
            resetForm();

		} catch (error) {
            console.error("Error submitting form: ", error);
            errorMessage = typeof error.message === 'string' ? error.message : "Terjadi kesalahan pada server";
		} finally {
            isSubmitting = false;
		}
	}

	function resetForm() {
		namaSantri = '';
		jenisKelamin = '';
		tanggalLahir = '';
		alamatSantri = '';
		namaWali = '';
		noHp = '';
		alamatWali = '';
		selectedKelas = '';
		fotoKkFile = null;
		fotoAkFile = null;
		fotoPasFile = null;

        document.querySelectorAll('input[type="file"]').forEach(input => input.value = '');
	}
</script>

<!-- UTAMA / CONTAINER -->
<div class="container">
  <div class="title">
    <h1>Pendaftaran Santri Baru</h1>
    <p>
      Silakan lengkapi form di bawah ini untuk mendaftarkan putra/putri Anda sebagai santri TPA Ar-Rahmah
    </p>
  </div>

  <!-- SYARAT -->
  <div class="card">
    <h2>Syarat Pendaftaran</h2>
    <ul>
      <li>Usia minimal 5 tahun</li>
      <li>Mengisi formulir pendaftaran dengan lengkap</li>
	  <li>Masukkan foto-foto yang dibutuhkan</li>
	  <ul>
		  <li>Foto Kartu Keluarga</li>
		  <li>Foto Akta Kelahiran</li>
		  <li>Pas foto ukuran 3x4</li>
	  </ul>
    </ul>
  </div>

  <!-- FORM PENDAFTARAN -->
  <div class="card">
    <h2>Form Pendaftaran</h2>

	<form onsubmit={handleSubmit}>
      <div class="form-group">
        <label for="nama-santri">Nama Lengkap Santri<span>*</span></label>
        <input 
          id="nama-santri"
          type="text" 
          placeholder="Masukkan nama lengkap" 
          bind:value={namaSantri}
          required
        />
      </div>

      <div class="form-group">
        <label for="jenis-kelamin">Jenis Kelamin<span>*</span></label>
		<select 
			id="jenis-kelamin" 
			class="form-select"
			bind:value={jenisKelamin}>
			<option value="" disabled>Pilih Jenis Kelamin</option>
			<option value="L">Laki-laki</option>
			<option value="P">Perempuan</option>
		</select>
      </div>

      <div class="form-group">
        <label for="tanggal-lahir">Tanggal Lahir<span>*</span></label>
        <input 
          id="tanggal-lahir"
          type="date" 
          placeholder="Masukkan tanggal lahir" 
          bind:value={tanggalLahir}
          min="5"
          required
        />
      </div>

      <div class="form-group">
        <label for="alamat-santri">Alamat Santri</label>
        <textarea 
          id="alamat-santri"
          placeholder="Masukkan alamat santri" 
          bind:value={alamatSantri}
        ></textarea>
      </div>

      <div class="form-group">
        <label for="nama-wali">Nama Orang Tua/Wali<span>*</span></label>
        <input 
          id="nama-wali"
          type="text" 
          placeholder="Masukkan nama orang tua/wali" 
          bind:value={namaWali}
          required
        />
      </div>

      <div class="form-group">
        <label for="no-hp">Nomor HP</label>
        <input 
          id="no-hp"
          type="text" 
          placeholder="contoh: 081234567890" 
          bind:value={noHp}
        />
      </div>

      <div class="form-group">
        <label for="alamatWali">Alamat Wali</label>
        <textarea 
          id="alamatWali"
          placeholder="Masukkan alamat wali" 
          bind:value={alamatWali}
        ></textarea>
      </div>

      <div class="form-group">
        <label for="kelas">Kelas<span>*</span></label>
		<select 
			id="kelas" 
			class="form-select"
			bind:value={selectedKelas}
			required>
			<option value="" disabled>Pilih Kelas</option>
			{#each daftarKelas as kelas}
				<option value={kelas.id}>{kelas.nama}</option>
			{/each}
		</select>
	  </div>

      <div class="form-group">
        <label for="foto-kk" class="form-label">
			Foto Kartu Keluarga<span>*</span>
		</label>
        <input 
          id="foto-kk"
		  class="form-control"
          type="file" 
		  accept="image/*"
			onchange={(e) => fotoKkFile = e.target.files[0] || null}
          required
        />
      </div>


      <div class="form-group">
        <label for="no-hp" class="form-label">
			Foto Akta Kelahiran<span>*</span>
		</label>
        <input 
          id="no-hp"
		  class="form-control"
          type="file" 
		  accept="image/*"
			onchange={(e) => fotoAkFile = e.target.files[0] || null}
          required
        />
      </div>


      <div class="form-group">
        <label for="no-hp" class="form-label">
			Pas Foto 3x4<span>*</span>
		</label>
        <input 
          id="no-hp"
		  class="form-control"
          type="file" 
		  accept="image/*"
			onchange={(e) => fotoPasFile = e.target.files[0] || null}
          required
        />
      </div>

	  <button type="submit" class="btn" disabled={isSubmitting}>
		{isSubmitting ? 'Sedang Mengirim...' : 'Kirim Pendaftaran'}
      </button>
        
      {#if errorMessage}
          <div class="alert alert-danger mb-3">{errorMessage}</div>
      {/if}

    </form>
  </div>

  <!-- INFORMASI TAMBAHAN -->
  <div class="card info-box">
    <h2>Informasi Tambahan</h2>
    <p>
      Setelah mengirimkan formulir, admin kami akan menghubungi Anda dalam 1-2 hari kerja untuk konfirmasi dan jadwal tes mengaji.
    </p>
    <br />
    <p>
      Untuk informasi lebih lanjut, hubungi:
      <b>+62 XXX XXXX XXXX</b>
    </p>
  </div>
</div>

<!-- FOOTER -->
<footer>
  <div class="footer-container">
    <div class="footer-box">
      <h3>TPA Ar-Rahmah</h3>
      <p>Tempat Pendidikan Al-Qur'an yang berkomitmen membentuk generasi Qurani</p>
    </div>

    <div class="footer-box">
      <h3>Lokasi</h3>
      <p>
        Ds. XYZ No.45 RT 02/03,<br />
        Indonesia
      </p>
    </div>

    <div class="footer-box">
      <h3>Jam Belajar</h3>
      <p>
        Senin - Jumat<br />
        Sore 15.30 - 17.00
      </p>
    </div>
  </div>
</footer>

<style>
  .container {
    max-width: 850px;
    margin: 50px auto;
    padding: 0 20px;
  }

  .title {
    text-align: center;
    margin-bottom: 30px;
  }

  .title h1 {
    color: #4c8b2b;
    font-size: 42px;
    margin-bottom: 10px;
  }

  .title p {
    color: #666;
    font-size: 15px;
  }

  .card {
    background-color: white;
    border: 1px solid #ccc;
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 25px;
  }

  .card h2 {
    color: #4c8b2b;
    margin-bottom: 18px;
    font-size: 34px;
  }

  .card ul {
    padding-left: 20px;
    color: #555;
    line-height: 1.8;
  }

  .form-group {
    margin-bottom: 20px;
  }

  .form-group label {
    display: block;
    margin-bottom: 8px;
    font-size: 14px;
    font-weight: bold;
    color: #444;
  }

  .form-group span {
    color: red;
  }

  input,
  textarea {
    width: 100%;
    padding: 13px;
    border: 1px solid #ccc;
    border-radius: 6px;
    outline: none;
    transition: 0.3s;
  }

  input:focus,
  textarea:focus {
    border-color: #4c8b2b;
  }

  textarea {
    min-height: 100px;
    resize: vertical;
  }

	/*
  .upload-box {
    border: 1px solid #ccc;
    border-radius: 8px;
    padding: 30px;
    text-align: center;
    color: #777;
  }

  .upload-icon {
    font-size: 40px;
    margin-bottom: 10px;
  }

  .upload-box input {
    border: none;
  }

  .upload-text {
    margin-top: 10px;
    font-size: 13px;
  }

  .file-selected {
    color: #2f7d1f;
    font-weight: bold;
  }
	*/

  .btn {
    width: 100%;
    background-color: #2f7d1f;
    color: white;
    border: none;
    padding: 14px;
    border-radius: 6px;
    cursor: pointer;
    font-weight: bold;
    transition: 0.3s;
  }

  .btn:hover {
    background-color: #256318;
  }

  .info-box {
    background-color: #e9eef5;
  }

  .info-box h2 {
    color: #222;
  }

  .info-box p {
    color: #555;
    line-height: 1.7;
  }

  .info-box b {
    color: black;
  }

  footer {
    background-color: #1f2937;
    color: white;
    padding: 35px 50px;
    margin-top: 50px;
  }

  .footer-container {
    display: flex;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 30px;
  }

  .footer-box h3 {
    margin-bottom: 12px;
  }

  .footer-box p {
    color: #d1d5db;
    font-size: 14px;
    line-height: 1.7;
  }

  @media (max-width: 768px) {
		/*
    .navbar {
      flex-direction: column;
      gap: 15px;
    }

    .menu {
      flex-wrap: wrap;
      justify-content: center;
    }
		*/

    .title h1 {
      font-size: 30px;
    }

    .card h2 {
      font-size: 26px;
    }

    .footer-container {
      flex-direction: column;
    }
  }
</style>
