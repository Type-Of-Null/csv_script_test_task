import pytest

from src.service.operate_csv import OperateCSV
from src.service.operate_data import OperateData


def test_reader_csv_reads_file(sample_csv_files):
    paths = sample_csv_files
    data = OperateCSV.reader_csv(paths[0])

    # Проверяем, что результат - список
    assert isinstance(data, list)
    # Проверяем, что прочитано 3 строки данных (без заголовка)
    assert len(data) == 3
    # Проверяем, что в каждой строке есть нужные колонки
    assert "country" in data[0]
    assert "gdp" in data[0]


def test_average_and_sorting(sample_csv_files):
    paths = sample_csv_files
    all_data = []

    for p in paths:
        all_data.extend(OperateCSV.reader_csv(p))

    # Рассчитываем средний ВВП для каждой страны
    avg = OperateData.average_gdp(all_data)

    # Проверяем правильность расчётов:
    # Russia: (100+200+300)/3 = 200.0
    # Belarus: (150+50)/2 = 100.0
    assert avg.get("Russia") == pytest.approx(200.0)
    assert avg.get("Belarus") == pytest.approx(100.0)

    # Тест сортировки по убыванию
    sorted_gdp = OperateData.sorting_gdp_desc(avg)

    # Преобразуем в список пар (страна, ВВП) для проверки
    items = list(sorted_gdp.items())

    # Проверяем порядок сортировки:
    assert items[0][0] == "Russia"
    assert items[0][1] == pytest.approx(200.0)
    assert items[1][0] == "Belarus"
