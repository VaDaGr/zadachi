def people(names):
    welcome = []
    for name in names:
        welcome.append("Привет " + name)
    return ", ".join(welcome)

print(people(["Паша" , "Глаша" , "Маша"]))