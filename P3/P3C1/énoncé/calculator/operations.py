def addition(left_param, right_param):
    return left_param + right_param

def soustraction(left_param, right_param):
    return left_param - right_param

def multiplication(left_param, right_param):
    return left_param * right_param

def division(left_param, right_param):
    try:
        return left_param / right_param
    except ZeroDivisionEror:
        print("Erreur : Division par zéro ! ")