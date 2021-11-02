from Logic.Adaugare import adaugare_cheltuieli
from Logic.Stergere import stergere_cheltuieli
from Logic.Modificare import modificare_cheltuieli
from Logic.determinare_cheltuieli import determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli

from Domain.cheltuieli import to_string

from Logic.ordonare_cheltuieli import ordonare_cheltuieli_desc


def print_menu_add_del_mod():
    print("""
1. Adaugă înregistrare.
2. Modifica înregistrare.
3. Șterge înregistrare.
4. Determinare max cheltuieli in următoarea ordine (întreținere, canal, alte cheltuieli). 
5. Ordonare lista in ordine descrescătoare după sumă. 
6. Afișare lista. 
x. Exit
""")


def menu_add_del_mod():
    lista = [{'numar_apartament': '12', 'suma': '1024', 'data': '11.12.2002', 'tip': 'canal'},
         {'numar_apartament': '12', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
             {'numar_apartament': '12', 'suma': '112.32', 'data': '11.12.2002', 'tip': 'alte cheltuieli'},
             {'numar_apartament': '12', 'suma': '5132.321', 'data': '11.12.2002', 'tip': 'canal'}]
    while True:
        print_menu_add_del_mod()
        cmd = input("Introduceți comanda: ")
        if cmd == '1':
            nr_apartament = input("Introduceți numărul apartamentului: ")
            suma = input("Introduceți suma: ")
            data = input("Introduceți data de forma (DD.MM.YYYY): ")
            tip = input("Introduceți tipul cheltuielii (Întreținere, Canal, Alta cheltuiala): ")
            adaugare_cheltuieli(lista, nr_apartament, suma, data, tip)
        elif cmd == '2':
            nr_apartament = input("Introduceți numărul apartamentului: ")
            suma = input("Introduceți suma: ")
            data = input("Introduceți data de forma (DD.MM.YYYY): ")
            tip = input("Introduceți tipul cheltuielii (Întreținere, Canal, Alta cheltuiala): ")
            modificare_cheltuieli(lista, nr_apartament, suma, data, tip)
        elif cmd == '3':
            nr_apartament = input("Introduceți numărul apartamentului: ")
            stergere_cheltuieli(lista, nr_apartament)
        elif cmd == '4':
            intretinere, canal, alte_cheltuieli = determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(lista)
            print(f"Întreținere: {intretinere}")
            print(f"Canal: {canal}")
            print(f"alte cheltuieli: {alte_cheltuieli}")
        elif cmd == '5':
            print(ordonare_cheltuieli_desc(lista))
            pass
        elif cmd == '6':
            to_string(lista)
        elif cmd == 'x':
            break
        else:
            print("Instrucțiunea este greșită!")
