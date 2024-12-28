def super_massive(lst):
    def summer(lst):
        s = 0
        for x in lst:
            s = s + x
            yield s
    return list(summer(lst))

print(super_massive([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))