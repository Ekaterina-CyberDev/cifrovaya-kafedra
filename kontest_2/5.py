def login_required(func):
    def wrapper(*args, **kwargs):
        # Получаем глобальные переменные
        from __main__ import token, logged
        if token in logged:
            return func(*args, **kwargs)
        else:
            print("Access denied")
            return None
    wrapper.__name__ = func.__name__
    return wrapper


# Остальной код остается таким же...