import pandas as pd

def transformData(data_pokemon):
    # ubah ke bentuk tabel (DataFrame)
    tabel = pd.DataFrame(data_pokemon)

    # ubah tinggi dari decimeter ke meter
    tabel["tinggi_meter"] = tabel["tinggi"] / 10

    # ubah berat dari hectogram ke kilogram
    tabel["berat_kg"] = tabel["berat"] / 10

    # pilih kolom yang mau disimpan
    tabel_bersih = tabel[["nama", "tipe_1", "tipe_2","tinggi_meter", "berat_kg", "exp"]]
    
    return tabel_bersih