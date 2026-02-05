import csv

import pytest

from src.service.reader_csv import reader_csv


# Тест на наличие ошибки при отсутствии файла
def test_file_not_found():
    with pytest.raises(FileNotFoundError, match="Файл по указанному пути"):
        reader_csv("path/to_file/file.csv")


# Тест на наличие ошибки при пустом файле
def test_reader_csv_empty_file(tmp_path):

    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")

    with pytest.raises(csv.Error):
        reader_csv(str(empty_file))
