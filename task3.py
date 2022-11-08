def delete(list_, index=None):
    if index is None:
        list_ = list_[:-1]
    else:
        if index < len(list_):
            index = index % len(list_)
            list_ = list_[:index] + list_[index+1:]
    return list_

print(delete([0, 0, 1, 2], index=6))
print(delete([0, 1, 1, 2, 3], index=-1))
print(delete([0, 1, 2, 3, 4, 4]))


