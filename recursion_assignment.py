def change(amount):
    assert(amount>=24)
    if amount ==24:
        return [5,5,7,7]
    if amount ==25:
        return [5,5,5,5,5]
    if amount ==26:
        return [5,7,7,7]
    if amount ==27:
        return [5,5,5,5,7]
    if amount ==28:
        return [7,7,7,7]
    coins = change(amount-5)
    coins.append(5)
    return coins

amount = int(input("Enter the amount from 24 to 1000: "))
print(change(amount))



    
    