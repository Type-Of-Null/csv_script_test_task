from src.service.operate_csv import OperateCSV
from src.service.operate_data import OperateData


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


def main() -> None:
    print(load_and_process_data(["data/economic1.csv", "data/economic2.csv"]))


if __name__ == "__main__":
    main()
