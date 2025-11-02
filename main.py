from helper.get_data import getPokemonData
from helper.transform import transformData
from helper.load import saveCsv

def main():
    print("=== MULAI PROSES ETL POKEMON ===")
    data = getPokemonData(limit=20)
    transformed = transformData(data)
    saveCsv(transformed)
    print("=== ETL SELESAI ===")

if __name__ == "__main__":
    main()
