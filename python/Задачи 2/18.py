def change(text):
    for i in range(len(text)):
        if text[i] == 'а':
            text = text.replace(text[i], '4')
        elif text[i] == 'е':
            text = text.replace(text[i], '3')
        elif text[i] == 'и':
            text = text.replace(text[i], '1')
        elif text[i] == 'о':
            text = text.replace(text[i], '0')
        elif text[i] == 'с':
            text = text.replace(text[i], '5')
    return text

print(change('50 задач это слишком много :)'))
