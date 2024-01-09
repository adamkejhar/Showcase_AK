from pojistenec import Pojistenec

class Databaze():
    def __init__(self):
        self.pojistenci = []


    def zapis_noveho(self, novy_pojistenec):
        self.pojistenci.append(novy_pojistenec)

    def vypis_vsechny(self, pojistenci): ## metoda pro výpis všech záznamů - uživatelská možnost 2
        for zaznam in self.pojistenci:
            print(zaznam)

    def uloz(self):
        with open("databaze.txt", "w", encoding="utf-8") as file:
            for osoba in self.pojistenci:
                hodnoty = [osoba.jmeno, osoba.prijmeni, osoba.vek, osoba.telefon]
                radek = ";".join(hodnoty)
                file.write(radek + "\n")

    def nacti(self):
        self.pojistenci = []
        with open("databaze.txt", "r", encoding="utf-8") as file:
            for line in file.readlines():
                jmeno, prijmeni, vek, telefon = line.strip().split(";")
                novy_pojistenec = Pojistenec(jmeno, prijmeni, vek, telefon)
                self.zapis_noveho(novy_pojistenec)


    def vyhledavani(self, zadani): ##metoda vyhledávání podle všech atributů
        hledane_zaznamy = [clovek for clovek in self.pojistenci if any(zadani.lower() in getattr(clovek, attr).lower() for attr in ["jmeno", "prijmeni", "vek", "telefon"])]

        if not hledane_zaznamy:
            print('Nebyly nalezeny žádné záznamy.')
        else:
            print('\nNalezené záznamy:')
            print('Jméno      Příjmení   Věk        Telefon')
            for clovek in hledane_zaznamy:
                original_index = self.pojistenci.index(clovek)
                print(f"{original_index + 1}. {clovek}")

    def vyhledavani_a_mazani(self, zadani): ##třída nabídne vyhledávání a následně nabídne jeden z nalezených záznamů smazat
        hledane_zaznamy = [clovek for clovek in self.pojistenci if any(zadani.lower() in getattr(clovek, attr).lower() for attr in ["jmeno", "prijmeni", "vek", "telefon"])]

        if not hledane_zaznamy:
            print('Nebyly nalezeny žádné záznamy.')
        else:
            print('\nNalezené záznamy:')
            print('Jméno      Příjmení   Věk        Telefon')
            for clovek in hledane_zaznamy:
                original_index = self.pojistenci.index(clovek)
                print(f"{original_index +1}. {clovek}")

            index_to_delete = input("Zadejte číslo záznamu, který chcete smazat (nebo stiskněte Enter pro zrušení): ")

            if index_to_delete.isdigit() and 0 < int(index_to_delete):
                index_to_delete = int(index_to_delete) - 1
                deleted_record = self.pojistenci.pop(index_to_delete)
                print(f"Záznam -  {deleted_record} byl smazán.")
            else:
                print("Operace byla zrušena.")