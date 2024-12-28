def count_it(dictan):
    count_num = {int(number): dictan.count(number) for number in dictan}
    sorting = sorted(count_num.items(), key=lambda element: element[1])
    return dict(sorting[-3:])

print(count_it('12121212211515121221311121212215555151551'))
print(count_it('00000001111111222222233333344455566'))