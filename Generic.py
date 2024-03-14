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
        time.sleep(0.05)  
    print()

def cerca_informazioni(nome, cognome, città, numero_telefono):
    query_parts = []
    if nome:
        query_parts.append(nome)
    if cognome:
        query_parts.append(cognome)
    if città:
        query_parts.append(città)
    if numero_telefono:
        query_parts.append(numero_telefono)
    
    query = " ".join(query_parts) + " -site:linkedin.com -site:facebook.com -site:twitter.com"
    risultati = []

    try:
        for j in search(query, num=10, stop=10, pause=2):
            risultati.append(j)
    except Exception as e:
        pass

    return risultati

def ottieni_links(risultati):
    return risultati

def stampa_introduzione():
    clear_screen()
    type_writer_effect(f"{Fore.CYAN}Benvenuto al programma di ricerca! Questo tool fa parte della raccolta di t.me/VikingTERMINAL\n{Style.RESET_ALL}")

def salva_risultati(links):
    nome_file = input(f"{Fore.YELLOW}Inserisci il nome del file per salvare i risultati (senza estensione): {Style.RESET_ALL}")
    nome_file += ".txt"
    with open(nome_file, "w") as file:
        for link in links:
            file.write(link + "\n")
    print(f"{Fore.GREEN}I risultati sono stati salvati nel file {nome_file}.{Style.RESET_ALL}")

def main():
    stampa_introduzione()

    nome = input(f"{Fore.YELLOW}Inserisci il nome (opzionale): {Style.RESET_ALL}")
    cognome = input(f"{Fore.YELLOW}Inserisci il cognome (opzionale): {Style.RESET_ALL}")
    città = input(f"{Fore.YELLOW}Inserisci la città (opzionale): {Style.RESET_ALL}")
    numero_telefono = input(f"{Fore.YELLOW}Inserisci il numero di telefono (opzionale): {Style.RESET_ALL}")

    risultati = cerca_informazioni(nome, cognome, città, numero_telefono)
    links = ottieni_links(risultati)

    clear_screen()
    if links:
        type_writer_effect(f"{Fore.CYAN}Links trovati:{Style.RESET_ALL}")
        for link in links:
            print(link)
        
        risposta = input(f"\n{Fore.YELLOW}Vuoi salvare i risultati in un file di testo? (yes/no): {Style.RESET_ALL}").lower()
        if risposta == "yes":
            salva_risultati(links)
        elif risposta != "no":
            print(f"{Fore.RED}Risposta non valida. I risultati non saranno salvati.{Style.RESET_ALL}")
    else:
        type_writer_effect(f"{Fore.GREEN}Nessun link trovato.{Style.RESET_ALL}")

if __name__ == "__main__":
    main()
