# Программа "Сотрудник"


class Worker:

    def __init__(self, lname, fname, position, wage, bonus):
        self.lname = lname
        self.fname = fname
        self.position = position
        self.wage = wage
        self.bonus = bonus
        self._income = {'wage': self.wage, 'bonus': self.wage * self.bonus / 100}


class Position(Worker):

    def get_full_name(self):
        return self.lname + ' ' + self.fname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


w1 = Position('Жуликов', 'Сергей', 'сантехник', 50000, 25)
print('Фамилия - ', w1.lname)
print('Имя - ', w1.fname)
print('Должность - ', w1.position)
print('Полное имя - ', w1.get_full_name())
print('Оклад, руб.: ', w1.wage)
print('Размер премии, %: ', w1.bonus)
print('Размер дохода, руб.: ', w1.get_total_income())

w2 = Position('Петросян', 'Артур', 'электрик', 42000, 30)
print(f'{w2.get_full_name()} - {w2.position}, доход - {w2.get_total_income()} руб.')
exit()
