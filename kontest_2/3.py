def prime_nums():
    """
    Генератор бесконечной последовательности простых чисел, начиная с 2.
    """
    yield 2  # Первое простое число
    
    n = 3
    while True:
        # Проверяем, является ли n простым числом
        is_prime = True
        
        # Проверяем делители до квадратного корня из n
        # Проверяем только нечетные делители, начиная с 3
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                is_prime = False
                break
        
        if is_prime:
            yield n
        
        n += 2  # Переходим к следующему нечетному числу


# Код для проверки (как указано в задании)
if __name__ == "__main__":
    count = int(input())
    prime = prime_nums()
    for _ in range(count):
        print(next(prime))