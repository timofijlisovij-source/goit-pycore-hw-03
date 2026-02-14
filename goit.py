from datetime import datetime
def get_days_from_today(date):
    try:
        date_value = datetime.strptime(date,"%Y-%m-%d")
        Now= datetime.now()
        days = (Now.toordinal())-(date_value.toordinal())
        return days
    except ValueError:
        return "invalid data format"
print(get_days_from_today("2010-12-5"))