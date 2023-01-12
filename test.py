def aiv(let):
    if let == "א" or let == "ה" or let == "ו" or let == "י":
        return let


def itzurim(e):
    if e == 'ב' or e == 'ג' or e == 'ד' or e == 'ז' or e == 'ח' or e == 'ט' or e == 'כ' or e == 'ל' or e == 'מ' or e == 'נ' or e == 'ס' or e == 'ע' or e == 'פ' or e == 'צ' or e == 'ק' or e == 'ר' or e == 'ש' or e == 'ת' or e == 'ף' or e == 'ץ' or e == 'ם' or e == 'ן':
        return e


def sum_l(name_gimatriha):
    sum_letter = sum(name_gimatriha)
    while sum_letter > 9:
        sum_letter_name_list = [x for x in str(sum_letter)]
        sum_letter_name_map = map(int, sum_letter_name_list)
        sum_letter_name_convert_list = list(sum_letter_name_map)
        sum_letter = sum(sum_letter_name_convert_list)
    print(sum_letter)


def sum_num(numbers):
    while numbers > 9:
        sum_numbers_list = [x for x in str(numbers)]
        sum_numbers_list_map = map(int, sum_numbers_list)
        sum_numbers_convert_list = list(sum_numbers_list_map)
        numbers = sum(sum_numbers_convert_list)
    print(numbers)


def letter(client_name):
    letters = {'א': 1,
               'ב': 2,
               'ג': 3,
               'ד': 4,
               'ה': 5,
               'ו': 6,
               'ז': 7,
               'ח': 8,
               'ט': 9,
               'י': 1,
               'כ': 2,
               'ל': 3,
               'מ': 4,
               'ם': 4,
               'נ': 5,
               'ן': 5,
               'ס': 6,
               'ע': 7,
               'פ': 8,
               'ף': 8,
               'צ': 9,
               'ץ': 9,
               'ק': 1,
               'ר': 2,
               'ש': 3,
               'ת': 4,
               'ך': 2,

               }
    name_gimatriha = []
    for letter in client_name:
        if letter in letters:
            name_gimatriha.append(letters[letter])
    sum_l(name_gimatriha=name_gimatriha)

first_client_name = "שלומי"
letter(first_client_name)

#
# first_client_name = str(input( " הכנס שם פרטי מלא   "))
# last_client_name = str(input( " הכנס שם משפחה    "))
# full_name = first_client_name + last_client_name
# print(f" הגימטריה של {first_client_name} הוא: ")
# letter(first_client_name)
# print(f" הגימטריה של {last_client_name} הוא: ")
# letter(last_client_name)
# print("הגימטריה של השם המלא שזה אומר שאיפת האדם הוא:  ")
# letter(full_name)
# print(f"אהוי של {first_client_name} הוא:")
# letter(list(filter(aiv, full_name)))
# print(f"העיצורים של {first_client_name} הוא:")
# letter(list(filter(itzurim, full_name)))
