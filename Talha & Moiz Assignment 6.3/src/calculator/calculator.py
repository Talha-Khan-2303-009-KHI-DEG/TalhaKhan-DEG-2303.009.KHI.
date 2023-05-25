from constants import ERROR_VALUE
from sum import add
from product import multiply

class Calculator:
    """
    A positive calculator that performs addition and multiplication.

    Attributes:
        error (float): The error value to return for invalid operations.
        name (str): The name of the calculator.

    Methods:
        add_positive: Performs addition if both arguments are positive.
        multiply_positive: Performs multiplication if both arguments are positive.
    """
    def __init__(self, name):
        """
        Initializes a Calculator object.

        Args:
            name (str): The name of the calculator.
        """
        self.name = name
        self.error = ERROR_VALUE

    def add_positive(self, num1, num2):
        """
        Adds two positive numbers.

        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.

        Returns:
            float: The sum of num1 and num2 if both numbers are positive, otherwise the error value.

        Examples:
            >>> calc = Calculator("Positive calculator")
            >>> calc.add_positive(2, 3)
            5.0
            >>> calc.add_positive(-1, 4)
            -1.0
        """
        if num1 > 0 and num2 > 0:
            return add(num1, num2)
        else:
            return self.error

    def multiply_positive(self, num1, num2):
        """
        Multiplies two positive numbers.

        Args:
            num1 (float or int): The first number.
            num2 (float or int): The second number.

        Returns:
            float or error: The product of num1 and num2 as a float if both numbers are positive,
                            otherwise returns the error value.

        Examples:
            >>> calc = Calculator("MyCalculator")
            >>> calc.multiply_positive(2, 3)
            6.0
            >>> calc.multiply_positive(-1, 4)
            -1.0
        """
        if num1 > 0 and num2 > 0:
            return multiply(num1, num2)
        else:
            return self.error
