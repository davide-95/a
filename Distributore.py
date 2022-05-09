from Bibita import Bibita
class CreditoInsufficiente(Exception):
    pass
class BevandaEsaurita(Exception):
    pass

class Distributore:

    def __init__(self):
        self.colonne = [[],[],[],[]]
        self.tessere ={}
        self.bevande =[]



    def aggiungiBevanda(self, codice, nome, prezzo):
        nuovaBibita = Bibita(codice, nome, prezzo)
        self.bevande.append(nuovaBibita)


    def getPrice(self, codiceBibita):
        for bevanda in self.bevande:
            if bevanda.codice == codiceBibita:
                return bevanda.prezzo


    def getNome(self, codiceBibita):
        for bevanda in self.bevande:
            if bevanda.codice == codiceBibita:
                return bevanda.nome

    def caricaTessera(self, codiceTessera, credito):
        self.tessere[codiceTessera] = credito

    def leggiCredito(self, codiceTessera):
        return self.tessere[codiceTessera]

    def aggiornaColonna(self, numeroColonna, codiceBibita, numeroLattine):
        for bibita in self.bevande:
            if bibita.codice == codiceBibita:
                nuovaBibita = bibita
        self.colonne[numeroColonna - 1] = [nuovaBibita, numeroLattine]

    def erogaBibita(self, codiceBibita, codiceTessera):
        for idx, colonna in enumerate(self.colonne):
            if colonna [0].codice == codiceBibita:
              if colonna [1]  > 0:
                  if self.tessere[codiceTessera] > colonna[0].prezzo:
                     self.tessere[codiceTessera] -= colonna[0].prezzo
                     colonna[1] -= 1
                     return idx + 1
                  else:
                      raise CreditoInsufficiente
              else:
                  raise BevandaEsaurita
        raise BevandaEsaurita



    def lattineDisponibili(self, codiceBibita):
        sum = 0
        for colonna in self.colonne:
            if colonna [0].codice== codiceBibita:
                sum += colonna[1]
        return sum



