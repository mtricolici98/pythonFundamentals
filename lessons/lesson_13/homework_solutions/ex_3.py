def validate_numeric(func):
    def wrapped(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float, complex)):
            raise ValueError("Result type is not numeric")
        return result

    return wrapped


@validate_numeric
def return_number():
    return 10


@validate_numeric
def return_str():
    return '123'


print(return_number())
# 10
print(return_str())
# ValueError: Result type is not numeric
