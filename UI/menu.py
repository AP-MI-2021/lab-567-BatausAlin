from Domain.lista_undo_redo import create_cheltuieli, get_lista_curenta
from Logic.Adaugare import adaugare_cheltuieli
from Logic.Stergere import stergere_cheltuieli, stergere_totala_cheltuieli_camera
from Logic.Modificare import modificare_cheltuieli
from Logic.afisare_sume_lunare import afisare_sume_lunare
from Logic.determinare_cheltuieli import determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli
from Logic.Validare import validare_inputs, validare_numar_apartament
from Domain.cheltuieli import to_string

from Logic.ordonare_cheltuieli import ordonare_cheltuieli_desc
from Logic.undo_redo import apply_redo, apply_undo

from UI.command_line import command_line_console


def print_menu_add_del_mod():
    print("""
1. Adaugă înregistrare.
2. Modifica înregistrare.
3. Șterge înregistrare.
4. Ștergerea tuturor cheltuielilor pentru un apartament dat.
5. Determinare max cheltuieli in următoarea ordine (întreținere, canal, alte cheltuieli). 
6. Ordonare lista in ordine descrescătoare după sumă.
7. Afișare lista.
8. Afișarea sumelor lunare pentru fiecare apartament.
g. command line console.
u. Undo 
r. Redo  
x. Exit
""")

def menu_add_del_mod():
    lista = create_cheltuieli()
    adaugare_cheltuieli(lista, '1', '15', '5', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(lista, '2', '32', '13', '13.12.2002', 'canal')
    adaugare_cheltuieli(lista, '3', '44', '99.99', '11.12.2021', 'alte cheltuieli')
    adaugare_cheltuieli(lista, '4', '102', '11.23', '15.12.2021', 'canal')
    adaugare_cheltuieli(lista, '5', '99', '12.21', '17.05.2002', 'intretinere')
    while True:
        print_menu_add_del_mod()
        cmd = input("Introduceți comanda: ")
        if cmd == '1':
            id = input("Introduceți ID-ul: ")
            nr_apartament = input("Introduceți numărul apartamentului: ")
            suma = input("Introduceți suma: ")
            data = input("Introduceți data de forma (DD.MM.YYYY): ")
            tip = input("Introduceți tipul cheltuielii (Întreținere, Canal, Alta cheltuiala): ")
            try:
                validare_inputs(id, nr_apartament, suma, data, tip)
                adaugare_cheltuieli(lista, id, nr_apartament, suma, data, tip)
            except ValueError as ve:
                print(ve)

        elif cmd == '2':
            nr_apartament = input("Introduceți numărul apartamentului: ")
            id = input("Introduceți ID-ul: ")
            suma = input("Introduceți suma: ")
            data = input("Introduceți data de forma (DD.MM.YYYY): ")
            tip = input("Introduceți tipul cheltuielii (Întreținere, Canal, Alta cheltuiala): ")

            try:
                validare_inputs(id, nr_apartament, suma, data, tip)
                modificare_cheltuieli(lista, id, nr_apartament, suma, data, tip)
            except ValueError as ve:
                print(ve)

        elif cmd == '3':
            nr_apartament = input("Introduceți numărul apartamentului: ")
            try:
                validare_numar_apartament(nr_apartament)
                stergere_cheltuieli(lista, nr_apartament)
            except ValueError as vs:
                print(vs)
        elif cmd == '4':
            apartament = input("Introduceți numărul apartamentului: ")
            try:
                validare_numar_apartament(apartament)
                stergere_totala_cheltuieli_camera(lista, apartament)
            except ValueError as vs:
                print(vs)

            pass
        elif cmd == '5':
            intretinere, canal, alte_cheltuieli = determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(lista)
            print(f"Întreținere: {intretinere}")
            print(f"Canal: {canal}")
            print(f"alte cheltuieli: {alte_cheltuieli}")
        elif cmd == '6':
            ordonare_cheltuieli_desc(lista)
            print("Lista a fost ordonată cu succes !!!")
            pass
        elif cmd == '7':
            for elem in get_lista_curenta(lista):
                print(to_string(elem))
        elif cmd == '8':
            get_lista = get_lista_curenta(lista)
            for_for = afisare_sume_lunare(get_lista)
            for elem in for_for:
                print(elem, for_for[elem])
        elif cmd == 'g':
            if command_line_console() == -1:
                break
            else:
                lista.append(command_line_console())
        elif cmd == 'u':
            apply_undo(lista)
            print('Undo facut cu succes')
            pass
        elif cmd == 'r':
            apply_redo(lista)
            print('Redo facut cu succes')
            pass
        elif cmd == 'x':
            break
        else:
            print("Instrucțiunea este greșită!")
