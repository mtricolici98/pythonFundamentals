usr_list = []
for a in range(int(input())):
    print(a)
    usr_list.append(
        dict(
            username=input('Username: '),
            age=input('Age: '),
        )
    )

user_found = False

for usr in usr_list:
    if int(usr['age']) >= 25:
        print(usr['username'])
        user_found = True
        break
if not user_found:
    print('No users above 25')
