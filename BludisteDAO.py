import os
from BludisteDAOInterface import BludisteDAOInterface

class BludisteDAO(BludisteDAOInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        if not os.path.exists(cesta_k_souboru):
            raise FileNotFoundError(f"Soubor {cesta_k_souboru} nebyl nalezen.")
        
        bludiste_data = []
        with open(cesta_k_souboru, 'r') as soubor:
            for radek in soubor:
                # kazdy znak v radku na cislo
                radek_data = [int(x) for x in radek.strip()]
                bludiste_data.append(radek_data)
        
        return bludiste_data