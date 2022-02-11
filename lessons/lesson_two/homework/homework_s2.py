# Ex1
result = 'Hello' * 2
print(result)  # HelloHello

# Ex2

new_string = input()
a_s = new_string.count('a')
e_s = new_string.count('e')
o_s = new_string.count('o')
y_s = new_string.count('y')
u_s = new_string.count('u')
i_s = new_string.count('i')
print(a_s + e_s + o_s + y_s + u_s + i_s)

# Or

new_string = input()
print(
    new_string.count('a') +
    new_string.count('e') +
    new_string.count('o') +
    new_string.count('y') +
    new_string.count('u') +
    new_string.count('i')
)

# Or


new_string = input()
count = 0
count += new_string.count('a')
count += new_string.count('e')
count += new_string.count('o')
count += new_string.count('y')
count += new_string.count('u')
count += new_string.count('i')
print(count)

# Ex3

email = input('Input a gmail email: ')
# Optional (make it lowercase)
email = email.lower()
email_end = email[-10:]
print(email_end == '@gmail.com')

# Or

email = input('Input a gmail email: ')
# Optional (make it lowercase)
email = email.lower()
print(email_end.count('@gmail.com') == 1)
