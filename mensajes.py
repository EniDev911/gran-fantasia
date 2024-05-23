import csv

def leer_dialogos(key:str) -> str:
    with open('dialogos.csv', encoding='utf-8') as f:
        csv_reader = csv.DictReader(f)
        dialogos = {row['Id']:row['Dialogo'] for row in csv_reader}

    return dialogos[key]

if __name__ == "__main__":
    print(leer_dialogos('principal'))