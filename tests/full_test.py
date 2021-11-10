from Domain.cheltuieli import creare_cheltuiala, get_id, get_suma
from Domain.lista_undo_redo import create_cheltuieli, get_lista_curenta
from Logic.Stergere import stergere_cheltuieli, \
    stergere_totala_cheltuieli_camera  # test_delete, test_stergere_totala_cheltuieli
from Logic.Adaugare import adaugare_cheltuieli  # test_add
from Logic.Modificare import modificare_cheltuieli  # test_modify
from Logic.afisare_sume_lunare import afisare_sume_lunare
from Logic.determinare_cheltuieli import \
    determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli  # test_determinare_max_cheltuieli
from Logic.ordonare_cheltuieli import ordonare_cheltuieli_desc  # test_ordonare_cheltuieli_desc
from Logic.adunare_valoare import adunare_valoare

""" Functie Terminata !!!!"""


def test_add():
    get_cheltuieli = create_cheltuieli()
    cheltuiala_adaugata = creare_cheltuiala('2', '7', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '2', '7', '24', '11.12.2002', 'intretinere')
    lista_curenta = get_lista_curenta(get_cheltuieli)
    assert len(get_lista_curenta(get_cheltuieli)) == 1
    assert lista_curenta[0] == cheltuiala_adaugata
    assert get_id(lista_curenta[0]) == '2'

    adaugare_cheltuieli(get_cheltuieli, '3', '7', '24', '11.12.2015', 'canal')
    cheltuiala_adaugata_2 = creare_cheltuiala('3', '7', '24', '11.12.2015', 'canal')
    assert len(lista_curenta) == 2
    assert lista_curenta[0] == cheltuiala_adaugata
    assert lista_curenta[1] == cheltuiala_adaugata_2


""" Functie Terminata !!!!"""


def test_modify():
    get_cheltuieli = create_cheltuieli()
    cheltuiala_adaugata = creare_cheltuiala('2', '7', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '2', '7', '24', '11.12.2002', 'intretinere')
    cheltuiala_adaugata_2 = creare_cheltuiala('3', '4', '54', '17.5.2002', 'canal')
    adaugare_cheltuieli(get_cheltuieli, '3', '4', '54', '17.5.2002', 'canal')

    lista_curenta = get_lista_curenta(get_cheltuieli)

    assert len(lista_curenta) == 2
    modificare_cheltuieli(get_cheltuieli, '2', '17', '245', '9.11.2021', 'alte cheltuieli')
    assert len(lista_curenta) == 2
    assert get_id(cheltuiala_adaugata) == '2'
    assert get_id(cheltuiala_adaugata_2) == '3'


""" Functie Terminata !!!!"""


def test_delete():
    get_cheltuieli = create_cheltuieli()
    adaugare_cheltuieli(get_cheltuieli, '2', '11', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '3', '5', '54', '17.5.2002', 'canal')

    lista_curenta = get_lista_curenta(get_cheltuieli)
    assert len(lista_curenta) == 2
    stergere_cheltuieli(get_cheltuieli, '5')
    assert len(lista_curenta) == 1
    adaugare_cheltuieli(get_cheltuieli, '3', '17', '54', '17.5.2002', 'canal')
    stergere_cheltuieli(get_cheltuieli, '17')
    stergere_cheltuieli(get_cheltuieli, '11')
    assert len(lista_curenta) == 0
    adaugare_cheltuieli(get_cheltuieli, '3', '17', '54', '17.5.2002', 'canal')
    assert len(lista_curenta) == 1


""" Functie Terminata !!!!"""


def test_stergere_totala_cheltuieli():
    get_cheltuieli = create_cheltuieli()
    adaugare_cheltuieli(get_cheltuieli, '4', '1', '54', '17.5.2002', 'alte cheltuieli')
    adaugare_cheltuieli(get_cheltuieli, '2', '7', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '1', '7', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '3', '7', '54', '17.5.2002', 'canal')
    lista_curenta = get_lista_curenta(get_cheltuieli)
    stergere_totala_cheltuieli_camera(get_cheltuieli, '7')


