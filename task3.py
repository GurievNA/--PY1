def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]
        return list_
    if not isinstance(index, int):
        raise ValueError
    elif len(list_) < index:
        raise ValueError
    else:
        index = index % len(list_)
        list_ = list_[:index] + list_[index+1:]
    return list_

try:
    print(delete([0, 0, 1, 2], index=6))
except:
    print("Invalid index")
try:
    print(delete([0, 1, 1, 2, 3], index=-1))
except:
    print("Invalid index")
try:
    print(delete([0, 1, 2, 3, 4, 4]))
except:
    print("Invalid index")


