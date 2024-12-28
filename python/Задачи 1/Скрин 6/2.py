my_dict = {'first_one': 'we can do it'}

def biggest_dict(**kwargs):
    my_dict.update(**kwargs)

biggest_dict(two=2, three=3, four=4, five=5)
biggest_dict(six=6, seven=7, eight=8, nine=9)
print(my_dict)