num = int(input())

def calcul(a):
    if a % 5 == 0 :
        print(a // 5)
    elif a % 5 != 0 and a // 5 >= 2 :
        if a % 5 == 3 :
            print((a // 5) + 1)
        elif (5 + (a % 5)) % 3 == 0 :
            print((a // 5) - 1 + ((5 + (a % 5)) // 3))
        elif (10 + (a % 5)) % 3 == 0 :
            print((a//5) - 2 + ((10 + (a % 5)) // 3))
        elif a % 3 == 0 :
            print(a // 3)
        else :
            print(-1)
    elif a % 5 !=0 and a // 5 == 1 :
        if a % 5 == 3 :
            print((a // 5) + 1)
        elif (5 + (a % 5)) % 3 == 0 :
            print((a // 5) - 1 + ((5 + (a % 5)) // 3))
        elif a % 3 == 0 :
            print(a // 3)
        else :
            print(-1)
    elif a % 5 != 0 and a // 5 == 0 :
        if a % 5 == 3 :
            print(1)
        else :
            print(-1)
    else :
        print(-1)
        
calcul(num)
