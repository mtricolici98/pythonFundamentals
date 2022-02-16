# Odd even lists as values in a dict, using list references
even = []
impar = []
my_dict = dict(even=even, impar=impar)
for k in range(5):
    k = int(input())
    if not k % 2:
        even.append(k)
    else:
        impar.append(k)
print(my_dict['even'])
print(my_dict['impar'])
print(my_dict['even'] == even)
print(my_dict['impar'] == impar)
