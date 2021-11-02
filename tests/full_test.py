from Logic.Stergere import stergere_cheltuieli  # test_delete
from Logic.Adaugare import adaugare_cheltuieli  # test_add
from Logic.Modificare import modificare_cheltuieli  # test_modify
from Logic.determinare_cheltuieli import \
    determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli  # test_determinare_max_cheltuieli
from Logic.ordonare_cheltuieli import ordonare_cheltuieli_desc  # test_ordonare_cheltuieli_desc


def test_add():
    assert adaugare_cheltuieli([], '12', 'sum12', '11.12.2002', 'canal') == [
        {'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}]
    assert adaugare_cheltuieli([], '5', 'suma5', '17.05.2002', 'intretinere') == [
        {'numar_apartament': '5', 'suma': 'suma5', 'data': '17.05.2002', 'tip': 'intretinere'}]


def test_delete():
    assert stergere_cheltuieli([{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}],
                               '12') == []
    assert stergere_cheltuieli([{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'},
                                {'numar_apartament': '6', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}],
                               '12') == [
               {'numar_apartament': '6', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}]


def test_modify():
    assert modificare_cheltuieli([{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}],
                                 '12', 'suma12', '17.05.2002', 'alte cheltuieli') == [
               {'numar_apartament': '12', 'suma': 'suma12', 'data': '17.05.2002', 'tip': 'alte cheltuieli'}]
    assert modificare_cheltuieli([{'numar_apartament': '15', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}],
                                 '15', 'suma12', '17.05.2002', 'intretinere') == [
               {'numar_apartament': '15', 'suma': 'suma12', 'data': '17.05.2002', 'tip': 'intretinere'}]


def test_determinare_max_cheltuieli():
    assert determinare_max_cheltuieli_pentru_fiecare_tip_de_cheltuieli(
        [{'numar_apartament': '12', 'suma': '1024', 'data': '11.12.2002', 'tip': 'canal'}
            , {'numar_apartament': '12', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
         {'numar_apartament': '12', 'suma': '12.32', 'data': '11.12.2002', 'tip': 'alte cheltuieli'},
         {'numar_apartament': '12', 'suma': '132.321', 'data': '11.12.2002', 'tip': 'canal'}]) == [24.0, 1024.0, 12.32]


def test_ordonare_cheltuieli_desc():
    assert ordonare_cheltuieli_desc([{'numar_apartament': '12', 'suma': '1024', 'data': '11.12.2002', 'tip': 'canal'}
                                        , {'numar_apartament': '12', 'suma': '24', 'data': '11.12.2002',
                                           'tip': 'intretinere'},
                                     {'numar_apartament': '12', 'suma': '12.32', 'data': '11.12.2002',
                                      'tip': 'alte cheltuieli'},
                                     {'numar_apartament': '12', 'suma': '132.321', 'data': '11.12.2002',
                                      'tip': 'canal'}]) == [
               {'numar_apartament': '12', 'suma': '1024', 'data': '11.12.2002', 'tip': 'canal'},
               {'numar_apartament': '12', 'suma': '132.321', 'data': '11.12.2002', 'tip': 'canal'},
               {'numar_apartament': '12', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
               {'numar_apartament': '12', 'suma': '12.32', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}
           ]


def testele():
    test_add()
    test_delete()
    test_modify()
    test_determinare_max_cheltuieli()
    test_ordonare_cheltuieli_desc()
