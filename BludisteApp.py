import tkinter as tk
from Bludiste import Bludiste
from BludisteView import BludisteView

class BludisteApp:
    def __init__(self, root, window_sirka, window_vyska, bludiste_data):
        self.root = root
        self.window_sirka = window_sirka
        self.window_vyska = window_vyska

        # vytvori instanci tridy Bludiste
        self.bludiste = Bludiste(bludiste_data)

        # zatim globalni, pote bude promenna, az bude robot
        self.bludiste.roboti_pozice = bludiste_data[2][3]  # priklad nastaveni
        self.bludiste.roboti_kontrola = bludiste_data[2][2]  # priklad nastaveni

        # vytvoreni instance tridy Bludisteiew
        self.view = BludisteView(root, self.bludiste, self.window_sirka, self.window_vyska)
        self.view.vykresli()

# spusteni aplikace
def main():
    root = tk.Tk()
    root.title("Bludiste App")

    # zde se da nastavit rozmery okna
    window_width = 600
    window_height = 450

    # zde se vklada bludiste, mozna pak udelam odkaz na file ve kterem to bude zvlast
    bludiste_data = [
        [0, 1, 1, 1],
        [0, 1, 0, 0],
        [0, 0, 0, 2]  
    ]

    # vytvoreni aplikace
    app = BludisteApp(root, window_width, window_height, bludiste_data)

    # spousti se mainloop
    root.mainloop()

if __name__ == "__main__":
    main()