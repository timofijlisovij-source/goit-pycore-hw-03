from datetime import datetime
date = input("enter the date:")
date_value = datetime.strptime(date,"%Y-%m-%d")
Now= datetime.now()
days = (Now.toordinal())-(date_value.toordinal())
print(days)