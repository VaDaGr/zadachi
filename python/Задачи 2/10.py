def convert_list(x, y):
    count = 0
    list = []
    for i in x :
        count += 1
    for i in range (0, count):
        list.append ([x[i], y[i]])
    return list

print(convert_list([1, 2, 3, 4, 5] , [5, 4, 3, 2, 1]))