from modulo_menu import Menu, Elemento, Azione
from modulo_login import Utente, SistemaLogin


# Definizione delle azioni di esempio


def registrazione():

    username = input("Inserisci l'username").lower()
    if not login.controlla_utente(username):
        password = input("Inserisci una password: ").lower()
        domanda_segreta = input("Qual era il nome della tua scuola elementare?: ").lower()
        login.crea_nuovo_utente(username, password, domanda_segreta)
    else:
        print("Utente già registrato, inserisci la password: ")
        password = input("Inserisci la password: ").lower()
        login.login(username, password)

def login():
    
    username = input("Inserisci l'username") 
    if login.controlla_utente(username):

        password = input("Inserisci la password: ")
        login.login(username, password)
    
    else: 

        print("Utente non trovato. Registrarsi.")
        menu.mostra_menu()

def reset_password():

    login.reset_password(username)

def cambia_username():

    login.cambia_username(old_username, new_username)




menu = Menu()
login = SistemaLogin()



elemento1 = Elemento("Registrazione", Azione(registrazione))
elemento2 = Elemento("Login", Azione(login))
elemento3 = Elemento("Ringraziamento", Azione(ringrazia))

menu.aggiungi_elemento(elemento1)
menu.aggiungi_elemento(elemento2)
menu.aggiungi_elemento(elemento3)

# Mostra il menu ripetibile
menu.mostra_menu()