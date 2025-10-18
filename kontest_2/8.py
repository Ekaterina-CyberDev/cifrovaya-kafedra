class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def bonus(self, percentage):
        # Вычисляем надбавку и округляем до ближайшего целого
        return round(self.salary * percentage)
    
    def salary_total(self):
        # Получаем процент надбавки из глобального словаря bonuses
        global bonuses
        bonus_percentage = bonuses.get(self.position, 0)
        # Вычисляем итоговую зарплату
        return self.salary + self.bonus(bonus_percentage)
    
    def __repr__(self):
        return f"{self.name} ({self.position}): {self.salary_total()}"


class Manager(Employee):
    def __init__(self, name, salary=16242):
        # Вызываем конструктор родительского класса с должностью "manager"
        super().__init__(name, 'manager', salary)
    
    def bonus(self, percentage):
        # Надбавка не может быть меньше 10%
        min_percentage = max(percentage, 0.1)
        return round(self.salary * min_percentage)
