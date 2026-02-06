from collections import defaultdict


class OperateData:

    @staticmethod
    def average_gdp(data: list[dict[str, str]]) -> dict[str, float]:
        country_gdps = defaultdict(list)
        for row in data:
            _country = row.get("country")
            _gdp = row.get("gdp")
            if _country and _gdp:
                try:
                    country_gdps[_country].append(float(_gdp))
                except (ValueError, TypeError):
                    continue
        avg_gdps = {
            country: sum(gdps) / len(gdps)
            for country, gdps in country_gdps.items()
            if gdps
        }
        return avg_gdps

    @staticmethod
    def sorting_gdp_desc(data: dict[str, float]) -> dict[str, float]:
        sorted_items = sorted(data.items(), key=lambda x: x[1], reverse=True)
        return dict(sorted_items)
