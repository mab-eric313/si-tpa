```
$ grep -Rn "TODO:" . \
    --exclude-dir="node_modules" \
    --exclude-dir=".venv" \
    --exclude-dir=".git" \
    --exclude-dir="build" \
    --exclude="TODO.md" \
    --exclude="*.bak"
./frontend/src/routes/(public)/login/+page.svelte:132:                          <!-- TODO: "Ingat Saya" is not working -->
./frontend/src/routes/(public)/pendaftaran/+page.svelte:19:  // TODO: Add Uploading files
./frontend/src/routes/(protected)/pengajar/Header.svelte:9:     // TODO: change icons to Lucide
./frontend/src/routes/(protected)/pengajar/Header.svelte:49:                            <!-- TODO: Add user icon -->
./frontend/src/routes/(protected)/pengajar/+page.svelte:1:<!-- TODO: class schedule still static -->
./frontend/src/routes/(protected)/pengajar/absensi/+page.svelte:102:                    // TODO: check if siswa is active
./frontend/src/routes/(protected)/pengajar/penilaian/+page.svelte:97:   // TODO: Remove this unused code
./frontend/src/routes/(protected)/admin/users/add/+page.svelte:10:      // TODO: add kelas_id when user select role "Pengajar"
./frontend/src/routes/(protected)/admin/kelola-calon-siswa/+page.svelte:64:     /* TODO: Add edit page for pendaftaran siswa
./frontend/src/routes/(protected)/admin/Header.svelte:9:        // TODO: change icons to Lucide
./frontend/src/routes/(protected)/admin/kelola-siswa/+page.svelte:107:                          <!-- TODO: Change this and take the data from kelas table -->
./frontend/src/routes/(protected)/bendahara/Header.svelte:8:    // TODO: Use Lucide Icons
```
- (HIGH) Add column `mengajar` in table `pengajar` 
    for assigning to what class

- (MED) Remove kelas field in pendaftaran page
- (MED) What the difference between "Nama Pencatatan" dan "Catatan"
- (MED) Add comma in number field
- (MED) Add Backup automation
- (LOW) rename auth.py to user.py
- (LOW) Check console log, maybe there are debug message
- (LOW) Change name `PUBLIC_FRONTEND_BASE_URL` to `PUBLIC_FE_BASE_URL` in .env
