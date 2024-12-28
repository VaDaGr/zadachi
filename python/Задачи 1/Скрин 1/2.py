def change(lst):
    first = lst.pop()
    last = lst.pop(0)
    lst.append(last)
    lst.insert(0, first)
    return lst

print(change([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
