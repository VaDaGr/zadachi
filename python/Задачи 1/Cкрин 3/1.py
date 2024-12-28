def dislike_6(a):
    if a == 6 or a == 6.0:
        return 'Только не 6!'
    return True

print(dislike_6(6.0))
print(dislike_6(6))
print(dislike_6('6'))
print(dislike_6(5))
print(dislike_6("[6, 6]"))