""" Functie Terminata !!!!"""


def test_determinare_max_cheltuieli():
    get_cheltuieli = create_cheltuieli()
    adaugare_cheltuieli(get_cheltuieli, '1', '17', '123', '11.12.2020', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '3', '55', '123', '17.5.2021', 'canal')
    adaugare_cheltuieli(get_cheltuieli, '2', '13', '123', '17.5.2022', 'alte cheltuieli')
    lista_curenta = get_lista_curenta(get_cheltuieli)
    assert determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(get_cheltuieli) == [123.0, 123.0, 123.0]
    adaugare_cheltuieli(get_cheltuieli, '5', '6', '1234', '10.11.2021', 'canal')
    assert determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(get_cheltuieli) == [123.0, 1234.0, 123.0]
    adaugare_cheltuieli(get_cheltuieli, '5', '6', '1234', '10.11.2021', 'alte cheltuieli')
    assert determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(get_cheltuieli) == [123.0, 1234.0, 1234.0]


""" Functie Terminata !!!!"""


def test_ordonare_cheltuieli_desc():
    get_cheltuieli = create_cheltuieli()
    adaugare_cheltuieli(get_cheltuieli, '1', '17', '1', '11.12.2020', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '3', '55', '2', '17.5.2021', 'canal')
    adaugare_cheltuieli(get_cheltuieli, '2', '13', '3', '17.5.2022', 'alte cheltuieli')
    lista_curenta = get_lista_curenta(get_cheltuieli)
    ordonare_cheltuieli_desc(get_cheltuieli)

    assert get_id(lista_curenta[0]) == '2'
    assert get_id(lista_curenta[1]) == '3'
    assert get_suma(lista_curenta[2]) == '1'
    assert get_suma(lista_curenta[0]) == '3'


""" Functie Terminata !!!!"""


def test_adunare_valoare_data():
    get_cheltuieli = create_cheltuieli()
    adaugare_cheltuieli(get_cheltuieli, '2', '7', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, '1', '17', '245', '10.11.2021', 'canal')
    lista_curenta = get_lista_curenta(get_cheltuieli)
    adunare_valoare(get_cheltuieli, '10.11.2021', '1')
    assert get_suma(lista_curenta[1]) == '246.0'
    adunare_valoare(get_cheltuieli, '10.11.2021', '1')
    assert get_suma(lista_curenta[1]) == '247.0'
    pass


""" Functie Terminata !!!!"""


def test_afisare_sume_lunare():
    lista = [{"id": '1', 'numar_apartament': '12', 'suma': '1', 'data': '11.5.2002', 'tip': 'canal'},
             {"id": '2', 'numar_apartament': '7', 'suma': '1', 'data': '11.1.2002', 'tip': 'intretinere'},
             {"id": '3', 'numar_apartament': '12', 'suma': '1', 'data': '11.5.2002', 'tip': 'alte cheltuieli'},
             {"id": '4', 'numar_apartament': '8', 'suma': '1', 'data': '11.2.2002', 'tip': 'canal'},
             {"id": '5', 'numar_apartament': '12', 'suma': '1', 'data': '11.3.2002', 'tip': 'alte cheltuieli'},
             {"id": '5', 'numar_apartament': '12', 'suma': '112.123', 'data': '11.3.2002', 'tip': 'alte cheltuieli'}]
    assert afisare_sume_lunare(lista) == {'Apartamentul 12 luna 5 suma este:': 2.0,
                                          'Apartamentul 7 luna 1 suma este:': 1.0,
                                          'Apartamentul 8 luna 2 suma este:': 1.0,
                                          'Apartamentul 12 luna 3 suma este:': 113.123}


def testele():
    test_add()
    test_modify()
    test_delete()
    test_stergere_totala_cheltuieli()
    test_determinare_max_cheltuieli()
    test_ordonare_cheltuieli_desc()
    test_adunare_valoare_data()
    test_afisare_sume_lunare()
