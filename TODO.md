```
$ grep -Rn "TODO:" . \
    --exclude-dir="node_modules" \
    --exclude-dir=".venv" \
    --exclude-dir=".git" \
    --exclude-dir="build" \
    --exclude="TODO.md"
./frontend/src/routes/(public)/login/+page.svelte:55:   <!-- TODO: Login form is not same with the design -->
./frontend/src/routes/(public)/login/+page.svelte:79:                           <!-- TODO: "Ingat Saya" is not working -->
./frontend/src/routes/(public)/pendaftaran/+page.svelte:3:  // TODO: use $state()
./frontend/src/routes/(protected)/pengajar/Header.svelte:6:     // TODO: change icons to Lucide
./frontend/src/routes/(protected)/bendahara/Header.svelte:5:    // TODO: Use Lucide Icons
```

- (HIGH) Add security for auth
- (HIGH) Add RBAC
- (LOW) Add all DB tables
- (LOW) Use bootstrap for frontend
