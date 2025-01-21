import tkinter as tk
from tkinter import filedialog, messagebox
import os
from Bludiste import Bludiste
from BludisteView import BludisteView
from Robot import Robot
from RobotView import RobotView
from BludisteDAOFactory import BludisteDAOFactory

class BludisteApp:
    def __init__(self, root, window_sirka, window_vyska):
        self.root = root
        self.window_sirka = window_sirka
        self.window_vyska = window_vyska

        # Nastavení velikosti okna
        self.root.geometry(f"{window_sirka}x{window_vyska}")

        # Inicializace plátna a ovládacího panelu
        canvas_sirka = int(0.75 * self.window_sirka)
        canvas_vyska = self.window_vyska
        control_width = int(0.25 * self.window_sirka)

        self.bludiste = None
        self.robot = None
        self.umisťovani_robota = False  # Režim umisťování robota

        self.view = BludisteView(
            self,  # Předání instance BludisteApp
            root, canvas_sirka, canvas_vyska, control_width, self.vyber_a_vykresli_bludiste
        )

        self.robot_view = None

        # Zaregistrování události pro kliknutí na canvas
        self.view.canvas.bind("<Button-1>", self.on_canvas_click)

    def vyber_a_vykresli_bludiste(self):
        cesta_k_souboru = self.vyber_soubor()
        if not cesta_k_souboru:
            return

        dao = BludisteDAOFactory.get_bludiste_dao(cesta_k_souboru)
        bludiste_data = dao.nacti_bludiste(cesta_k_souboru)

        self.bludiste = Bludiste(bludiste_data)
        self.bludiste.app = self  # Pro propojení s BludisteApp
        self.view.vykresli(self.bludiste)

        sirka_ctverce = self.view.get_ctverec_sirka()
        vyska_ctverce = self.view.get_ctverec_vyska()

        # Vytvoření instance RobotView
        self.robot_view = RobotView(self.view.canvas, sirka_ctverce, vyska_ctverce)

    def vyber_soubor(self):
        slozka = os.path.dirname(__file__)
        soubor = filedialog.askopenfilename(
            title="Vyberte soubor",
            initialdir=slozka,
            filetypes=[("Podporované soubory", "*.txt;*.xml;*.csv")]
        )
        return soubor

    def on_canvas_click(self, event):
        if not self.bludiste:
            print("Bludiště není načteno.")
            return

        if not self.umisťovani_robota:
            print("Režim umisťování robota není aktivní.")
            return

        sirka_ctverce = self.view.get_ctverec_sirka()
        vyska_ctverce = self.view.get_ctverec_vyska()

        x = event.x // sirka_ctverce
        y = event.y // vyska_ctverce

        if x < 0 or y < 0 or x >= self.bludiste.get_sirka() or y >= self.bludiste.get_vyska():
            print("Kliknutí je mimo bludiště.")
            return

        if not self.bludiste.je_volne_pole(x, y) and self.bludiste.bludiste[y][x] != 2:
            print("Toto pole není volné.")
            return

        if not self.robot:
            self.robot = Robot()

        self.robot.nastav_pozici(x, y)
        self.robot_view.vykresli(self.robot)

        self.umisťovani_robota = False
        print("Robot byl úspěšně umístěn.")

    def aktivuj_rezim_umistit_robota(self):
        if not self.bludiste:
            print("Bludiště není načteno.")
            return

        self.umisťovani_robota = True
        messagebox.showinfo("Režim umístění robota", "Klikněte na volné pole v bludišti pro umístění robota.")

    def vymaz_robota(self):
        if self.robot_view:
            self.robot_view.vymaz()
        self.robot = None

    def spust_pruchod(self):
        if not self.robot or not self.bludiste:
            messagebox.showwarning("Chyba", "Robot nebo bludiště nejsou nastaveny.")
            return

        self.robot.dojdi_na_cervene_pole(self.bludiste, self.robot_view)

    def hlasi_uspech(self):
        messagebox.showinfo("Úspěch", "Robot dokončil svou práci!")

    def hlasi_neuspech(self):
        messagebox.showwarning("Neúspěch", "Robot nemohl najít cestu k červenému poli.")

if __name__ == "__main__":
    root = tk.Tk()
    app = BludisteApp(root, 800, 600)
    root.mainloop()

