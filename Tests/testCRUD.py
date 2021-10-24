from Domain.Librarie import getId, getTitlu, getGen, getReducere, getPret
from Logic.CRUD import adaugaLibrarie, getById, stergeLibrarie, modificaLibrarie


def testAdaugaLibrarie():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getTitlu(getById("1", lista)) == "Baltagul"
    assert getGen(getById("1", lista)) == "Traditionalism"
    assert getPret(getById("1", lista)) == 15
    assert getReducere(getById("1", lista)) == "none"

def testStergeLibrarie():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = stergeLibrarie("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergeLibrarie("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None

def testModificaLibrarie():
    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)
    lista = adaugaLibrarie("2", "Ion", "Realism", 20, "silver", lista)

    lista = modificaLibrarie("1", "Enigma Otiliei", "Realism", 5, "gold", lista)

    librariaUpdatata = getById("1", lista)
    assert getId(librariaUpdatata) == "1"
    assert getTitlu(librariaUpdatata) == "Enigma Otiliei"
    assert getGen(librariaUpdatata) == "Realism"
    assert getPret(librariaUpdatata) == 5
    assert getReducere(librariaUpdatata) == "gold"

    librariaNeupdatata = getById("2", lista)
    assert getId(librariaNeupdatata) == "2"
    assert getTitlu(librariaNeupdatata) == "Ion"
    assert getGen(librariaNeupdatata) == "Realism"
    assert getPret(librariaNeupdatata) == 20
    assert getReducere(librariaNeupdatata) == "silver"

    lista = []
    lista = adaugaLibrarie("1", "Baltagul", "Traditionalism", 15, "none", lista)

    lista = modificaLibrarie("3", "Enigma Otiliei", "Realism", 5, "gold", lista)

    librariaNeupdatata = getById("1", lista)
    assert getId(librariaNeupdatata) == "1"
    assert getTitlu(librariaNeupdatata) == "Baltagul"
    assert getGen(librariaNeupdatata) == "Traditionalism"
    assert getPret(librariaNeupdatata) == 15
    assert getReducere(librariaNeupdatata) == "none"