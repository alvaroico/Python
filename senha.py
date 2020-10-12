def validar_senha(senha):
    flag_digit = False
    flag_alpha = False
    flag_upper = False
    flag_lower = False

    if len(senha) < 6 or len(senha) > 12:
        return False

    for i in senha:
        if not flag_digit and i.isdigit():
            flag_digit = True
        if not flag_alpha and i.isalpha():
            flag_alpha = True
        if not flag_upper and i.isupper():
            flag_upper = True
        if not flag_lower and i.islower():
            flag_lower = True

    return flag_digit and flag_alpha and flag_lower and flag_upper


print(validar_senha("1aWw23"))