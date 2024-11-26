import tkinter as tk
from tkinter import filedialog
import os
from Bludiste import Bludiste
from BludisteView import BludisteView
from BludisteDAOFactory import BludisteDAOFactory


class BludisteApp:
    def __init__(self, root, window_sirka, window_vyska):
        self.root = root
        self.window_sirka = window_sirka
        self.window_vyska = window_vyska

        # nastaveni velikosti okna
        self.root.geometry(f"{window_sirka}x{window_vyska}")

        # inicializace canvasu a ovladaciho panelu
        canvas_sirka = int(0.75 * self.window_sirka)
        canvas_vyska = self.window_vyska
        control_width = int(0.25 * self.window_sirka)
        self.view = BludisteView(root, canvas_sirka, canvas_vyska, control_width, self.vyber_a_vykresli_bludiste)
        self.view.vykresli(blank=True)  # zobrazi prazdne pole

        # inicializace bludiste, zatim prazdne
        self.bludiste = None

    def vyber_a_vykresli_bludiste(self):
        cesta_k_souboru = self.vyber_soubor()
        if not cesta_k_souboru:
            return

        # poutiti DAO factory
        dao = BludisteDAOFactory.get_bludiste_dao(cesta_k_souboru)
        bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

        # vytvoreni instance bludiste
        self.bludiste = Bludiste(bludiste_data)

        # vykresleni bludiste
        self.view.vykresli(self.bludiste)

    def vyber_soubor(self):
        slozka = os.path.dirname(__file__)
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )
        return soubor


# spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiště App")
    app = BludisteApp(root, window_sirka=1000, window_vyska=500)
    root.mainloop()


if __name__ == "__main__":
    main()
