def dont_screaming(phrase):
    if phrase[-1] not in ["?", "!"]:
        return phrase
    s = phrase[-1]
    while phrase[-1] == s:
        phrase = phrase[:-1]
    return phrase + s

print(dont_screaming("Don't call my name, don't call my name Alejandro!!!!"))