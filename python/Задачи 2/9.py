def inoagents(names, enemies):
    for i in enemies:
        for j in names:
            if i == j:
                names.remove(i)
    return names

print(inoagents(["Люда" , "Петя" , "Вася" , "Игорь" , "Вениамин"] , ['Donald' , 'Joseph' , 'Igor' , 'Вениамин']))