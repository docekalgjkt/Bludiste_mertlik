import time


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

        while not queue.empty():
            x, y = queue.get()

            if bludiste.bludiste[y][x] == 2:
                self.nastav_pozici(x, y)
                robot_view.vykresli(self)
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy

                if (nx, ny) not in navstiveno and bludiste.je_volne_pole(nx, ny):
                    queue.put((nx, ny))
                    navstiveno.add((nx, ny))

                    self.nastav_pozici(nx, ny)
                    robot_view.vykresli(self)
                    time.sleep(0.2)  # Animace průchodu

        return False
