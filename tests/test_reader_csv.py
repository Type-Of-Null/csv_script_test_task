import pytest

from src.service.operate_csv import OperateCSV


# Тест на наличие ошибки при отсутствии файла
def test_reader_csv_file_not_found():
    with pytest.raises(FileNotFoundError, match="не найден"):
        OperateCSV.reader_csv("path/to_file/file.csv")


# Тест на наличие ошибки при пустом файле
def test_reader_csv_empty_file(tmp_path):

    empty_file = tmp_path / "empty.csv"
    empty_file.write_text("")

    with pytest.raises(ValueError):
        OperateCSV.reader_csv(str(empty_file))
