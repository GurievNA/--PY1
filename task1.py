from pprint import pprint

def create_dict(num):
    return [{"bin": bin(n), "dec": n, "hex": hex(n), "oct": oct(n)} for n in range(num)]

pprint(create_dict(16))
