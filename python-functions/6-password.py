def validate_password(password):
    SpecialSymbol = ["@", "#", "$", " ", "&", "%"]
    val = True 

    if len(password) < 8:  
        return False 
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if " " not in password:
        return True
    else:
        return False
    if val:
        return val