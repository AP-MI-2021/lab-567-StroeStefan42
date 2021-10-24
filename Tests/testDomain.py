from Domain.Librarie import creeazaLibrarie, getId, getTitlu, getGen, getPret, getReducere


def testLibrarie():
    librarie = creeazaLibrarie("1", "tiramisu", "italiana", 15, "none")

    assert getId(librarie) == "1"
    assert getTitlu(librarie) == "tiramisu"
    assert getGen(librarie) == "italiana"
    assert getPret(librarie) == 15
    assert getReducere(librarie) == "none"
