import os
from BludisteTXTDAO import BludisteTXTDAO
from BludisteXMLDAO import BludisteXMLDAO
from BludisteCSVDAO import BludisteCSVDAO


class BludisteDAOFactory:
    @staticmethod
    def get_bludiste_dao(cesta_k_souboru):
        if not os.path.exists(cesta_k_souboru):
            raise FileNotFoundError(f"Soubor {cesta_k_souboru} nebyl nalezen.")

        _, extension = os.path.splitext(cesta_k_souboru)

        if extension == '.txt':
            return BludisteTXTDAO()
        elif extension == '.xml':
            return BludisteXMLDAO()
        elif extension == '.csv':
            return BludisteCSVDAO()
        else:
            raise ValueError("Nepodporovaný typ souboru: očekáván '.txt', '.xml' nebo '.csv'.")
