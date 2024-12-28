def to_float(num):
    if isinstance(num, (int, float)):
        return float(num)
    return "Невозможно преобразовать"

print(to_float(1))
print(to_float(-2))
print(to_float(1,2))
print(to_float('Числа'))
print(to_float('0'))