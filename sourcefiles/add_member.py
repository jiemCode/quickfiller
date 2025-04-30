import logging
import string

from constants import UTILS_DIR
from member import Member

logging.basicConfig(filename=UTILS_DIR / "process.log",
                    filemode="a",
                    level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


def _set_school():
    schools = ["ESTI", "ESMGE", "ES2A", "ESU2A", "HEEG"]
    while True:
        i = int(input("Ecole (indice): "))
        try:
            return schools[i - 1]
        except ValueError:
            print("Entree invalide !")
            continue


def _validate_string(_string: str) -> str:
    _string = _string.strip(" ")
    for char in _string:
        if char in string.digits:
            logging.warning(f"Bad string {_string} expected")
            return _string
    else:
        if len(_string) > 21:
            logging.warning(f"String {_string} is too long...")
            return _string
    return _string


def _validate_number(number):
    for char in number:
        if char in string.ascii_letters:
            break
    else:
        return 1
    return 0


def _get_member(school: str = '', sex: str = '', number: str = '', first_name: str = '', last_name: str = '',
                address: str = '',
                commission_: str = '',
                phone_number: str = '',
                promo: str = '',
                project_name: str = ''):
    if first_name == '':
        first_name = input("Prenom: ")
        while not _validate_string(first_name):
            first_name = input("Prenom: ")
    first_name = _validate_string(first_name)

    if last_name == '':
        last_name = input("Nom: ")
        while not _validate_string(last_name):
            last_name = input("Nom: ")
    last_name = _validate_string(last_name)

    if address == '':
        address = input("Adresse: ")
        while not _validate_string(address):
            address = input("Adresse: ")

    # if commission == '':
    #     commission = input("Commission: ")
    #     while not _validate_string(commission):
    #         commission = input("Commission: ")
    # else:
    #     if commission.startswith("Com_"):
    #         commission = commission.split("_")[1]
    #         if ";" in commission:
    #             commission = commission.split(";")[0]
    #     else:
    #         commission = ""
    # commission = _validate_string(commission)

    if phone_number == '':
        phone_number = input("Telephone: ")
        while not _validate_number(phone_number):
            phone_number = input("Telephone: ")

    # if promo == '':
    #     promo = input("Promo: ")

    return {
        'number': number,
        'sex': sex,
        'first_name': first_name,
        'last_name': last_name,
        'address': address,
        'commission_': commission_,
        'phone_number': phone_number,
        'school': school,
        'promo': promo,
        'project_name': project_name,
    }


if __name__ == "__main__":
    def start_session():
        ask_school = "==> Choix de l'ecole : "
        ask_continue = "==> Ajouter un autre membre dans {} ? (y) "
        ask_confirm = "==> Confirmer ? (y) "
        print("""
    =======================================
          Programme d'ajout de membre     #
    =======================================
        """)
        print(ask_school + "1-ESTI ** 2-ESMGE ** 3-ES2A ** 4-ESU2A ** 5:HEEG")
        school = _set_school()
        print(f"==> Demarrage de l'ajout dans {school}")

        go_on = 'y'

        while go_on == 'y':

            print(20 * "-")
            data = _get_member(school)
            print(20 * "*")
            for elem in data.keys():
                print(f"{elem} : {data.get(elem)}")

            print(20 * "*")
            confirm = input(f"{ask_confirm}")
            if confirm == 'y':
                member = Member(**data)
                member.save_member()
                print("Membre ajoute avec success...")

            go_on = input(f"\n{ask_continue.format(school)}")
        print(f"Fin de l'ajout dans {school}\n\n\n")


    session = input("\nCommencer une session ? (y) ")
    while session == 'y':
        print(15 * "#")
        start_session()
        session = input("\nCommencer une session ? (y) ")
