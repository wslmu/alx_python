def no_c(my_string):
    """
    Removes all characters c and C from a string.
    Returns the new string
    """
    newString = ""
    for i in my_string:
        if i != "c" and i != "C":
            newString = newString + i
    return newString
    
