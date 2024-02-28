# Cara Menjalankan Aplikasi Secara Local

## Prerequisite
Anda harus sudah menginstal Python dan memasukkan Python dalam PATH environment variable Anda.

## Langkah-Langkah
1. Setup virtual environment jika belum dengan menggunakan `python -m venv env`.
2. Aktifkan virtual environment dengan command `.\env\Scripts\activate` pada Windows atau `source env/bin/activate` pada Linux atau MacOS.
3. Instal dependencies dan packages yang dibutuhkan dengan menggunakan command `pip install -r requirements.txt`.
4. Dengan asumsi Anda berada pada direktori utama, jalankan aplikasi Streamlit dengan menggunakan command `streamlit run .\dashboard\dashboard.py` dikarenakan `dashboard.py` ada di folder `dashboard`, bukan di root.
5. Aplikasi seharusnya sudah jalan.