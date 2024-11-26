import tkinter as tk
from tkinter import messagebox

class RobotView:
    def __init__(self, root, canvas, sirka_ctverce, vyska_ctverce):
        self.root = root
        self.canvas = canvas
        self.sirka_ctverce = sirka_ctverce
        self.vyska_ctverce = vyska_ctverce
        self.robot = None

    def vykresli(self, x, y):

        if self.robot:
            self.canvas.delete(self.robot)  # pokud uz robot je, vymaze se

        # vytvoreni noveho modreho kruhu
        radius = min(self.sirka_ctverce, self.vyska_ctverce) // 3  # velikost kruhu se pocita z velikosti kruhu
        center_x = x * self.sirka_ctverce + self.sirka_ctverce // 2
        center_y = y * self.vyska_ctverce + self.vyska_ctverce // 2

        self.robot = self.canvas.create_oval(
            center_x - radius, center_y - radius, center_x + radius, center_y + radius,
            fill="blue", outline="black"
        )
