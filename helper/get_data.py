import requests 
# -----------------------
# LANGKAH 1: AMBIL DATA
# -----------------------
def getPokemonData(limit=10):
    # URL API pokemon
    api = f"https://pokeapi.co/api/v2/pokemon?limit={limit}"
    
    # ambil data dari internet
    respon = requests.get(api)
    data_json = respon.json()

    hasil = data_json["results"]
    
    semua_pokemon = []
    
    # loop setiap pokemon untuk ambil detailnya
    for i in hasil:
        detail_url = i["url"]
        detail = requests.get(detail_url).json()

        l_types = detail["types"]

        # cek apakah pokemon punya 2 tipe atau tidak

        if len(l_types) < 2:
            tipe1 = l_types[0]["type"]["name"]
            tipe2 = None
        else:
            tipe1 = l_types[0]["type"]["name"]
            tipe2 = l_types[1]["type"]["name"]

        
        # ambil beberapa informasi penting
        info = {
            "nama": detail["name"],
            "tinggi": detail["height"],
            "berat": detail["weight"],
            "exp": detail["base_experience"],
            "tipe_1": tipe1,
            "tipe_2": tipe2
        }
        semua_pokemon.append(info)
    
    return semua_pokemon
