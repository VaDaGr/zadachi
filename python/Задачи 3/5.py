def pluses(s):
    s = '<' + s + '>'
    n = len(s)
    for i in range(1, n-1):
        if s[i].isalpha():
            if not (s[i-1]=='+' and s[i+1]=='+'):
                return False
    return True

print(pluses("+c++"))