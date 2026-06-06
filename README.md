# SI-TPA — Sistem Informasi Taman Pendidikan Al Quran
Information System Website with Svelte and FastAPI

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
```cmd
pip install -r requirements.txt
```

4. Install Svelte dependencies
```sh
npm install
```

5. Setup .env
Create `.env` file
```sh
DB_USER=your_pc_username
DB_HOST=localhost
DB_PORT=3306
DB_NAME=si-tpa
```

5. Run the project
```
npm run dev:all
```

