import csv

def read_shows(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        # lines = file.readlines()
        # for number, line in enumerate(lines, start=1):
        #     print(f"Line {number}: {line.strip()}")

        reader = csv.DictReader(file)
        for show in reader:
            print(f"Serie: {show['Name']}")
            print(f"Genero: {show['Genre']}")
            print(f"Numero de episodios: {show['Episodes']}")
            print(f"Plataforma: {show['Platform']}")
            print("\n")
        
        
            

def main():
    read_shows('shows.csv')


main() 