import tkinter as tk

class BludisteView:
    def __init__(self, app, root, canvas_sirka, canvas_vyska, control_width, vyber_bludiste_callback):
        self.app = app  # Odkaz na instanci BludisteApp
        self.root = root
        self.canvas_sirka = canvas_sirka
        self.canvas_vyska = canvas_vyska
        self.control_width = control_width
        self.vyber_bludiste_callback = vyber_bludiste_callback

        self.bludiste = None

        # Vytvoření canvasu pro bludiště
        self.canvas = tk.Canvas(self.root, width=self.canvas_sirka, height=self.canvas_vyska, bg="white")
        self.canvas.place(x=0, y=0)

        # Vytvoření ovládacích prvků
        self.create_controls()

    def vykresli(self, bludiste=None):
        self.canvas.delete("all")

        if not bludiste:
            return

        self.bludiste = bludiste
        data = bludiste.bludiste
        sirka = bludiste.get_sirka()
        vyska = bludiste.get_vyska()

        sirka_ctverce = self.get_ctverec_sirka()
        vyska_ctverce = self.get_ctverec_vyska()

        for y, radek in enumerate(data):
            for x, hodnota in enumerate(radek):
                color = 'white' if hodnota == 0 else 'black'
                if hodnota == 2:
                    color = 'red'

                x1, y1 = x * sirka_ctverce, y * vyska_ctverce
                x2, y2 = x1 + sirka_ctverce, y1 + vyska_ctverce
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def get_ctverec_sirka(self):
        return self.canvas_sirka // self.bludiste.get_sirka()

    def get_ctverec_vyska(self):
        return self.canvas_vyska // self.bludiste.get_vyska()

    def create_controls(self):
        control_start_x = self.canvas_sirka
        button_height = 30
        button_spacing = 10
        current_y = 10

        buttons = [
            ("Vybrat Bludiště", self.vyber_bludiste_callback),
            ("Umísti Robota", self.app.aktivuj_rezim_umistit_robota),
            ("Vymaž Robota", self.app.vymaz_robota),
            ("Spustit Průchod", self.app.spust_pruchod),  # Nové tlačítko
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, command=command).place(
                x=control_start_x + 10,
                y=current_y,
                width=self.control_width - 20,
                height=button_height
            )
            current_y += button_height + button_spacing

