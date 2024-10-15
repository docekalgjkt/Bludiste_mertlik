import tkinter as tk

class MyWindow:
    def __init__(self, root, x):
        # hlavni okno
        root.geometry("900x1200")
        root.title("mertlik_bludiste")

        # zavola metodu na vytvoreni canvasu
        self.create_gameplan(root, x)

    def create_gameplan(self, root, x):
        # vytvori canvas s hernim planem
        self.canvas = tk.Canvas(root, width=600, height=600, bg="white")
        self.canvas.place(relx=0.4, rely=0.5, anchor="center") #relativni umisteni, mozna zmenim

        # vypocet velikosti ctverce
        square_size = 600 / x  # 600 je velikost canvasu

        # loop na nakresleni mrizky
        for i in range(x):
            for j in range(x):
                # Výpočet souřadnic čtverců
                x1 = i * square_size
                y1 = j * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                # Kreslení čtverců
                self.canvas.create_rectangle(x1, y1, x2, y2, outline="black")



# vytvori hlavni okno
root = tk.Tk()

# Poocet ctvercu v bludisti, promenna 
x = 50

# spusteni tridy s parametrem x
app = MyWindow(root, x)

# spusteni tkinter loop
root.mainloop()