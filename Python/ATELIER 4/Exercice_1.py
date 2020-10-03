"""
Exercice 1 de l'atelier 4 : Manipulations simples
file       = "Exercice_1.py"
author     = "Baptiste Varamo & Jean-François Giammari"
credits    = ["Baptiste Varamo","Jean-François Giammari"]
version    = "1.0"
"""


def full_name(str_arg: str) -> str:
    """
    Transform text (Uppercase for Name, Lowercase for surname)
    str_arg -- The string who contain the name/surname
    return the formated text
    """
    splited_text = str_arg.split()
    return splited_text[0].upper() + " " + splited_text[1].capitalize()


def is_mail(str_arg: str) -> (int, int):
    """
    Check if email is valid
    str_arg -- The string who contain the email
    return error code or succes code
    (1, 0, the mail is valid
    (0, 1) the mail is not valid, the body is not valid
    (0, 2) the mail is not valid, the @ is missing.
    (0, 3) the mail is not valid, the domain is not valid (univ-corse)
    (0, 4) the email is not valid, the . on the domain
    """
    result = (1, 0)

    if not '@' in str_arg:
        result = (0, 2)
    else:

        mail_split = str_arg.split('@')
        corp = mail_split[1]
        domaine = mail_split[1]

        # Check for (0,1) Error
        if len(str_arg) > 64 or corp.startswith(".") or corp.endswith(".") or corp.find("..") > -1 or corp.isnumeric() :
            result = (0, 1)

        # Check for (0,3) Error
        if len(domaine) < 3:
            result = (0, 3)

        # Check for (0,4) Error
        if not '.' in domaine:
            result = (0, 4)

    return result


def test_exercice1():
    """
    Test for Exercice 1
    """
    print("Test full_name (musk elon) : ", full_name('musk elon'))
    print("Test is_mail (eeeeeeeeeeeeeeeeeeeeeeeeeeeelon.musk@tesla.money) -> INV : ", is_mail('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeelon.musk@tesla.money'))
    print("Test is_mail (.elon.musk@tesla.money) -> INV : ", is_mail('.elon.musk@tesla.money'))
    print("Test is_mail (elon..musk@tesla.money) -> INV : ", is_mail('elon..musk@tesla.money'))
    print("Test is_mail (elon.musk@tesla.money.) -> INV : ", is_mail('elon.musk@tesla.money.'))
    print("Test is_mail (elon.musk@tesla.money) -> VALID : ", is_mail('elon.musk@tesla.money'))
    print("Test is_mail (elon.musk@.m) -> INV : ", is_mail('elon.musk@.m'))
    print("Test is_mail (elon.musk@teslamoney) -> INV : ", is_mail('elon.musk@teslamoney'))
    print("Test is_mail (elon.musk@tesla.\money) -> INV : ", is_mail('elon.musk@tesla.\money'))
    print("Test is_mail (elon.musktesla\money) -> INV : ", is_mail('elon.musktesla\money'))


test_exercice1()
