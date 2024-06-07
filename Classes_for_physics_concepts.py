class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def addition(self, term):  # метод сложения
        """Метод сложения дробей."""
        first_action = float(term) * self.denominator
        second_action = float(first_action) + self.numerator
        third_act = float(second_action) / self.denominator

        return third_act

    def subtraction(self, minuend):  # метод вычитания
        first_action = float(minuend) * self.denominator
        second_action = float(first_action) - self.numerator
        third_act = float(second_action) / self.denominator

        return third_act

    def multiplication(self, factor):  # метод умножения
        first_action = float(factor) * self.numerator
        return f"{float(first_action)}/{self.denominator}"

    def division(self, divider):  # метод деления
        first_action = self.denominator * divider
        return f"{self.numerator}/{first_action}"

    def get_denominator(self):  # посмотреть знаменатель
        return self.denominator

    def get_numerator(self):  # посмотреть числительное
        return self.numerator

    def set_denominator(self, set_number):  # изменение знаменателя
        self.denominator = set_number

    def set_numerator(self, set_number):  # изменение числителя
        self.numerator = set_number

    def display(self):  # посмотреть пример
        return f"{self.numerator}/{self.denominator}"


class Conversion_degree:  # Класс для конвертирования Цельсия и Фаренгейт и наоборот

    @staticmethod
    def Celsius_to_Fahrenheit(Celsius):  # метод для конвертирования Цельсия в Фаренгейт
        return float(Celsius) * 9 / 5 + 32

    @staticmethod
    def Fahrenheit_to_Celsius(Fahrenheit):  # метод для конвертирования Фаренгейт в Цельсия
        return (float(Fahrenheit) - 32) * 5 / 9


class Translation_of_measures:  # Класс для конвертирования Галлоны в Литры, Километры в Мили и наоборот

    @staticmethod
    def liters_to_gallons(liters):  # метод для конвертирования Литры в Галлоны
        return round(float(liters) / 3.785, 6)

    @staticmethod
    def gallons_to_litters(gallons):  # метод для конвертирования Галлоны в Литры
        return round(float(gallons) * 3.785, 6)

    @staticmethod
    def miles_to_kilometers(miles):  # метод для конвертирования Мили в Километры
        return float(miles) * 1.609

    @staticmethod
    def kilometers_to_miles(kilometers):  # метод для конвертирования Километры в Мили
        return float(kilometers) / 1.609


proverka = Fraction().addition(20.8194)
print(proverka)