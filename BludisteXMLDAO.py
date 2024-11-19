import xml.etree.ElementTree as ET
from BludisteDAOInterface import BludisteDAOInterface


class BludisteXMLDAO(BludisteDAOInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        bludiste_data = []
        strom = ET.parse(cesta_k_souboru)
        koren = strom.getroot()

        for radek in koren.findall('radek'):
            radek_data = [int(x) for x in radek.text.strip()]
            bludiste_data.append(radek_data)

        return bludiste_data