import re

phone_numbers = """    067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   """

def normalize_phone(phone_number):
    digits = re.sub(r'\D', '', phone_number)

    if digits.startswith('380'):
        normalized = '+' + digits
    elif digits.startswith('0'):
        normalized = '+38' + digits
    elif digits.startswith('38'):
        normalized = '+' + digits
    else:
        normalized = '+38' + digits

    return normalized

lines = phone_numbers.strip().splitlines()
for line in lines:
    print(normalize_phone(line))
