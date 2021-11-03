from Domain.Librarie2 import toString, getId
from Logic.CRUD import adaugaLibrarie, getById


def print_help():
    print("Comenzi disponibile: ")
    print("Ajutor: ")
    print("Adauga vanzare: adauga, id, titlu, gen, pret, reducere ")
    print("Sterge vanzare: sterge, id ")
    print("Afisare: showall ")
    print("Stop ")
    print("Parametrii trebuie separati prin virgula. ")
    print("Comenzile trebuie separate prin ; ")

def adauga(lista, parametrii):
    id = str(parametrii[1])
    titlu = str(parametrii[2])
    gen = str(parametrii[3])
    pret = float(parametrii[4])
    reducere = str(parametrii[5])
    lista = adaugaLibrarie(id, titlu, gen, pret, reducere, lista)
    print("Adaugare efectuata")
    return lista

def sterge(lista, parametrii):
    id = int(parametrii[1])
    if getById(id, lista) is None:
        raise ValueError("Nu exista vanzare cu Id-ul dat")
    return [librarie for librarie in lista if getId(librarie)!=id]

def showall(lista):
    for librarie in lista:
        print(toString(librarie))

def run_console(lista):
    contor = True
    while contor:
        comenzi = input("Introduceti comenzile (Ajutor, Adauga, Sterge, Afisare, Stop): ")
        functii = comenzi.split(";")
        for functie in functii:
            parametrii = functie.split(",")
            if(parametrii[0] == "Ajutor"):
                print_help()
            elif parametrii[0] == "Adauga":
                lista = adauga(lista, parametrii)
            elif parametrii[0] == "Sterge":
                lista = sterge(lista, parametrii)
            elif parametrii[0] == "Afisare":
                print("Lista de vanzari este: ")
                showall(lista)
            elif parametrii[0] == "Stop":
                contor = False