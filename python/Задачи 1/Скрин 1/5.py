def list_sort(lst):
    lst.sort(key=lambda x: abs(x), reverse=True)
    return lst

print(list_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))