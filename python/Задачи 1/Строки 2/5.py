def shortener(st):
    while '(' in st or ')' in st:
        left = st.rfind('(')
        right = st.find(')', left)
        st = st.replace(st[left:right + 1], '')
    return st

print(shortener("I won't cry for you (I really won't)I won't crucify the things you do, do, do (Ooh)"))