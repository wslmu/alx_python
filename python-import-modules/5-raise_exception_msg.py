def raise_exception_msg(message=""):
    try:
        print(message)
    except NameError as ne:
        print(ne)
