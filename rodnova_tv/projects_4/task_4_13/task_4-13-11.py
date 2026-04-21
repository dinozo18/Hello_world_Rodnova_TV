N = int(input("Введите N: "))

if N < 2:
    print("Нет элементов с чётными индексами")
else:
    sum_val = 0
    count = 0
    i = 1
    while i <= N:
        x = float(input("Введите число: "))
        if i % 2 == 0:          
            sum_val = sum_val + x
            count = count + 1
        i = i + 1
    avg = sum_val / count        
    print(avg)