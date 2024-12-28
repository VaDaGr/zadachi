def help_bool(letter=None):
    if letter == 'к':
        return 'a+b = b+a, ab=ba'
    elif letter == 'а':
        return '(а + b) + c = a + (b + c) , (ab)c = a(bc)'
    elif letter == 'д':
        return 'с (a + b) = са + cb , (а + b)c = ас + bc'
    elif letter == 'м':
        return 'не(А и В) = не А или не В , не(А или В) = не А и не В , не(не А) = А '
    else:
        return 'Возможные аргументы: к – Коммутативность, д – Дистрибутивность, а – Ассоциативность, м – Теорема Де Моргана'

print(help_bool('мак'))
print(help_bool(3))
print(help_bool('к'))