def sum(*boxes):
    s = 0
    for x in boxes:
        s = s + x[0] * x[1] * x[2]
    return s

print(sum([1, 2, 3], [4, 5, 6], [7, 8, 9]))