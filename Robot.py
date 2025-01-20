class Robot:
    def __init__(self):
        self.x = None
        self.y = None

    def nastav_pozici(self, x, y):
        self.x = x
        self.y = y

    def get_pozice(self):
        return self.x, self.y

    def dojdi_na_cervene_pole(self, bludiste, robot_view):
        from queue import Queue

        start = (self.x, self.y)
        queue = Queue()
        queue.put(start)
        navstiveno = set()
        navstiveno.add(start)

        cil_dosažen = [False]  # Pro indikaci dosažení cíle

        def krok():
            if queue.empty():
                if not cil_dosažen[0]:
                    # Zpětné volání hlášení do BludisteApp
                    bludiste.app.hlasi_neuspech()
                return

            x, y = queue.get()

            # Kontrola cílového pole (červené pole)
            if bludiste.bludiste[y][x] == 2:
                self.nastav_pozici(x, y)
                robot_view.vykresli(self)
                cil_dosažen[0] = True
                bludiste.app.hlasi_uspech()
                return

            # Procházení pouze ortogonálních sousedních polí
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in navstiveno and bludiste.je_volne_pole(nx, ny):
                    queue.put((nx, ny))
                    navstiveno.add((nx, ny))

            # Animace pohybu robota
            self.nastav_pozici(x, y)
            robot_view.vykresli(self)

            # Další krok po 200 ms
            robot_view.canvas.after(200, krok)

        krok()  # Spuštění prvního kroku


