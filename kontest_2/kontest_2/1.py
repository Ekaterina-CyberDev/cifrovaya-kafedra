def min_number(n):
    # Если n меньше 10, то минимальное число - само n
    if n < 10:
        return n
    
    # Разлагаем n на множители от 9 до 2
    digits = []
    for divisor in range(9, 1, -1):
        while n % divisor == 0:
            digits.append(divisor)
            n //= divisor
    
    # Если после разложения n не равно 1, значит невозможно представить
    # n как произведение цифр
    if n != 1:
        return 0
    
    # Сортируем цифры в возрастающем порядке для получения минимального числа
    digits.sort()
    
    # Преобразуем список цифр в число
    result = 0
    for digit in digits:
        result = result * 10 + digit
    
    return result

# Примеры использования
if __name__ == "__main__":
    # Пример 1
    print(min_number(72))  # Должно вернуть 89 (8*9=72)
    
    # Пример 2  
    print(min_number(73))  # Должно вернуть 0