class Calculator:
    def add(self, x, y):
        """Возврат суммы двух значений."""
        return x + y

    def divide(self, x, y):
        """Деление одного числа на другое."""
        if y == 0:
            raise ValueError("делить на ноль нельзя")
        return x / y

    def is_prime_number(self, value):
        """Определение, является ли число простым."""
        if type(value) is not int:
            raise TypeError("ожидается целое число")

        if value < 2:
            return False

        limit = int(value ** 0.5)
        for divider in range(2, limit + 1):
            if value % divider == 0:
                return False

        return True
