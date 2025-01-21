class Bludiste:
    def __init__(self, bludiste_data):
        self.bludiste = bludiste_data

    def get_sirka(self):
        return len(self.bludiste[0]) if self.bludiste else 0

    def get_vyska(self):
        return len(self.bludiste)

    def je_volne_pole(self, x, y):
        if 0 <= y < len(self.bludiste) and 0 <= x < len(self.bludiste[0]):
            return self.bludiste[y][x] in (0, 2)  # Pole je volné nebo cílové
        return False
