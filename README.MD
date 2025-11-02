# Simple ETL Pokémon Data Project

## Deskripsi

Project ini adalah **mini ETL (Extract, Transform, Load)** sederhana menggunakan **Open API Pokémon (https://pokeapi.co/)**.  
Tujuannya untuk melatih dasar alur kerja seorang **Data Engineer** dalam memproses data dari sumber eksternal hingga menjadi dataset yang siap dianalisis.

Project ini dibangun dengan pendekatan modular:

-   **Extract:** Mengambil data Pokémon dari API.
-   **Transform:** Membersihkan dan mengubah format data (konversi satuan, pemilihan kolom penting).
-   **Load:** Menyimpan hasil akhir ke dalam file `.csv`.

---

## Tujuan Pembelajaran

Melalui project ini, peserta diharapkan memahami:

1. Cara melakukan _data extraction_ dari API publik.
2. Teknik sederhana untuk melakukan _data transformation_ menggunakan Pandas.
3. Proses _load_ hasil akhir ke format CSV.
4. Struktur ETL yang modular seperti praktik di dunia Data Engineering.

## Library Yang Dibutuhkan

library antara lain

-   **requests:** Mengambil data Pokémon dari API.
-   **pandas:** trasnform data Pokémon dari API dalam projek ini untuk melakukan normalisasi data emnjadi satuan meter dan kilogram.

Library dapat diinstal dengan cara mengekseskusi command berikut ini

pip install -r list_lib.txt.txt
