def sumNumbers(n):
    summa = 0
    for i in range(1, n + 1):
        summa += i
    return summa

    #print(summa)
    
# n = int(input('Введи число, дружок: ')) # 5
# sumNumbers(n) # 15

n = int(input('Введи число, дружок: ')) # 5
print(sumNumbers(n)) # 15