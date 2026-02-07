import pytest


@pytest.fixture
def sample_csv_files(tmp_path):

    # Тестовые данные в формате CSV
    csv1 = """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
Russia,2025,100,0,0,0,1,X
Russia,2024,200,0,0,0,1,X
Belarus,2023,150,0,0,0,1,X
"""

    csv2 = """country,year,gdp,gdp_growth,inflation,unemployment,population,continent
Russia,2021,300,0,0,0,1,X
Belarus,2023,50,0,0,0,1,X
"""
    # Временные файлы
    f1 = tmp_path / "file1.csv"
    f1.write_text(csv1, encoding="utf-8")

    f2 = tmp_path / "file2.csv"
    f2.write_text(csv2, encoding="utf-8")

    return [str(f1), str(f2)]
