from pprint import pprint

num = 16

def create_dict(num):
    dictionary = []
    for n in range(num):
        dictionary.append ({"bin": bin(n),
                  "dec": n,
                  "hex": hex(n),
                  "oct": oct(n)})
    return dictionary

pprint(create_dict(num))

