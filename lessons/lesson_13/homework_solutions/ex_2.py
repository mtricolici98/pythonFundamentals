elements = ['php', 'w3r', 'Python', 'abcd', 'Java', 'aaa']

palindromes = filter(lambda el: el == el[::-1], elements)
print(list(palindromes))
