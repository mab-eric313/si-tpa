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
  let daftarKelas = $state({});
  let selectedKelas = $state('');
  let fotoKk = $state('');
  let fotoAk = $state('');
  let fotoPas = $state('');

  // TODO: Add Uploading files
  // let files = $state(null);

	let errorMessage = $state('');
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
		}
	});

	let payload = $derived({
		nama_siswa: namaSantri,
		status: "Pending",
		jenis_kelamin_siswa: jenisKelamin,
		tanggal_lahir_siswa: tanggalLahir,
		alamat_siswa: alamatSantri,
		nama_wali: namaWali,
		no_hp_wali: noHp,
		alamat_wali: alamatWali,
		kelas_id: selectedKelas,
		foto_kk: fotoKk,
		foto_ak: fotoAk,
		foto_pas: fotoPas,
	});

  // Fungsi untuk menangani pengiriman form
  async function handleSubmit() {
    // Validasi sederhana (karena semua field wajib diisi)
    if (!namaSantri || !jenisKelamin || !tanggalLahir || !namaWali || !kelas) {
      alert('Mohon lengkapi semua data yang wajib diisi (*).');
      return;
    }

		try {
			const res = await fetch(`${PUBLIC_API_BASE_URL}/pendaftaran-siswa/`, {
				method: "POST",
				headers: { "Content-Type": "application/json" },
				body: JSON.stringify(payload)
			});
			if (!res.ok) throw new Error(res.statusText);

			daftarKelas = await res.json();
		} catch (error) {
			console.error(error);
		}

    const formData = {
      namaSantri,
	  jenisKelamin,
      tanggalLahir,
      alamatSantri,
      namaWali,
      noHp,
      alamatWali,
      selectedKelas,
  	  fotoKk,
  	  fotoAk,
  	  fotoPas,
    };

    console.log('Data pendaftaran berhasil dikirim:', formData);
    alert('Pendaftaran berhasil dikirim! Admin akan segera menghubungi Anda.');
    
    // Reset form setelah sukses
    resetForm();
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
    fotoKk = '';
    fotoAk = '';
    fotoPas = '';
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
	  <li>Masukkan foto-foto yang dibutuhkan ke dalam Google Drive</li>
	  <ul>
		  <li>Foto Kartu Keluarga</li>
		  <li>Foto Akta Kelahiran</li>
		  <li>Pas foto ukuran 3x4</li>
	  </ul>
	  <li>Kemudian salin link foto-foto tersebut lalu masukkan ke dalam form yang sesuai</li>
    </ul>
  </div>

  <!-- FORM PENDAFTARAN -->
  <div class="card">
    <h2>Form Pendaftaran</h2>

    <form>
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
			bind:value={selectedKelas}>
			{#each daftarKelas as kelas}
				<option value={kelas.id}>{kelas.nama}</option>
			{/each}
		</select>
	  </div>

      <div class="form-group">
        <label for="no-hp">Foto Kartu Keluarga<span>*</span></label>
        <input 
          id="no-hp"
          type="text" 
          placeholder="Masukkan link foto Kartu Keluarga" 
          bind:value={fotoKk}
          required
        />
      </div>


      <div class="form-group">
        <label for="no-hp">Foto Akta Kelahiran<span>*</span></label>
        <input 
          id="no-hp"
          type="text" 
          placeholder="Masukkan link foto Akta Kelahiran" 
          bind:value={fotoAk}
          required
        />
      </div>


      <div class="form-group">
        <label for="no-hp">Pas Foto 3x4<span>*</span></label>
        <input 
          id="no-hp"
          type="text" 
          placeholder="Masukkan link pas foto 3x4" 
          bind:value={fotoPas}
          required
        />
      </div>

	  <button type="submit" class="btn" onclick={handleSubmit}>
        Kirim Pendaftaran
      </button>
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
