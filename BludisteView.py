import tkinter as tk


class BludisteView:
    def __init__(self, root, canvas_sirka, canvas_vyska, control_width, vyber_bludiste_callback):
        self.root = root
        self.canvas_sirka = canvas_sirka
        self.canvas_vyska = canvas_vyska
        self.control_width = control_width
        self.vyber_bludiste_callback = vyber_bludiste_callback

        # Vytvoření canvasu pro bludiště
        self.canvas = tk.Canvas(self.root, width=self.canvas_sirka, height=self.canvas_vyska, bg="white")
        self.canvas.place(x=0, y=0)

        # Vytvoření ovládacích prvků
        self.create_controls()

    def vykresli(self, bludiste=None, blank=False):
        self.canvas.delete("all")  # Smazání předchozího obsahu

        if blank:  # Pokud chceme prázdné bílé pole, nic dalšího nekreslíme
            return

        if not bludiste:
            return

        data = bludiste.bludiste
        sirka = bludiste.get_sirka()
        vyska = bludiste.get_vyska()

        sirka_ctverce = self.canvas_sirka // sirka
        vyska_ctverce = self.canvas_vyska // vyska

        for y, radek in enumerate(data):
            for x, hodnota in enumerate(radek):
                color = 'white' if hodnota == 0 else 'black'
                if hodnota == 2:
                    color = 'red'

                x1, y1 = x * sirka_ctverce, y * vyska_ctverce
                x2, y2 = x1 + sirka_ctverce, y1 + vyska_ctverce
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color)

    def create_controls(self):
        control_start_x = self.canvas_sirka
        button_height = int(0.05 * self.canvas_vyska)
        button_spacing = int(0.02 * self.canvas_vyska)
        textbox_height = int(0.04 * self.canvas_vyska)
        label_height = int(0.03 * self.canvas_vyska)
        current_y = 10

        # Tlačítka
        buttons = [
            ("Vybrat Bludiště", self.vyber_bludiste_callback),
            ("Robot start", lambda: print("Start pressed")),
            ("Robot stop", lambda: print("Stop pressed")),
        ]

        for text, command in buttons:
            tk.Button(self.root, text=text, command=command).place(
                x=control_start_x + 10,
                y=current_y,
                width=self.control_width - 20,
                height=button_height
            )
            current_y += button_height + button_spacing

        # Textboxy mezi třetím a čtvrtým tlačítkem
        for label_text in ["Souřadnice X", "Souřadnice Y"]:
            tk.Label(self.root, text=label_text).place(
                x=control_start_x + 10,
                y=current_y,
                width=self.control_width - 20,
                height=label_height
            )
            current_y += label_height

            tk.Entry(self.root).place(
                x=control_start_x + 10,
                y=current_y,
                width=self.control_width - 20,
                height=textbox_height
            )
            current_y += textbox_height + button_spacing

        # Další tlačítka po textboxech
        buttons_after_textbox = [
            ("Umísti robota", lambda: print("Umísti robota pressed")),
            ("Vymaž robota", lambda: print("Vymaž robota pressed")),
        ]

        for text, command in buttons_after_textbox:
            tk.Button(self.root, text=text, command=command).place(
                x=control_start_x + 10,
                y=current_y,
                width=self.control_width - 20,
                height=button_height
            )
            current_y += button_height + button_spacing
