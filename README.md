# SI-TPA — Sistem Informasi Taman Pendidikan Al Quran
Information System Website with Svelte and FastAPI

## Tech Stack
- Frontend: Svelte
- Backend: FastAPI
- Database: Mariadb, SQLAlchemy (ORM), Alembic (Migration)

## Application Access
- FastAPI: `http://localhost:8000/`
- FastAPI Docs: `http://localhost:8000/docs`
- Svelte: `http://localhost:5173/`

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

   Make sure openssl is installed in your system. If you have not installed it,  
   for Windows visit the website: [Win32 OpenSSL](https://slproweb.com/products/Win32OpenSSL.html)  

   Generate secret key:
   ```
   openssl rand -hex 32
   ```

   Use your text editor to create `.env` file
   ```
   DB_USER=your_pc_username
   DB_HOST=localhost
   DB_PORT=3306
   DB_NAME=si_tpa

   SECRET_KEY=openssl_generate_key
   ```

7. Run the project

    ```sh
    npm run dev:all
    ```


