def median(list):
    list.sort()
    num = len(list)
    even_or_odd = num // 2
    if num % 2 == 0:
        return (list[even_or_odd- 1] + list[even_or_odd]) / 2
    else:
        return list[even_or_odd]

print(median([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(median([1, 2, 3, 7, 8, 9, 10]))