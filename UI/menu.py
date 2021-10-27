from Logic.Adaugare import adaugare_cheltuieli
from Logic.Stergere import stergere_cheltuieli
from Logic.Modificare import modificare_cheltuieli


def print_menu_add_del_mod():
    print("""
1. Adauga inregistrare.
2. Modifica inregistrare.
3. Sterge inregistrare.
4. Afisare lista
4. Exit
""")


def menu_add_del_mod():
    lista = []
    while True:
        print_menu_add_del_mod()
        cmd = input("Introduceti comanda: ")
        if cmd == '1':
            nr_apartament = input("Introduceti numarul apartamentului: ")
            suma = input("Introduceti suma: ")
            data = input("Introduceti data de forma (DD.MM.YYYY): ")
            tip = input("Introduceti tipul cheltuielii (Intretinere, Canal, Alta cheltuiala): ")
            adaugare_cheltuieli(lista,nr_apartament, suma, data, tip)
        elif cmd == '2':
            nr_apartament = input("Introduceti numarul apartamentului: ")
            suma = input("Introduceti suma")
            data = input("Introduceti data de forma (DD.MM.YYYY): ")
            tip = input("Introduceti tipul cheltuielii (Intretinere, Canal, Alta cheltuiala): ")
            modificare_cheltuieli(lista, nr_apartament, suma, data, tip)
        elif cmd == '3':
            nr_apartament = input("Introduceti numarul apartamentului: ")
            stergere_cheltuieli(lista, nr_apartament)
        elif cmd == '4':
            print(lista)
        elif cmd == '5':
            break
        else:
            print("Instructiunea este gresita!")


