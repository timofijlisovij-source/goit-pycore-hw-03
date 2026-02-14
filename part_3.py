import re
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



