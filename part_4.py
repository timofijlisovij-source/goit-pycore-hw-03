from datetime import datetime, date, timedelta
users = [
    {"name": "John Doe", "birthday": "1985.02.16"},
    {"name": "Jane Smith", "birthday": "1990.05.27"}
]   
upcoming_birthdays = []
def get_upcoming_birthdays(users):
    today = datetime.today().date()
    for user in users: 
        birthday_date = datetime.strptime(user["birthday"],"%Y.%m.%d").date()
        birthday_this_year = birthday_date.replace(year=today.year)
        if birthday_this_year < today :
            birthday_this_year = birthday_this_year.replace(year=today.year+1)    
        days = birthday_this_year.toordinal() - today.toordinal()
        if days < 8:
            if birthday_this_year.weekday() == 5 :
                    congratulation_date = birthday_this_year + timedelta(days=2) 
            elif birthday_this_year.weekday() == 6 :
                    congratulation_date = birthday_this_year + timedelta(days=1) 
            else :
                    congratulation_date = birthday_this_year
            upcoming_birthdays.append({
              "name": user["name"],
              "congratulation_day": congratulation_date.strftime("%Y.%m.%d")
        })
    return upcoming_birthdays

            
         
print(get_upcoming_birthdays(users))