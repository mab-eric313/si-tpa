```
$ grep -Rn "TODO:" . \
    --exclude-dir="node_modules" \
    --exclude-dir=".venv" \
    --exclude-dir=".git" \
    --exclude-dir="build" \
    --exclude="TODO.md"
./frontend/src/routes/(public)/login/+page.svelte:74:   <!-- TODO: Login form is not same with the design -->
./frontend/src/routes/(public)/login/+page.svelte:98:                           <!-- TODO: "Ingat Saya" is not working -->
./frontend/src/routes/(public)/pendaftaran/+page.svelte:3:  // TODO: use $state()
./frontend/src/routes/(protected)/pengajar/Header.svelte:7:     // TODO: change icons to Lucide
./frontend/src/routes/(protected)/pengajar/Header.svelte:47:                            <!-- TODO: Add user icon -->
./frontend/src/routes/(protected)/pengajar/kelas/+page.svelte.bak:107:                          <!-- TODO: Change this and take the data from kelas table -->
./frontend/src/routes/(protected)/pengajar/kelas/+page.svelte.bak:190:                          <!-- TODO: The table is not same with the design -->
./frontend/src/routes/(protected)/pengajar/kelas/+page.svelte.bak:219:                                                                  <!-- TODO: Delete currenlty is not working -->
./frontend/src/routes/(protected)/pengajar/+page.svelte:1:<!-- TODO: All '...' is need to take data from database -->
./frontend/src/routes/(protected)/admin/kelola-pengguna/+page.svelte:10:                        // TODO: change hardcoded url. Make URL variable placed in $lib dir
./frontend/src/routes/(protected)/admin/users/add/+page.svelte:8:       // TODO: add kelas_id when user select role "Pengajar"
./frontend/src/routes/(protected)/admin/Header.svelte:7:        // TODO: change icons to Lucide
./frontend/src/routes/(protected)/admin/+page.svelte:11:                        // TODO: change hardcoded url. Make URL variable placed in $lib dir
./frontend/src/routes/(protected)/admin/+page.svelte:27:                        // TODO: change hardcoded url. Make URL variable placed in $lib dir
./frontend/src/routes/(protected)/bendahara/Header.svelte:5:    // TODO: Use Lucide Icons

```
- (MED) Change all static data in pengajar beranda page
- (MED) Add or change header for pengajar and admin page
- (LOW) rename auth.py to user.py
- (LOW) Check console log, maybe there are debug message
