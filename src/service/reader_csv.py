import csv
from pathlib import Path
from typing import Dict, Any, List


def reader_csv(file_path: str) -> List[Dict[str, Any]]:
    data = []
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Файл по указанному пути: {file_path} не найден")

    with open(path, "r", encoding="utf-8", newline="") as file:
        sample = file.read(1024)
        file.seek(0)
        dialect = csv.Sniffer().sniff(sample)
        reader = csv.DictReader(file, dialect=dialect)
        if reader.fieldnames is None:
            raise ValueError(f"В файле {file_path} нет заголовков")

        for row in reader:
            data.append(row)

    return data
