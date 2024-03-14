import os
import re
import requests
import time
from colorama import Fore, Style
from googlesearch import search

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)  
    print()

def cerca_informazioni(nome, cognome, città):
    query = f"{nome} {cognome} {città} -site:linkedin.com -site:facebook.com -site:twitter.com"
    risultati = []

    try:
        for j in search(query, num=10, stop=10, pause=2):
            risultati.append(j)
    except Exception as e:
        pass

    return risultati

def ottieni_numeri_telefono(risultati):
    numeri_telefono = []
    phone_pattern = r'\b(?:\+?39)?\s?(?:0[1-9][0-9])\s?\d{5,10}\b'  

    for link in risultati:
        try:
            response = requests.get(link)
            if response.status_code == 200:
                matches = re.findall(phone_pattern, response.text)
                numeri_telefono.extend(matches)
        except Exception as e:
            pass

    return numeri_telefono

def stampa_introduzione():
    clear_screen()
    type_writer_effect(f"{Fore.CYAN}Benvenuto al programma di ricerca! questo tool fa parte della raccolta di t.me/VikingTERMINAL\n{Style.RESET_ALL}")

def stampa_numeri_telefono(numeri_telefono):
    clear_screen()
    if numeri_telefono:
        type_writer_effect(f"{Fore.GREEN}Numeri di telefono trovati:{Style.RESET_ALL}")
        for numero in numeri_telefono:
            print(numero)
        
        risposta = input(f"\n{Fore.YELLOW}Vuoi salvare i numeri di telefono trovati in un file di testo? (yes/no): {Style.RESET_ALL}").lower()
        if risposta == "yes":
            
            nome_file = "numeri_telefono.txt"
            with open(nome_file, "w") as file:
                for numero in numeri_telefono:
                    file.write(numero + "\n")
            print(f"{Fore.GREEN}I numeri di telefono sono stati salvati nel file {nome_file}.{Style.RESET_ALL}")
        elif risposta != "no":
            print(f"{Fore.RED}Risposta non valida. I numeri di telefono non saranno salvati.{Style.RESET_ALL}")
    else:
        type_writer_effect(f"{Fore.GREEN}Nessun numero di telefono trovato.{Style.RESET_ALL}")

def main():
    stampa_introduzione()

    nome = input(f"{Fore.YELLOW}Inserisci il nome: {Style.RESET_ALL}")
    cognome = input(f"{Fore.YELLOW}Inserisci il cognome: {Style.RESET_ALL}")
    città = input(f"{Fore.YELLOW}Inserisci la città: {Style.RESET_ALL}")

    risultati = cerca_informazioni(nome, cognome, città)
    numeri_telefono = ottieni_numeri_telefono(risultati)

    stampa_numeri_telefono(numeri_telefono)

if __name__ == "__main__":
    main()
