# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# HW4-3 Возьмите задачу о банкомате из семинара 2.
# Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance
        self.operations = []

    def check_balance(self, amount):
        if amount <= self.balance:
            return True
        else:
            return False

    def withdraw(self, amount):
        if self.check_balance(amount):
            self.balance -= amount
            self.operations.append(f'Снятие: {amount}')
            return True
        else:
            return False

    def deposit(self, amount):
        self.balance += amount
        self.operations.append(f'Пополнение: {amount}')

    def print_operations(self):
        print('Последние операции:')
        for operation in self.operations:
            print(operation)

    def exit_program(self):
        print('Программа завершена.')

if __name__ == "__main__":
    account = BankAccount(10000)

    while True:
        print('Сумма денег:', account.balance)
        action = input('\nВыберите действие (пополнить, снять, печать, выйти): ')

        if action == 'выйти':
            account.exit_program()
            break

        elif action == 'пополнить':
            amount = int(input('Введите сумму пополнения: '))
            if amount % 50 != 0:
                print('Сумма пополнения должна быть кратной 50 у.е.')
                continue

            account.deposit(amount)

            if len(account.operations) % 3 == 0:
                account.balance *= 1.03

        elif action == 'снять':
            amount = int(input('Введите сумму снятия: '))
            if amount % 50 != 0:
                print('Сумма снятия должна быть кратной 50 у.е.')
                continue

            if not account.withdraw(amount):
                print('Недостаточно средств на счете.')

        elif action == 'печать':
            account.print_operations()

        else:
            print('Некорректное действие. Попробуйте снова.')
            continue
