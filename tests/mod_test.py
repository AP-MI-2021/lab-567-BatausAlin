from Logic.Modificare import modificare_cheltuieli


def test_mod():
    assert modificare_cheltuieli([{'numar_apartament': '12', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}],
                                 '12', 'suma12', '17.05.2002', 'alte cheltuieli') == [
               {'numar_apartament': '12', 'suma': 'suma12', 'data': '17.05.2002', 'tip': 'alte cheltuieli'}]
    assert modificare_cheltuieli([{'numar_apartament': '15', 'suma': 'sum12', 'data': '11.12.2002', 'tip': 'canal'}],
                                 '15', 'suma12', '17.05.2002', 'intretinere') == [
               {'numar_apartament': '15', 'suma': 'suma12', 'data': '17.05.2002', 'tip': 'intretinere'}]

