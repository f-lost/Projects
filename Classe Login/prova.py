from modulo_menu import Menu, Elemento, Azione
from modulo_login import Utente, SistemaLogin


# Definizione delle azioni di esempio
def registrazione():

    login.registra_utente(username, password, domanda_segreta)   

def equazione():

    eq.start(utente)   

def ringrazia():
    print("Grazie per aver utilizzato il menu!")





menu = Menu()
utente = Utente("stefi")
login = SistemaLogin()



elemento1 = Elemento("Indovina il Numero", Azione(numero))
elemento2 = Elemento("Addio", Azione(equazione))
elemento3 = Elemento("Ringraziamento", Azione(ringrazia))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)

# Mostra il menu ripetibile
menu.mostra_menu()