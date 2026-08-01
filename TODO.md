```
$ grep -Rn "TODO:" . \
    --exclude-dir="node_modules" \
    --exclude-dir=".venv" \
    --exclude-dir=".git" \
    --exclude-dir="build" \
    --exclude-dir=".svelte-kit" \
    --exclude="TODO.md" \
    --exclude="*.bak"
./frontend/src/routes/(public)/login/+page.svelte:105:                                  <!-- TODO: Add see password -->
./frontend/src/routes/(public)/login/+page.svelte:114:                          <!-- TODO: "Ingat Saya" is not working -->
./frontend/src/routes/(public)/pendaftaran/+page.svelte:19:  // TODO: Add Uploading files
./frontend/src/routes/(protected)/pengajar/Header.svelte:9:     // TODO: change icons to Lucide
./frontend/src/routes/(protected)/pengajar/Header.svelte:49:                            <!-- TODO: Add user icon -->
./frontend/src/routes/(protected)/pengajar/absensi/+page.svelte:102:                    // TODO: check if siswa is active
./frontend/src/routes/(protected)/pengajar/penilaian/+page.svelte:97:   // TODO: Remove this unused code
./frontend/src/routes/(protected)/admin/users/add/+page.svelte:10:      // TODO: add kelas_id when user select role "Pengajar"
./frontend/src/routes/(protected)/admin/kelola-calon-siswa/+page.svelte:64:     /* TODO: Add edit page for pendaftaran siswa
./frontend/src/routes/(protected)/admin/Header.svelte:9:        // TODO: change icons to Lucide
./frontend/src/routes/(protected)/admin/+page.svelte:56:<!-- TODO: Auth checking not is actually checking -->
./frontend/src/routes/(protected)/bendahara/Header.svelte:8:    // TODO: Use Lucide Icons
```
- (HIGH) Add feature upload image to cloudinary
- (HIGH) Add column `mengajar` in table `pengajar` 
    for assigning to what class
- (HIGH) If the class is just for monday, then presence must just for monday
- (MED) Add Detail button for every row table
- (MED) Remove kelas field in pendaftaran page
- (MED) What the difference between "Nama Pencatatan" dan "Catatan"
- (MED) Add Backup automation
- (MED) Change `os.getenv()` to Pydantic settings in `config.py` 
- (LOW) rename auth.py to user.py
- (LOW) Check console log, maybe there are debug message
- (LOW) Change name `PUBLIC_FRONTEND_BASE_URL` to `PUBLIC_FE_BASE_URL` in .env
