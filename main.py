cyrrilyc_alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
text = 'варенник'

cyrrilyc_alpha_dict = dict(enumerate(cyrrilyc_alpha, 1))
cyrrilyc_alpha_dict = {v: k for k, v in cyrrilyc_alpha_dict.items()}

result = ''
for c in text:
    result += str(cyrrilyc_alpha_dict.get(c))
print(result)