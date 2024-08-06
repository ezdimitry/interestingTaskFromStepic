'''
Проверка на автомобильный номер. На вход программе подаётся одна строка – сгенерированный ИИ автомобильный номер.
Напишите программу, которая принимает на вход строку и проверяет, является ли эта строка корректным автомобильным номером.
Программа должна вывести «YES» (без кавычек), если искусственный интеллект справился со своей задачей, или «NO» (без кавычек) в противном случае.
В нашей задаче корректным автомобильным номером будем считать следующие форматы:
<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА>
<БУКВА><ЦИФРА><ЦИФРА><ЦИФРА><БУКВА><БУКВА>_<ЦИФРА><ЦИФРА><ЦИФРА>
'''
license_plate = input()
is_valid = 'NO'
allowed_letters = 'АВЕКМНОРСТУХ'
if 9 <= len(license_plate) <= 10:
    letters_part = license_plate[0] + license_plate[4:6]
    digits_part = license_plate[1:4] + license_plate[7:]
    underscore_part = license_plate[6]
    if digits_part.isdigit() and underscore_part == "_":
        is_valid = 'YES'
    for char in letters_part:
        if char not in allowed_letters:
            is_valid = 'NO'
print(is_valid)