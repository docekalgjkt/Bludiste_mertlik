class Bludiste:
    def __init__(self, bludiste):
        self.bludiste = bludiste
        self.roboti_pozice = None  # inicializace
        self.roboti_kontrola = None  # inicializace

    def get_sirka(self):
        return len(self.bludiste[0])

    def get_vyska(self):
        return len(self.bludiste)

    def je_vychod(self):
        return self.roboti_pozice == 2  # Vrací True, pokud je robot na východě

    def je_volno(self):
        return self.roboti_kontrola == 0 or self.roboti_kontrola == 2  # Vrací True, pokud je volno

    def get_vychod(self):
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 2:
                    return (y, x)  # Vrátí souřadnice východu
        return None  # Pokud východ nenalezen