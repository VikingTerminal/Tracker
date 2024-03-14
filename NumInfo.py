import os
import re
import requests
import time
from bs4 import BeautifulSoup
from colorama import Fore, Style

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_writer_effect(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

def cerca_informazioni(numero_telefono, api_key=None):
    risultati = []

    try:
        if api_key:
            response = requests.get(f"https://www.google.com/search?q={numero_telefono}&key={api_key}")
        else:
            response = requests.get(f"https://www.google.com/search?q={numero_telefono}")
            
        response.raise_for_status()  
        soup = BeautifulSoup(response.text, 'html.parser')
        search_results = soup.find_all('div', class_='BNeawe deIvCb AP7Wnd')
        for result in search_results:
            info = result.get_text(strip=True)
            risultati.append(info)
    except requests.RequestException as e:
        print(f"{Fore.RED}Errore nella richiesta HTTP: {e}{Style.RESET_ALL}")
    except Exception as e:
        print(f"{Fore.RED}Errore imprevisto: {e}{Style.RESET_ALL}")

    return risultati

def stampa_introduzione():
    clear_screen()
    type_writer_effect(f"{Fore.CYAN}Benvenuto al programma di ricerca! Questo tool fa parte della raccolta di t.me/VikingTERMINAL\n{Style.RESET_ALL}")

def stampa_risultati(risultati):
    clear_screen()
    if risultati:
        type_writer_effect(f"{Fore.GREEN}Dettagli trovati:{Style.RESET_ALL}")
        for risultato in risultati:
            print(risultato)
    else:
        type_writer_effect(f"{Fore.GREEN}Nessun dettaglio trovato.{Style.RESET_ALL}")

def main():
    stampa_introduzione()

    scelta = input(f"{Fore.YELLOW}Vuoi usare una tua API Key per la ricerca? (sì/no): {Style.RESET_ALL}").lower()
    if scelta == 'si':
        api_key = input(f"{Fore.YELLOW}Inserisci la tua API key: {Style.RESET_ALL}")
        numero_telefono = input(f"{Fore.YELLOW}Inserisci il numero di telefono: {Style.RESET_ALL}")
        if not re.match(r'^\d{10}$', numero_telefono):  
            print(f"{Fore.RED}Il numero di telefono inserito non è valido. Inserisci un numero di 10 cifre.{Style.RESET_ALL}")
            return

        risultati = cerca_informazioni(numero_telefono, api_key)
        stampa_risultati(risultati)
    elif scelta == 'no':
        numero_telefono = input(f"{Fore.YELLOW}Inserisci il numero di telefono: {Style.RESET_ALL}")
        if not re.match(r'^\d{10}$', numero_telefono):  
            print(f"{Fore.RED}Il numero di telefono inserito non è valido. Inserisci un numero di 10 cifre.{Style.RESET_ALL}")
            return

        risultati = cerca_informazioni(numero_telefono)
        stampa_risultati(risultati)
    else:
        print(f"{Fore.RED}Scelta non valida. Per favore, inserisci 'sì' o 'no'.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
