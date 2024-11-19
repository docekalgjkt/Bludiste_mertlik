from BludisteDAOInterface import BludisteDAOInterface


class BludisteTXTDAO(BludisteDAOInterface):
    def nacti_bludiste(self, cesta_k_souboru):
        bludiste_data = []
        with open(cesta_k_souboru, 'r') as soubor:
            for radek in soubor:
                radek_data = [int(x) for x in radek.strip()]
                bludiste_data.append(radek_data)
        return bludiste_data