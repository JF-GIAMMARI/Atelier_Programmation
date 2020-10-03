"""
Exercice 5 de l'atelier 4 : Vérification d'expressions arithmétiques
file       = "Exercice_5.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""


def ouvrante(car: str) -> bool:
    """
    Check if  a char is an opening bracket, hook or brace
    car -- Char to analyse
    return True if car is an opening bracket, hook or brace
    """
    BRACKET = 40
    HOOK = 91
    BRACE = 123
    car = car[0]
    return ord(car) == BRACKET or ord(car) == HOOK or ord(car) == BRACE


def fermante(car: str) -> bool:
    """
    Check if  a char is an closing bracket, hook or brace
    car -- Char to analyse
    return True if car is an closing bracket, hook or brace
    """
    BRACKET = 41
    HOOK = 93
    BRACE = 125
    car = car[0]
    return ord(car) == BRACKET or ord(car) == HOOK or ord(car) == BRACE


def renverse(car: str) -> str:
    """
    Replace an bracket, hook or hug by its reverse
    car -- Char to analyse
    return the inverted char
    """
    BRACKETS = [40, 41]
    HOOKS = [91, 93]
    BRACES = [123, 125]
    car = ord(car[0])

    if car == BRACKETS[0]:
        car = BRACKETS[1]
    elif car == HOOKS[0]:
        car = HOOKS[1]
    elif car == BRACES[0]:
        car = BRACES[1]

    return chr(car)


def operateur(car: str) -> bool:
    """
    Check if a char is an operator (* +)
    car -- Char to analyse
    return True if car is an operator
    """
    MULTIPLICATION = 42
    ADDITION = 43
    SOUSTRACTION = 45
    car = car[0]
    return ord(car) == MULTIPLICATION or ord(car) == ADDITION or ord(car) == SOUSTRACTION


def nombre(car: str) -> bool:
    """
    Check if a char is a number
    car -- Char to analyse
    return True if car is a number
    """
    return car.isdigit()


def caractere_valide(car: str) -> bool:
    """
    Check if a char is valid
    car -- Char to analyse
    return True if is valid
    """
    return ouvrante(car) or fermante(car) or nombre(car) or operateur(car)


def verif_parenthese(expression: str):
    """
    Check if an expression is valid
    Expression -- str to analyse
    return True if is valid
    """
    lst_P = []
    is_valid = True
    length = len(expression)
    i = 0
    while i < length and is_valid:
        if not caractere_valide(expression[i]):
            is_valid = False
        if ouvrante(expression[i]):
            lst_P.append((expression[i]))
        elif fermante(expression[i]):
            if lst_P[0]:
                if renverse(lst_P[-1]) == expression[i]:
                    lst_P.pop(-1)
                else:
                    is_valid = False
            else:
                is_valid = False
        i += 1
    return is_valid


def test_exercice5():
    """
       Test for exercice 5
    """
    print("Test ouvrante avec ( - TRUE : ", ouvrante("("))
    print("Test ouvrante avec { - TRUE : ", ouvrante("{"))
    print("Test ouvrante avec [ - TRUE : ", ouvrante("["))
    print("Test ouvrante avec ) - FALSE : ", ouvrante(")"))
    print("\nTest fermante avec ) - TRUE : ", fermante(")"))
    print("Test fermante avec } - TRUE : ", fermante("}"))
    print("Test fermante avec ] - TRUE : ", fermante("]"))
    print("Test fermante avec ( - FALSE : ", fermante("("))
    print("\nTest renverse avec (  : ", renverse("("))
    print("Test renverse avec {  : ", renverse("{"))
    print("Test renverse avec [  : ", renverse("["))
    print("Test renverse avec )  : ", renverse(")"))
    print("Test renverse avec }  : ", renverse("}"))
    print("Test renverse avec ]  : ", renverse("]"))
    print("Test renverse avec ]  : ", renverse("1"))
    print("\nTest operateur avec * -> TRUE  : ", operateur("*"))
    print("Test operateur avec + -> TRUE  : ", operateur(*"+"))
    print("Test operateur avec f -> FALSE  : ", operateur("f"))
    print("\nTest nombre avec 4 -> TRUE  : ", nombre("4"))
    print("Test nombre avec g -> FALSE  : ", nombre("g"))
    print("\nTest caractère_valide avec 4 -> TRUE : ", caractere_valide("4"))
    print("Test caractère_valide avec ) -> TRUE : ", caractere_valide(")"))
    print("Test caractère_valide avec g -> FALSE  : ", caractere_valide("g"))
    print("\nTest expression_valide avec ([[3+2]*[6+1]]) -> TRUE : ", verif_parenthese("([[3+2]*[6+1]])"))
    print("Test expression_valide avec (3+2] * 6-1 -> FALSE : ", verif_parenthese("(3+2]*6-1"))


test_exercice5()
