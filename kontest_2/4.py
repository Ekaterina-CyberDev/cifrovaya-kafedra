def hanoi(n, source='a', target='b', auxiliary='c'):
    """
    Генератор для решения задачи Ханойских башен.
    
    Аргументы:
    n - количество дисков
    source - исходный стержень (по умолчанию 'a')
    target - целевой стержень (по умолчанию 'b') 
    auxiliary - вспомогательный стержень (по умолчанию 'c')
    """
    if n == 1:
        yield (source, target)
    else:
        # Перемещаем n-1 дисков с source на auxiliary
        yield from hanoi(n - 1, source, auxiliary, target)
        
        # Перемещаем самый большой диск с source на target
        yield (source, target)
        
        # Перемещаем n-1 дисков с auxiliary на target
        yield from hanoi(n - 1, auxiliary, target, source)


# Код для проверки
if __name__ == "__main__":
    n = int(input())
    steps = hanoi(n)

    towers = {'a': list(range(n)), 'b': [], 'c': []}
    for src, dest in steps:
        towers[dest].append(towers[src][-1])
        towers[src].pop()
        is_sorted = all(tower[i] < tower[i+1] for tower in towers.values() for i in range(len(tower) - 1))
        if not is_sorted:
            print('NO')
            exit(1)

    expect = {'a': [], 'b': list(range(n)), 'c': []}
    print('YES' if towers == expect and list(steps) == [] else 'NO')