from Domain.Librarie import creeazaLibrarie, getId


def adaugaLibrarie(id, titlu, gen, pret, reducere, lista):
    if getById(id, lista) is not None:
        raise ValueError("Id-ul exista deja")
    librarie = creeazaLibrarie(id, titlu, gen, pret, reducere)
    return lista + [librarie]

def getById(id, lista):
    for librarie in lista:
        if getId(librarie) == id:
            return librarie
    return None

def stergeLibrarie(id, lista):
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    return [librarie for librarie in lista if getId(librarie) != id]

def modificaLibrarie(id, titlu, gen, pret, reducere, lista):
    if getById(id, lista) is None:
        raise ValueError("Nu exista o librarie cu id-ul dat")
    listaNoua = []
    for librarie in lista:
        if getId(librarie) == id:
            librarieNoua = creeazaLibrarie(id, titlu, gen, pret, reducere)
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua