def rps(sign1, sign2):
    if sign1=='камень' and sign2=='бумага':
        return 'Победил второй игрок'
    elif sign1=='бумага' and sign2=='камень':
        return 'Победил первый игрок'
    elif sign1=='бумага' and sign2=='ножницы':
        return 'Победил второй игрок'
    elif sign1=='ножницы' and sign2=='бумага':
        return 'Победил первый игрок'
    elif sign1=='ножницы' and sign2=='камень':
        return 'Победил второй игрок'
    elif sign1=='камень' and sign2=='ножницы':
        return 'Победил первый игрок'
    else:
        return 'Ничья'

print(rps('камень' , 'ножницы'))