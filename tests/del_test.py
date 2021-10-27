from Logic.Stergere import stergere_cheltuieli


def test_del():
    assert stergere_cheltuieli([{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}], '12') == []
    assert stergere_cheltuieli([{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}, {'numar_apartament': '6', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}], '12') == [{'numar_apartament': '6', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}]
