class Pojistenec: ## třída reprezentuje záznam jedné osoby v systému
    def __init__(self, jmeno, prijmeni, vek, telefon=123456789):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.telefon = telefon

    def vypis_jednoho(self): ## obecná metoda pro výpis atributů
                return f'{self.jmeno.ljust(10)} {self.prijmeni.ljust(10)} {self.vek.ljust(10)} {self.telefon.ljust(10)}'
    def __str__(self):
        return f'{self.vypis_jednoho()}'