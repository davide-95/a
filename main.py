from Distributore import Distributore
from Bibita import Bibita

distrib = Distributore()
distrib.aggiungiBevanda("1", "Coca-cola", 50)
distrib.aggiungiBevanda("2", "Pepso", 45)
distrib.aggiungiBevanda("3", "Fanto", 40)
distrib.aggiornaColonna(1, "1", 5)
distrib.caricaTessera(33, 200)

distrib.erogaBibita("1", 33)
print("ok")
distrib.erogaBibita("1", 33)
distrib.erogaBibita("1", 33)





