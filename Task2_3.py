# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

# HW6_1 Создайте модуль и напишите в нём функцию, которая получает на вход дату в формате DD.MM.YYYY
# Функция возвращает истину, если дата может существовать или ложь, если такая дата невозможна.
# Для простоты договоримся, что год может быть в диапазоне [1, 9999].
# Весь период (1 января 1 года - 31 декабря 9999 года) действует Григорианский календарь.
# Проверку года на високосность вынести в отдельную защищённую функцию.

class DateValidator:
    def __init__(self):
        pass

    def is_leap_year(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                leap = year % 400 == 0
            else:
                leap = True
        else:
            leap = False
        return leap

    def is_valid_date(self, date_str):
        try:
            day, month, year = map(int, date_str.split('.'))
            if 1 <= year <= 9999 and 1 <= month <= 12:
                days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
                if self.is_leap_year(year):
                    days_in_month[1] = 29
                valid_day = 1 <= day <= days_in_month[month - 1]

                leap_message = "високосный" if self.is_leap_year(year) else "не високосный"
                print(f"{year} год - {leap_message}")

                return valid_day
        except ValueError:
            pass
        return False


if __name__ == "__main__":
    date_validator = DateValidator()

    date_str = "24.12.2020"
    result = date_validator.is_valid_date(date_str)
    print(f"Дата {date_str} существует: {result}")
