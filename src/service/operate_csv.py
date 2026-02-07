import csv
from pathlib import Path


class OperateCSV:

    @staticmethod
    def reader_csv(file_path: str) -> list[dict[str, str]]:
        data = []
        path = Path(file_path)
        if not path.exists():
            raise FileNotFoundError(f"Файл {file_path} не найден")

        with open(path, "r", encoding="utf-8", newline="") as file:
            # Считываем 1024 символа для определения диалекта
            try:
                sample = file.read(1024)
            except Exception as e:
                raise RuntimeError(f"Ошибка чтения файла {file_path}: {e}")
            file.seek(0)

            # Распознаем полученные данные
            try:
                sniffer = csv.Sniffer()
                dialect = sniffer.sniff(sample)
                reader = csv.DictReader(file, dialect=dialect)
                has_header = sniffer.has_header(sample)
            except csv.Error:
                raise ValueError(f"Файл {file_path} не является csv файлом")

            # Проверка наличия заголовков
            if not has_header:
                raise ValueError(f"В файле {file_path} нет заголовков")

            # Пропуск пустых строк
            for row in reader:
                if row:
                    data.append(row)

            # Проверка наличия данных
            if not data:
                raise ValueError(
                    f"Файл {file_path} не содержит данных (только заголовки): "
                )

        return data
