# SI-TPA — Sistem Informasi Taman Pendidikan Al Quran
Information System Website with Svelte and FastAPI

# Tech Stack
- Frontend: Svelte
- Backend: FastAPI
- Database: Mariadb, SQLAlchemy (ORM), Alembic (Migration)

# Application Access
- FastAPI: `http://localhost:8000/`
- FastAPI Docs: `http://localhost:8000/docs`
- Svelte: `http://localhost:5173/`

# Project Structure
```
$ tree -a --gitignore -F --dirsfirst -I .git -I .vscode
./
├── backend/
│   ├── app/
│   │   ├── alembic/
│   │   │   ├── versions/
│   │   │   ├── env.py
│   │   │   ├── README
│   │   │   └── script.py.mako
│   │   ├── routers/
│   │   │   ├── kelas.py
│   │   │   ├── siswa.py
│   │   │   └── wali.py
│   │   ├── tests/
│   │   │   ├── data.py
│   │   │   └── __init__.py
│   │   ├── app.py
│   │   ├── database.py
│   │   ├── errors.py
│   │   ├── __init__.py
│   │   ├── models.py
│   │   └── schemas.py
│   ├── config.py
│   ├── __init__.py
│   └── main.py
├── frontend/
│   ├── src/
│   │   ├── routes/
│   │   │   ├── (protected)/
│   │   │   │   ├── admin/
│   │   │   │   ├── bendahara/
│   │   │   │   │   ├── laporan/
│   │   │   │   │   │   └── +page.svelte
│   │   │   │   │   ├── pemasukan/
│   │   │   │   │   │   └── +page.svelte
│   │   │   │   │   ├── pengeluaran/
│   │   │   │   │   │   └── +page.svelte
│   │   │   │   │   ├── Header.svelte
│   │   │   │   │   ├── layout.css
│   │   │   │   │   ├── +layout.svelte
│   │   │   │   │   └── +page.svelte
│   │   │   │   └── pengajar/
│   │   │   │       ├── absensi/
│   │   │   │       │   ├── +page.js
│   │   │   │       │   └── +page.svelte
│   │   │   │       ├── ajukan-pergantian/
│   │   │   │       │   ├── +page.js
│   │   │   │       │   └── +page.svelte
│   │   │   │       ├── kelas/
│   │   │   │       │   ├── +page.js
│   │   │   │       │   └── +page.svelte
│   │   │   │       ├── rekap-absensi/
│   │   │   │       │   ├── +page.js
│   │   │   │       │   └── +page.svelte
│   │   │   │       ├── rekap-nilai/
│   │   │   │       │   ├── +page.js
│   │   │   │       │   └── +page.svelte
│   │   │   │       ├── Header.svelte
│   │   │   │       ├── layout.css
│   │   │   │       ├── +layout.svelte
│   │   │   │       └── +page.svelte
│   │   │   └── (public)/
│   │   │       ├── login/
│   │   │       │   └── +page.svelte
│   │   │       ├── pendaftaran/
│   │   │       │   └── +page.svelte
│   │   │       ├── Header.svelte
│   │   │       ├── +layout.svelte
│   │   │       └── +page.svelte
│   │   └── app.html
│   └── static/
│       └── robots.txt
├── references/                     # Stores ERD diagrams and website designs
│   ├── images/
│   │   └── ss-dashboard_design.png
│   ├── erd_diagram.mwb
│   ├── erd_diagram.pdf
│   └── erd_diagram.png
├── alembic.ini
├── .env.example
├── .gitignore
├── jsconfig.json
├── .npmrc
├── package.json
├── package-lock.json
├── poetry.lock
├── pyproject.toml
├── README.md
├── svelte.config.js
├── TODO.md
└── vite.config.js

```

## How to Setup
1. Clone this repository
    ```sh
    git clone https://github.com/mab-eric313/si-tpa.git
    cd si-tpa
    ```  

2. Make virtual environment  

    **Windows**  
    Open the code editor or command prompt  
    ```cmd
    python -m venv .venv
    .\.venv\Scripts\activate
    ```
      
    **Linux**
    ```sh
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3. Install FastAPI dependencies

    Using pip
    ```sh
    pip install .
    ```

    or using poetry
    ```sh
    # Make sure poetry is installed in your system
    poetry install --no-root
    ```

4. Install Svelte dependencies  

    ```sh
    npm install
    ```

5. Setup .env  

    Use your text editor to create `.env` file
    ```
    DB_USER=your_pc_username
    DB_HOST=localhost
    DB_PORT=3306
    DB_NAME=si-tpa
    ```

6. Run the project

    ```sh
    npm run dev:all
    ```

