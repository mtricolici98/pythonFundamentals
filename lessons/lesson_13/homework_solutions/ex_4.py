def my_user_input_generator(stop_at):
    while True:
        user_input = input("Please enter something: ")
        if user_input == stop_at:
            break
        yield user_input


for user_input in my_user_input_generator('STOP'):
    print(user_input)
