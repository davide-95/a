class Bibita:
    def __init__(self, Codice, Bevanda, Prezzo):
        self.bevanda= Bevanda
        self.prezzo = Prezzo
        self.codice = Codice
    def stampa_informazione(self):
        print(self.bevanda, " ", self.prezzo, " ", self.codice)