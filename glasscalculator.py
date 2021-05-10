import math
def shop(l,b,p):
    l = math.ceil(l)
    b = math.ceil(b)
    if (l>0):
        if (l >=1 and l<20):
            nl = l+3
        elif (l >=20 and l<30):
            nl = l+4
        elif (l >=30 and l<40):
            nl = l+5
        elif (l>=40 and l<50):
            nl = l+6
        else:
            nl = l+7

#increasing the breadth
    if (b>0):
        if (b >=1 and b<20):
            newb = b+3
        elif (b >=20 and b<30):
            newb = b+4
        elif (b >=30 and b<40):
            newb = b+5
        elif (b>=40 and b<50):
            newb = b+6
        else:
            newb = b+7

    cost = math.ceil(((nl*newb)*p)/144)
    return cost


if __name__ == "__main__":
    length = int(input("Enter the length in inch :"))
    breadth = int(input("Enter the Breadth in inch :"))
    price = int(input("Enter the price of glass in RS :"))
    print("The cost of the glass is :",shop(length,breadth,price))