# Задача 6.
# Дана строка (возможно,пустая),состоящая из букв A-Z:
# AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
# Нужно написать функцию RLE, которая на выходе даст строку вида:
# A4B3C2XYZD4E3F3A6B28
# И сгенерирует ошибку, если на вход пришла невалидная строка.
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def compress_str(string):
    validation = [chr(i) for i in range(ord("A"), ord("Z") + 1)]
    if not set(string).issubset(validation):
        return "невалидная строка"
    result = []
    count = 0
    last_index = len(string) - 1
    for i in range(len(string)):
        current_char = string[i]
        if i != last_index and current_char != string[i + 1]:
            result.append(current_char)
            if count != 0:
                result.append(count + 1)
                count = 0
        else:
            count += 1
            if i == last_index:
                result.append(f"{current_char}{count}")
    return result


input_str = "AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB"
print(*compress_str(input_str), sep="")




#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#Пример:
#A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input("Введите число "))
b = int(input("Введите степень числа(целое неотрицательно число) "))


def func(a, b):
    if b == 0:
        return 1

    return a * func(a, b - 1)


print(func(a, b))