nume = input('Introdu Numele')
t_z = input('Introdu timpul zilei: z - ziua / s - seara:')
t_z = t_z.lower()
text = 'ziua' if t_z == 'z' else 'seara'
print('Buna ' + text + ', ' + nume)

# OR
# Text va fi seara daca t_z este 's' de altfel va fi 'ziua'
text = 'seara' if t_z == 's' else 'ziua'
print('Buna ' + text + ', ' + nume)

# Echivalent cu
if t_z == 's':
    text = 'seara'
else:
    text = 'ziua'
