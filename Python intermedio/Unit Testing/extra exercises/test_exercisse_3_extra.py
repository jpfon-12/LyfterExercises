# Suponga la función.
# Cree un test que:
# Use unittest.mock para simular el contenido de un archivo
# Verifique que retorna las líneas esperadas sin crear archivos reales
# Compruebe que lanza FileNotFoundError si el archivo no existe


from exercise_3_extra import read_lines
from unittest.mock import patch, mock_open
import pytest


def test_read_lines_returns_expected_lines():
    content = "line1\nline2\nline3\n"
 
    with patch("exercise_3_extra.open", mock_open(read_data=content)) as mocked_open:
        result = read_lines("path.txt")
    assert result == ["line1\n", "line2\n", "line3\n"]
    mocked_open.assert_called_once_with("path.txt", "r")


def test_read_lines_raises_file_not_found():
    with patch("exercise_3_extra.open", side_effect=FileNotFoundError):
        with pytest.raises(FileNotFoundError):
            read_lines("path.txt")

