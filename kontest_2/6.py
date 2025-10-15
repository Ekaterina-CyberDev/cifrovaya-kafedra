class ExtensionManager:
    handlers = {}
    
    @classmethod
    def register(cls, extension, func):
        cls.handlers[extension] = func
    
    @classmethod
    def get_handler(cls, extension):
        return cls.handlers.get(extension)

def extensions_switcher(extension):
    def decorator(func):
        # Регистрируем функцию для указанного расширения
        ExtensionManager.register(extension, func)
        
        def wrapper(filename):
            # Получаем расширение файла
            if '.' in filename:
                file_extension = filename.split('.')[-1]
            else:
                return 'unsupported extension'
            
            # Находим подходящий обработчик
            handler = ExtensionManager.get_handler(file_extension)
            if handler:
                return handler(filename)
            else:
                return 'unsupported extension'
        
        wrapper.__name__ = func.__name__
        return wrapper
    return decorator
