from Domain.cheltuieli import to_string
from Logic.Adaugare import adaugare_cheltuieli
from Logic.Stergere import stergere_cheltuieli
from Logic.Validare import validare_inputs, validare_numar_apartament


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
    while True:
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
                for elem in lista_command_line:
                    print(to_string(elem))
            elif el_split[0] == 'b':
                break
            elif el_split[0] == 'h':
                print_command_line_help_console()
            elif el_split[0] == 'x':
                print('execut x')

    return lista_command_line
