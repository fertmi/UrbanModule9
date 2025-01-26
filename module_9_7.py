def is_prime(func):
    def wrapper(*args):
        function = func(*args)
        is_prime_bool = True
        for i in range(2, function):  # цикл для проверки деления на число от 2 до числа из списка
            if function % i == 0:  # проверка деления без остатка
                 is_prime_bool = False  # если делится, то это непростое число
                 break  # прервать процесс деления
            else:
                 is_prime_bool = True  # простое число, если после перебора циклом не делится без остатка
        if is_prime_bool:
            print(f"Cумма трех чисел {args} число Простое")  # если простое число, печатаем "Простое"
        else:
            print(f"Cумма трех чисел {args} число Составное")  # если число непростое, печатаем "Составное"
        return function
    return wrapper

@is_prime
def sum_three(a, b, c):
    result_three = a+b+c
    return result_three

result = sum_three(2, 3, 6)
print(f"Сумма трех чисел равна {result}")
result = sum_three(3, 3, 7)
print(f"Сумма трех чисел равна {result}")
result = sum_three(6, 3, 7)
print(f"Сумма трех чисел равна {result}")