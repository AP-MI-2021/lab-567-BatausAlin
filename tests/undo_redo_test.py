from Domain.lista_undo_redo import create_cheltuieli
from Logic.Adaugare import adaugare_cheltuieli
from Logic.undo_redo import apply_undo, apply_redo


def test_undo_redo():
    get_cheltuieli = create_cheltuieli()
    assert get_cheltuieli['listaCurenta'] == []
    adaugare_cheltuieli(get_cheltuieli, 'o1', '7', '24', '11.12.2002', 'intretinere')
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'}]
    adaugare_cheltuieli(get_cheltuieli, 'o2', '7', '24', '11.12.2002', 'canal')
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'}]
    adaugare_cheltuieli(get_cheltuieli, 'o3', '7', '24', '11.12.2002', 'alte cheltuieli')
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'},
        {'id': 'o3', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]

    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'}]
    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'}]
    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == []

    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == []

    adaugare_cheltuieli(get_cheltuieli, 'o1', '7', '24', '11.12.2002', 'intretinere')
    adaugare_cheltuieli(get_cheltuieli, 'o2', '7', '24', '11.12.2002', 'canal')
    adaugare_cheltuieli(get_cheltuieli, 'o3', '7', '24', '11.12.2002', 'alte cheltuieli')
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'},
        {'id': 'o3', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]
    apply_redo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'},
        {'id': 'o3', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]

    apply_undo(get_cheltuieli)
    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'}]
    apply_redo(get_cheltuieli)

    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'}]
    apply_redo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o2', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'canal'},
        {'id': 'o3', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]

    apply_undo(get_cheltuieli)
    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'}]

    adaugare_cheltuieli(get_cheltuieli, 'o4', '7', '24', '11.12.2002', 'alte cheltuieli')
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o4', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]
    apply_redo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o4', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]
    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'}]
    apply_undo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == []
    apply_redo(get_cheltuieli)
    apply_redo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o4', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]
    apply_redo(get_cheltuieli)
    assert get_cheltuieli['listaCurenta'] == [
        {'id': 'o1', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'intretinere'},
        {'id': 'o4', 'numar_apartament': '7', 'suma': '24', 'data': '11.12.2002', 'tip': 'alte cheltuieli'}]
