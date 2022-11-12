from random import choice, sample
import string

def get_random_password(length, signs) -> str:
    if length < 0:
        print("Длина не может быть отрицательной")
        return ''
    password = ''.join(sample(signs, length))
    return password


signs1 = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
print(get_random_password(7, signs1))
