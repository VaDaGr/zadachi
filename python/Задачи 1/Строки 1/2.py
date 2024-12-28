def first_last(letter, st):
    first = st.find(letter)
    if first < 0:
        return None, None
    last = st.rfind(letter)
    return first, last

print(first_last('е', 'длинношеее'))
print(first_last('i', 'indivisibility'))
print(first_last('б', 'превыскомногорассмотрительствующий'))