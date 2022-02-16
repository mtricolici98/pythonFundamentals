# Odd even lists as values in a dict

odd_even = {
    'odd': [],
    'even': []
}

for a in range(5):
    num = int(input('Number'))
    if num % 2 == 0:
        odd_even['even'].append(num)
    else:
        odd_even['odd'].append(num)
