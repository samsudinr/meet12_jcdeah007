import os

def saveCsv(df, nameFile="output/data_pokemon.csv"):

    os.makedirs(os.path.dirname(nameFile), exist_ok=True)

    df.to_csv(nameFile, index=False)
    
    print(f"Data disimpan ke {os.path.abspath(nameFile)}")