def safe_print_division(a, b):
    """
    Assume that a and b are integers
    This function:
    - divides the 2 integers
    - prints the result
    - returns the value of the division, otherwise: None
    """
    try:
        result = a/b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
        return result