
def creeazaLibrarie(id, titlu, gen, pret, reducere):
    list=[]
    list.append(id)
    list.append(titlu)
    list.append(gen)
    list.append(pret)
    list.append(reducere)
    return list



def getId(librarie):
    return librarie[0]

def getTitlu(librarie):
    return librarie[1]

def getGen(librarie):
    return librarie[2]

def getPret(librarie):
    return librarie[3]

def getReducere(librarie):
    return librarie[4]

def toString(librarie):
    return "Id: {}, Titlu: {}, Gen: {}, Pret: {}, Reducere: {}".format(
        getId(librarie),
        getTitlu(librarie),
        getGen(librarie),
        getPret(librarie),
        getReducere(librarie),
    )