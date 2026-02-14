import re
def normalize_phone (phone_number):
    pattern = r"\D+"
    clean_number = re.sub(pattern,"",phone_number)
    if clean_number.startswith("38"):
        return f"+{clean_number}"
    else :
        return f"+38{clean_number}"
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]
    
for num in raw_numbers:
    print(normalize_phone(num))



