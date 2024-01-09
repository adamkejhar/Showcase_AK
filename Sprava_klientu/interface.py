from databaze import Databaze
from pojistenec import Pojistenec
class Interface:

    def __init__(self):
        self.databaze = Databaze()



    def _vycisti_obrazovku(self): #metoda čistí obrazovku konzole od předchozích vstupů
        import os as _os
        _os.system('cls' if _os.name == 'nt' else 'clear')

    def dalsi_zadani(self):  # metoda zajišťuje pokračování/ukončení programu po provedené operaci
        while True:
            odpoved = input("\nPřejete si zadat další akci? ano / ne: ").lower()
            if odpoved == "ano": ##Návrat k do smyčky metody 'Menu'
                return True
            elif odpoved == "ne": ##ukončení programu po poslední operaci
                self.databaze.uloz()
                print("Děkuji za použití programu, data budou teď uložena, aplikaci ukončíte libovolnou klávesou.")
                input()
                return False
            print("Prosím, odpovězte 'ano' nebo 'ne'.")


    def menu(self): #metoda vypisuje dialog směrem k uživateli
        pokracovat = True
        self.databaze.nacti()
        while pokracovat:
            self._vycisti_obrazovku()
            print('-------------------------------------\n'
                  'Evidence Pojištěných - by Adam Kejhar\n'
                  '-------------------------------------\n')
            print(f'Vyberte si akci:')
            print('1 - Přidat nového pojistníka')
            print('2 - Vypsat všechny pojištěné')
            print('3 - Vyhledat záznam')
            print('4 - Vyhledat a smazat')
            vyber = (input())

            if vyber == '1':
                self.pridej_noveho()
                pokracovat = self.dalsi_zadani()
            elif vyber == '2':
                print('Jméno      Příjmení   Věk        Telefon')
                self.databaze.vypis_vsechny(self.databaze.pojistenci)
                pokracovat = self.dalsi_zadani()
            elif vyber == '3':
                zadani = (input('Zadejte hledaný výraz: '))
                self.databaze.vyhledavani(zadani)
                pokracovat = self.dalsi_zadani()
            elif vyber == '4':
                zadani = (input('Zadejte hledaný výraz: '))
                self.databaze.vyhledavani_a_mazani(zadani)
                pokracovat = self.dalsi_zadani()
            else:
                print('Neplatná volba!')
                continue  # Pokračování ve smyčce a nový vstup od uživatele
    def pridej_noveho(self): #metoda reprezentuje přidání nového uživatele do databáze - uživatelská možnosti 1
        jmeno = str(input('Zadejte jméno: '))
        prijmeni = str(input('Zadejte příjmení: '))
        vek = str(input('Zadejte Věk: '))
        telefon = str(input('Zadejte telefon: '))
        novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
        self.databaze.zapis_noveho(novy_pojistenec)
        print('\nByl přidán nový záznam:')
        print('Jméno      Příjmení   Věk        Telefon')
        print(novy_pojistenec)

