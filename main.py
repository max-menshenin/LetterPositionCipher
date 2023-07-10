CYRRILYC_ALPHA = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
input_raw = input("Введите текст: " )

CYRRILYC_ALPHA_DICT = dict(enumerate(CYRRILYC_ALPHA, 1))
CYRRILYC_ALPHA_DICT = {v: k for k, v in CYRRILYC_ALPHA_DICT.items()}

result = ''
for c in input_raw:
    result += ''.join(str(CYRRILYC_ALPHA_DICT.get(c))) + ' '
print(result[:-1])
