def typing(message):
    al = '_abcdefghijklmnopqrstuvwxyz'
    return sum(al.index(i) for i in message)

print(typing("never_gonna_give_you_up"))