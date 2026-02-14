import re
raw_numbers = [
    "067\\t123 4567",
"(095) 234-5678\\n",
"+380 44 123 4567",
"380501234567","    "
"+38(050)123-32-34",
"     0503451234",
"(050)8889900",
"38050-111-22-22",
"38050 111 22 11   "
]
def normalize_phone (num1):
    pattern = r"\D+"
    matches = re.sub(pattern,"",num1)

    match = re.search ("38",num1)
    if match :
        return (f"+{matches}") 
    else :
        return (f"+38{matches}")
for num in raw_numbers:
    print(normalize_phone(num))



