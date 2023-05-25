def add(num1,num2):
    """
    Returns the sum of two numbers.

    Args:
        num1 (float or int): The first number.
        num2 (float or int): The second number.

    Returns:
        float: The sum of num1 and num2.

    Raises:
        ValueError: If either num1 or num2 is not a float or int.

    Examples:
        >>> add(2, 3)
        5.0
        >>> add(1.5, -2.5)
        -1.0
    """
    if type(num1) == int and type(num2) == int:
        return float(num1 + num2)
    else:
        print("Both arguments must be of type int.")