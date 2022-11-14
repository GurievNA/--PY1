from random import randint

def get_unique_list_numbers(num1, num2, size) -> list[int]:
    unique_numbers = []
    while len(unique_numbers) != size:
        n = randint(num1, num2)
        if n in unique_numbers:
            continue
        else:
            unique_numbers.append(n)
    return unique_numbers

num1 = -10
num2 = 10
size = 15

list_unique_numbers = get_unique_list_numbers(num1, num2, size)
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))
