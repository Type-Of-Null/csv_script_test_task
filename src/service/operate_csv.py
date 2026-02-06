import csv
from pathlib import Path


class OperateCSV:

    @staticmethod
    def reader_csv(file_path: str) -> list[dict[str, str]]:
        data = []
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл по указанному пути: {file_path} не найден")

        with open(path, "r", encoding="utf-8", newline="") as file:
            try:
                sample = file.read(1024)
                if not sample:
                    raise ValueError("В файле отсутствуют данные")
            except Exception as e:
                raise RuntimeError(f"Ошибка {e}. Невозможно прочитать файл")
            file.seek(0)
            dialect = csv.Sniffer().sniff(sample)
            reader = csv.DictReader(file, dialect=dialect)
            if reader.fieldnames is None:
                raise ValueError(f"В файле {file_path} нет заголовков")

            for row in reader:
                data.append(row)

        return data
