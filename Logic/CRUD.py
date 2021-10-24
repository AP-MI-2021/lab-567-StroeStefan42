from Domain.Librarie import creeazaLibrarie, getId


def adaugaLibrarie(id, titlu, gen, pret, reducere, lista):
    librarie = creeazaLibrarie(id, titlu, gen, pret, reducere)
    return lista + [librarie]

def getById(id, lista):
    for librarie in lista:
        if getId(librarie) == id:
            return librarie
    return None

def stergeLibrarie(id, lista):
    return [librarie for librarie in lista if getId(librarie) != id]

def modificaLibrarie(id, titlu, gen, pret, reducere, lista):
    listaNoua = []
    for librarie in lista:
        if getId(librarie) == id:
            librarieNoua = creeazaLibrarie(id, titlu, gen, pret, reducere)
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua