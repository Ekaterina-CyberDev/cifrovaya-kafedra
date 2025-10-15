def is_prime(*numbers, check='mask'):
    """
    Проверяет числа на простоту.
    
    Аргументы:
    *numbers: числа для проверки
    check: режим проверки ('any', 'all', 'mask')
    
    Возвращает:
    - при check='any': True если есть хотя бы одно простое число
    - при check='all': True если все числа простые
    - при check='mask': кортеж с результатами для каждого числа
    """
    
    def check_single_number(n):
        """Проверяет одно число на простоту"""
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        
        # Проверяем делители до квадратного корня из n
        for i in range(3, int(n**0.5) + 1, 2):
            if n % i == 0:
                return False
        return True
    
    # Проверяем все числа
    results = [check_single_number(n) for n in numbers]
    
    # Возвращаем результат в зависимости от режима
    if check == 'any':
        return any(results)
    elif check == 'all':
        return all(results)
    else:  # режим 'mask' (по умолчанию)
        return tuple(results)


# Пример использования (как указано в задании)
if __name__ == "__main__":
    nums = [int(i) for i in input().split()]
    print(*is_prime(*nums), is_prime(*nums, check='all'), is_prime(*nums, check='any'))