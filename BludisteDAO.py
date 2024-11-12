import os
import csv
import xml.etree.ElementTree as ET
from BludisteDAOInterface import BludisteDAOInterface


class BludisteDAO(BludisteDAOInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        # kontrola, jestli sobour existuje jak by mel
        if not os.path.exists(cesta_k_souboru):
            raise FileNotFoundError(f"Soubor {cesta_k_souboru} nebyl nalezen.")

        # rozpoznani typu podle pripony
        _, extension = os.path.splitext(cesta_k_souboru)

        if extension == '.txt':
            return self.precti_txt(cesta_k_souboru)
        elif extension == '.xml':
            return self.precti_xml(cesta_k_souboru)
        elif extension == '.csv':
            return self.precti_csv(cesta_k_souboru)
        else:
            raise ValueError("Nepodporovaný typ souboru: očekáván '.txt', '.xml' nebo '.csv'.")

    def precti_txt(self, cesta_k_souboru):
        bludiste_data = []
        with open(cesta_k_souboru, 'r') as soubor:
            for radek in soubor:
                radek_data = [int(x) for x in radek.strip()]
                bludiste_data.append(radek_data)
        return bludiste_data

    def precti_xml(self, cesta_k_souboru):
        bludiste_data = []
        strom = ET.parse(cesta_k_souboru)
        koren = strom.getroot()

        for radek in koren.findall('radek'):
            radek_data = [int(x) for x in radek.text.strip()]
            bludiste_data.append(radek_data)

        return bludiste_data

    def precti_csv(self, cesta_k_souboru):
        bludiste_data = []
        with open(cesta_k_souboru, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for radek in reader:
                radek_data = [int(x) for x in radek]
                bludiste_data.append(radek_data)
        return bludiste_data

