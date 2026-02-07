import argparse
import sys
from tabulate import tabulate

from src.service.operate_csv import OperateCSV
from src.service.operate_data import OperateData


# Загрузка и обработка CSV файлов
def load_and_process_data(file_paths: list[str]) -> dict[str, float]:
    all_data = []

    for file_path in file_paths:
        try:
            data = OperateCSV.reader_csv(file_path)
            all_data.extend(data)
        except (FileNotFoundError, ValueError, RuntimeError) as e:
            print(f"Ошибка обработки файла. {e}")
            continue

    avg_gdp = OperateData.average_gdp(all_data)
    sorted_gdp = OperateData.sorting_gdp_desc(avg_gdp)

    return sorted_gdp


# Вывод отчета в консоль
def display_report(report_name: str, data: dict[str, float]) -> None:
    table_data = [[country, gdp] for country, gdp in data.items()]
    headers = ["country", "gdp"]

    print(f"\n Отчет {report_name}")
    print(tabulate(table_data, headers=headers, tablefmt="outline", floatfmt=".2f"))
    print()


# Точка входа в приложение
def main() -> None:

    parser = argparse.ArgumentParser(
        description="Обработка csv файлов и генерация отчетов"
    )
    parser.add_argument(
        "--files",
        nargs="+",
        required=True,
        help="CSV файлы для обработки",
    )
    parser.add_argument(
        "--report",
        choices=["average-gdp"],
        default="average-gdp",
        help="Вид отчета",
    )

    args = parser.parse_args()

    # Выбор логики в зависимости от типа отчета
    # При масштабировании можно добавлять необходимую реализацию
    if args.report == "average-gdp":
        data = load_and_process_data(args.files)
        display_report(args.report, data)
    else:
        print(f"Неправильный тип отчета: {args.report}")
        sys.exit(1)


if __name__ == "__main__":
    main()
