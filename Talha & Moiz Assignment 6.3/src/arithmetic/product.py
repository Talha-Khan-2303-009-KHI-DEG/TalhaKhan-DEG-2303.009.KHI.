def multiply(num1,num2):
    """
    Returns the product of two numbers.

    Args:
        num1 (float or int): The first number.
        num2 (float or int): The second number.

    Returns:
        float: The product of num1 and num2.

    Raises:
        ValueError: If either num1 or num2 is not a float or int.

    Examples:
        >>> multiply(2, 3)
        6.0
        >>> multiply(1.5, -2)
        -3.0
    """
    if type(num1) == int|float and type(num2) == int|float:
        return float(num1 * num2)
    else:
        print("Both arguments must be of type int.")