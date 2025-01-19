def safe_divide(numerator, denominator):
    try:
        result = numerator/denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."

    try:
        numerator = float(numerator)
        denominator = float(denominator)
        return numerator / denominator
    except ValueError:
        return "Please enter numeric only"
