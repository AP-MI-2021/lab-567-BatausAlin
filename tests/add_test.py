from Logic.Adaugare import adaugare_cheltuieli

def test_add():
    assert adaugare_cheltuieli([], '12', 'sum12', '11.12.2002', 'canal') == [{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}]
    assert adaugare_cheltuieli([], '5', 'suma5', '17.05.2002', 'intretinere') == [{'numar_apartament': '5', 'suma': 'suma5', 'data': '17.05.2002', 'tip': 'intretinere'}]
