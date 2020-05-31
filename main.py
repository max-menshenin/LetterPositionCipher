cyrrilyc_alpha = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
cyrrilyc_alpha = {value: key for key, value in dict(enumerate(cyrrilyc_alpha, 1)).items()}

text = 'шляпа'
print("".join([str(cyrrilyc_alpha.get(x)) for x in text]))