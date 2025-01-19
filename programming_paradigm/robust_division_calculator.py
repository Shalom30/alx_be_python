def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return f"The result of the operation is {result}"
    except ValueError:
        return "Error: Please enter numeric values only."

    try:
        result = numerator / denominator
        return f"The result of the operation is {result}"
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."


