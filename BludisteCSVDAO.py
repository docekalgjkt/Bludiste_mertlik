import csv
from BludisteDAOInterface import BludisteDAOInterface


class BludisteCSVDAO(BludisteDAOInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        bludiste_data = []
        with open(cesta_k_souboru, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for radek in reader:
                radek_data = [int(x) for x in radek]
                bludiste_data.append(radek_data)
        return bludiste_data
