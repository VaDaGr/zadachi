def camel(st):
    count = 0
    sentence = ''
    for letter in st:
        if letter.isalpha():
            if count == 0:
                letter = letter.upper()
                sentence += letter
                count = 1
            elif count == 1:
                letter = letter.lower()
                sentence += letter
                count = 0
        else:
            sentence += letter

    return sentence
print(camel("Hello, World"))