def input_check(txt: str):
    if txt.isalpha() and not txt == " ":
        return True
    else:
        return False


def welcome():
    print("Willkommen zum Mail Generator!")


def print_mail_address(mail_adress):
    print(f"Ihre Mail-Adresse lautet: {mail_adress}")


def ask_for_name(name_type: str):
    while True:
        txt = input(f"Bitte tippen sie ihren {name_type} ein: ")
        if input_check(txt):
            return txt


def generate_mail_address(first_name: str, family_name: str):
    x = first_name
    return f"{x}.{family_name}@schule.bremen.de"


welcome()
firstname = ask_for_name("vornamen")
lastname = ask_for_name("Nachname")
print_mail_address(generate_mail_address(firstname, lastname))
