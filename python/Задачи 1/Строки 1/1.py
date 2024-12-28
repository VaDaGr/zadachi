def search_substr(subst, st):
    if subst.lower() in st.lower():
        return 'Есть контакт!'
    else:
    	return 'Мимо!'

print(search_substr('Кот', 'Каток'))
print(search_substr('Бок', 'кубок'))
