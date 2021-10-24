from Domain.Librarie import toString
from Logic.CRUD import adaugaLibrarie, stergeLibrarie, modificaLibrarie


def printMenu():
    print("1. Adaugare carte")
    print("2. Stergere carte")
    print("3. Modificare carte")
    print("a. Afisare carti")
    print("x. Iesire")


def uiAdaugaLibrarie(lista):
    id = input("Dati id-ul: ")
    titlu = input("Dati titlul: ")
    gen = input("Dati genul: ")
    pret = float(input('Dati pretul: '))
    reducere = input("Dati tipul de reducere: ")
    return adaugaLibrarie(id, titlu, gen, pret, reducere, lista)


def uiStergeLibrarie(lista):
    id = input("Dati id-ul cartii de sters: ")
    return stergeLibrarie(id, lista)


def uiModificaLibrarie(lista):
    id = input("Dati id-ul cartii de modificat: ")
    titlu = input("Dati noul titlu: ")
    gen = input("Dati noul gen: ")
    pret = float(input('Dati noul pret: '))
    reducere =input("Dati noul tip de reducere: ")
    return modificaLibrarie(id, titlu, gen, pret, reducere, lista)


def showAll(lista):
    for librarie in lista:
        print(toString(librarie))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugaLibrarie(lista)
        elif optiune == "2":
            lista = uiStergeLibrarie(lista)
        elif optiune == "3":
            lista = uiModificaLibrarie(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")