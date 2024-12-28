def blackjack(cards):
    аmount = 0
    for i in cards:
        if i in ['В', 'Д', 'К']:
            аmount += 10
        elif i == "Т":
            аmount += 1
        else:
            аmount += i
    if аmount > 21:
        return True
    return False

print(blackjack([5 , 5 , 3 , 9]))