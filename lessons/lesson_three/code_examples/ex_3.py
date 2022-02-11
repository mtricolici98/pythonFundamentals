# When you have eliminated all which is impossible, then whatever remains, however improbable, must be the truth

expected = 64

guess = int(input('Da-mi un numar:'))
if guess > expected:  # Numarul ghicit este mai MARE decat cel asteptat
    print('Mai mic')  # Cerem un numar mai mic
elif guess < expected:  # Numarul ghicit este mai MIC decat cel asteptat
    print('Mai mare')  # Cerem un numar mai mare
else:  # Numarul ghicit nu este nici mai mare nici mai mic decat cel asteptat, inseamna ca e EGAL
    print('Ai ghicit')

## OR

if guess == expected:
    print('Ai ghicit')
if guess < expected:
    print('Mai mare')
if guess > expected:
    print('Mai mic')

## OR

if guess == expected:
    print('Ai ghicit')
elif guess < expected:
    print('Mai mare')
else:
    print('Mai mic')
