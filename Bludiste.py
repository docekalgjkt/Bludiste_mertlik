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
        return self.roboti_pozice == 2  # true kdyz je na policku vychod

    def je_volno(self):
        return self.roboti_kontrola == 0 or self.roboti_kontrola == 2  # true kdyz je policko pruchozi

    def get_vychod(self):
        for y, radek in enumerate(self.bludiste):
            for x, hodnota in enumerate(radek):
                if hodnota == 2:
                    return (y, x)  # index policka vychodu
        return None  # pokud vychod neni
