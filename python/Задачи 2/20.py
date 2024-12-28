def growing(list):
    while len(list) > 1:
        last_num = list.pop()
        if last_num <= list[-1]:
            return False
    return True

print(growing([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(growing([1, 3, 5, 2]))