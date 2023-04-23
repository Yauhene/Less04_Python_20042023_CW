def new_string(symbol, count=3):
    return symbol * count


print(new_string('!', 5)) # !!!!!
print(new_string('!'))

# ● Можно указать любое количество значений аргумента функции.
# ● Перед аргументом надо поставить *.
# В примере ниже функция работает со строкой, поэтому при введении чисел
# программа выдаёт ошибку:
def concatenatio(*params):
    res = ""
    for item in params:
        res += item
    return res

print(concatenatio('a', 's', 'd', 'w')) # asdw
print(concatenatio('a', '1')) # a1
# print(concatenatio(1, 2, 3, 4)) # TypeError: ...