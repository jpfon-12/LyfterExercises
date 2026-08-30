# Suponga la función.
# Cree un test que:
# Use unittest.mock para simular el contenido de un archivo
# Verifique que retorna las líneas esperadas sin crear archivos reales
# Compruebe que lanza FileNotFoundError si el archivo no existe


def read_lines(path):
    with open(path, 'r') as f:
        return f.readlines()