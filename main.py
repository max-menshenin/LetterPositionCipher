CYRRILYC_ALPHA = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = 'варенник'

CYRRILYC_ALPHA_DICT = dict(enumerate(CYRRILYC_ALPHA, 1))
CYRRILYC_ALPHA_DICT = {v: k for k, v in CYRRILYC_ALPHA_DICT.items()}

result = ' '
for c in text:
    result += ' ' + str(CYRRILYC_ALPHA_DICT.get(c))
print(result)