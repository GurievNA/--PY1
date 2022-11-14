from random import sample
import string

def get_random_password(length) -> str:
    signs = list(string.ascii_uppercase + string.ascii_lowercase + string.digits)
    if length < 0:
        print("Длина не может быть отрицательной")
        return ''
    password = ''.join(sample(signs, length))
    return password



print(get_random_password(8))
