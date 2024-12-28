def all_eq(lst):
    biggest = max(lst, key=lambda x: len(x))
    biggest_len = len(biggest)
    return [item.ljust(biggest_len, '_') for item in lst]

print(all_eq(['физика', 'русский', 'математика', 'английский']))