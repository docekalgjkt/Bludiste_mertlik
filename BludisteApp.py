import tkinter as tk
from tkinter import filedialog
import os
from Bludiste import Bludiste
from BludisteView import BludisteView
from BludisteDAO import BludisteDAO

class BludisteApp:
    def __init__(self, root, window_sirka, window_vyska):
        self.root = root
        self.window_sirka = window_sirka
        self.window_vyska = window_vyska

        # zavolani metody pro vyber souboru
        cesta_k_souboru = self.vyber_soubor()

        if cesta_k_souboru:
            # vytvoreni instance dao a nacteni dat
            dao = BludisteDAO()
            bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

            # vytvoreni instance tridy Bludiste
            self.bludiste = Bludiste(bludiste_data)

            # vytvoreni instance tridy BludisteView
            self.view = BludisteView(root, self.bludiste, self.window_sirka, self.window_vyska)
            self.view.vykresli()

    def vyber_soubor(self):
        # ziskani cesty k aktualnimu adresari
        slozka = os.path.dirname(__file__)

        # filtr pro podporovane soubory
        soubory = [f for f in os.listdir(slozka) if f.endswith(('.txt', '.xml', '.csv'))]

        if not soubory:
            print("Žádné podporované soubory nebyly nalezeny.")
            return None

        # otevreni dialogoveho okna pro vyber souboru
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )

        return soubor

# spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiste App")

    # nastaveni rozmeru okna
    window_width = 600
    window_height = 450

    # vytvoreni instance aplikace
    app = BludisteApp(root, window_width, window_height)

    # spusteni mainloop
    root.mainloop()

if __name__ == "__main__":
    main()
