import tkinter as tk
from Bludiste import Bludiste
from BludisteView import BludisteView
from BludisteDAO import BludisteDAO
import os

class BludisteApp:
    def __init__(self, root, window_sirka, window_vyska, cesta_k_souboru):
        self.root = root
        self.window_sirka = window_sirka
        self.window_vyska = window_vyska

        # Vytvoření instance a spusteni metody
        dao = BludisteDAO()
        bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

        # vytvoreni instance tridy
        self.bludiste = Bludiste(bludiste_data)

        # vytvoreni instance tridy
        self.view = BludisteView(root, self.bludiste, self.window_sirka, self.window_vyska)
        self.view.vykresli()

# spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiste App")

    # sem napisu rozmery okna, mozna to pak udelam pres popup okno
    window_width = 600
    window_height = 450

    # cesta k souboru pres os knihovnu
    cesta_k_souboru = os.path.join(os.path.dirname(__file__), 'bludiste_test.txt')

    # vytvoreni aplikece
    app = BludisteApp(root, window_width, window_height, cesta_k_souboru)

    # spusteni mainloop
    root.mainloop()

if __name__ == "__main__":
    main()
