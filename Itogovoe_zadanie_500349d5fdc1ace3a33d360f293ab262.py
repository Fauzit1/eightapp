#Задание 1 - Найти сумму геометрической прогрессии по n, b2, b5.
n = int(input("Введите номер задания: "))
if n == 1:
    def geometric_progression(n: int, q: int, b: int)-> int:
        b_prev = b
        for i in range(1, n):
            b_cur=b_prev*q
            print(b_cur)
            b_prev=b_cur
        return b_prev

#Задание 2 - Дана арифметическая прогрессия из n (n<10) членов, известны a1 и d. Найти сумму всех четных членов этой прогрессии.
if n==2:
# Разбиваем число на цифры 
d1 = num//100 
d2 = (num // 10) % 10 
d3 = num % 10 
 
# Находим сумму и произведение цифр 
sum = d1 + d2 + d3 
product = d1 * d2 * d3 
 
# Выводим результаты 
print("Сумма цифр:", sum) 
print("Произведение цифр:", product)

#Задание 3 - 
if n==3:
    n = int(input("Введите число: "))
    s = 0
    m = 1
    while n>0:
        s += n%10
        m *= n%10
        n = n//10
    print("Сумма:", s)
    print("Произведение:", m)

 #Задание 4 -
if n == 4:
    names = tuple(input("Введите имена студентов через пробел: ").split()) 
    name = [names]
    for name in names: 
        if "ва" in name:
            tuple(name)
            print = name
    
    
