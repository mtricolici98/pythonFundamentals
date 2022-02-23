# Writing
# my_file = open('new_file.txt', 'w')
# my_file.write('Hello from python3') #
# my_file.close()
#
# # Reading
# my_file = open('new_file.txt', 'r')
# data_from_file = my_file.read() # Reading all the data in the file
# print(data_from_file)

# Appending
# my_file = open('new_file.txt', 'a')
# my_file.write('Hello from python3') # Appending Hello from python3 to the file
# my_file.close()

# # Reading

my_file = open('new_file_3.txt', 'r+')
print(my_file.read())
my_file.seek(0)
print(my_file.read())
my_file.seek(0, 2)
my_file.write('123')

print(my_file.read())
