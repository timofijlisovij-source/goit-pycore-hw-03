from datetime import datetime


def get_days_from_today(date: str) -> int | str:
    try:
        date_value = datetime.strptime(date, "%Y-%m-%d")
        now = datetime.now()
        days = now.toordinal() - date_value.toordinal()
        return days
    except ValueError:
        return "invalid data format"


if __name__ == "__main__":
    print(get_days_from_today("2010-12-5"))
