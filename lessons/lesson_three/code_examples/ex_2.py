nr_1 = input('Number 1:')
nr_2 = input('Number 2:')

if not nr_1.isnumeric() or not nr_2.isnumeric():
    print('Data viitoare sa folosesti numere')
else:
    print(int(nr_1) + int(nr_2))
# OR

if nr_1.isnumeric() and nr_2.isnumeric():
    print(int(nr_1) + int(nr_2))
else:
    print('Data viitoare sa folosesti numere')

## BONUS

potential_float = input('Da-mi un float:')
# Verifica daca str is float
# Impartim string-ul in n bucati folosind .
# Verificam ca sunt 2 bucati ( un float poate avea doar 2 bucati, 1 din stinga si a doua din dreapta punctului)
# Verificam partea din stringa (prima bucata) e numerica si ca partea din dreapta (a doua bucata) e numerica
if len(potential_float.split('.')) == 2 and potential_float.split('.')[0].isnumeric() and potential_float.split('.')[1].isnumeric():
    print('Numarul este float')
