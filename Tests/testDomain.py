from Domain.Librarie import creeazaLibrarie, getId, getTitlu, getGen, getPret, getReducere


def testLibrarie():
    librarie = creeazaLibrarie("1", "Baltagul", "Traditionalism", 15, "none")

    assert getId(librarie) == "1"
    assert getTitlu(librarie) == "Baltagul"
    assert getGen(librarie) == "Traditionalism"
    assert getPret(librarie) == 15
    assert getReducere(librarie) == "none"
