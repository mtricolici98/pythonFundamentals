name = input('Name:')
age = int(input('Age:'))
gender = input('Gender (F/M):')
if age >= 18:
    if gender.upper() == 'F':
        print('Welcome Ms.', name)
    else:
        print('Welcome Mr.', name)
else:
    print('Yo', name)

# If-expression version

name = input('Name:')
age = int(input('Age:'))
gender = input('Gender (F/M):')
if age >= 18:
    text = 'Welcome Ms.' if gender.upper() == 'F' else 'Welcome Mr.'
    print(text, name)
else:
    print('Yo, ', name)

# If-elif version

name = input('Name:')
age = int(input('Age:'))
gender = input('Gender (F/M):')
if age >= 18 and gender.upper() == 'F':
    print('Welcome Ms.', name)
elif age >= 18 and gender.upper() == 'M':
    print('Welcome Mr.', name)
else:
    print('Yo, ', name)
