from Domain.Librarie import getId, creeazaLibrarie, getGen, getTitlu, getPret, getReducere

def discount(lista):
    listaNoua=[]
    for librarie in lista:
        if getReducere(librarie)=="silver":
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                getGen(librarie),
                getPret(librarie)  - (0.05 * getPret(librarie)),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        elif getReducere(librarie)=="gold":
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                getGen(librarie),
                getPret(librarie) - (0.1 * getPret(librarie)),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua

def modificareGen(numeOriginal, numeSchimbat, lista):
    listaNoua = []
    for librarie in lista:
        if numeOriginal == getGen(librarie):
            librarieNoua = creeazaLibrarie(
                getId(librarie),
                getTitlu(librarie),
                numeSchimbat ,
                getPret(librarie),
                getReducere(librarie)
            )
            listaNoua.append(librarieNoua)
        else:
            listaNoua.append(librarie)
    return listaNoua