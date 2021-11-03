from Logic.Adaugare import adaugare_cheltuieli
from Logic.Stergere import stergere_cheltuieli, stergere_totala_cheltuieli_camera
from Logic.Modificare import modificare_cheltuieli
from Logic.determinare_cheltuieli import determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli
from Logic.Validare import validare_inputs, validare_numar_apartament
from Domain.cheltuieli import to_string

from Logic.ordonare_cheltuieli import ordonare_cheltuieli_desc


# add,15,55,123,11.12.2021,intretinere;showall

def print_command_line_help_console():
    print("""
Trebuie să putem da comenzi dupa cum urmeaza:
    -add, 1, nume, descriere, 32, 321, 2000;
    -showall;
    -delete, 3
Totul pe o singură linie și să fie executate toate.
Separatorii pot fi orice.
Să implementeze minim 3 comenzi.
Implementarea trebuie facuta într-un fișier nou.
Noua interfata trebuie sa aiba si un help afisat care explica cum trebuie folosite comenzile
""")


def print_command_line_console():
    print("""
showall. Nu știu încă.
add. Adaugă ceva.
delete. Șterge ceva.
b. Back.
h. Help
x. Exit. (E bug încă n-am găsit rezolvare.)
""")


def command_line_console():
    lista_command_line = []
    stop = True
    while True and stop:
        print_command_line_console()
        cmd = input('Introduceți comanda: ')
        cmd_split = cmd.split(';')
        for el in range(0, len(cmd_split)):
            el_split = cmd_split[el].split(',')
            if el_split[0] == 'add':

                id_ul = el_split[1]
                nr_apartament = el_split[2]
                suma = el_split[3]
                data = el_split[4]
                tip = el_split[5]
                try:
                    validare_inputs(id_ul, nr_apartament, suma, data, tip)
                    adaugare_cheltuieli(lista_command_line, id_ul, nr_apartament, suma, data, tip)
                except ValueError as ve:
                    print(ve)

            elif el_split[0] == 'delete':
                # print('Aici execut delete command:')
                nr_apartament = el_split[1]
                try:
                    validare_numar_apartament(nr_apartament)
                    stergere_cheltuieli(lista_command_line, nr_apartament)
                except ValueError as vs:
                    print(vs)
            elif el_split[0] == 'showall':
                # print('Aici execut showall: ')
                for elem in lista_command_line:
                    print(to_string(elem))
            elif el_split[0] == 'b':
                menu_add_del_mod()
            elif el_split[0] == 'h':
                print_command_line_help_console()
            elif el_split[0] == 'x':
                print('execut x')
                stop = False
    return lista_command_line


def print_menu_add_del_mod():
    print("""
1. Adaugă înregistrare.
2. Modifica înregistrare.
3. Șterge înregistrare.
4. Ștergerea tuturor cheltuielilor pentru un apartament dat.  ####
5. Determinare max cheltuieli in următoarea ordine (întreținere, canal, alte cheltuieli). 
6. Ordonare lista in ordine descrescătoare după sumă.  ####
7. Afișare lista.
g. command line console. 
x. Exit
""")


def menu_add_del_mod():
    lista = [{"id": '1', 'numar_apartament': '12', 'suma': '1024', 'data': '11.12.2002', 'tip': 'canal'},
             {"id": '2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
             {"id": '3', 'numar_apartament': '12', 'suma': '112.32', 'data': '11.12.2002', 'tip': 'alte cheltuieli'},
             {"id": '4', 'numar_apartament': '8', 'suma': '5132.321', 'data': '11.12.2002', 'tip': 'canal'},
             {"id": '5', 'numar_apartament': '12', 'suma': '2132.321', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]
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
            for elem in lista:
                print(to_string(elem))
        elif cmd == 'g':
            lista.append(command_line_console())
        elif cmd == 'x':
            break
        else:
            print("Instrucțiunea este greșită!")
