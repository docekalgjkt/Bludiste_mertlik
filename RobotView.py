class RobotView:
    def __init__(self, canvas, sirka_ctverce, vyska_ctverce):
        self.canvas = canvas
        self.sirka_ctverce = sirka_ctverce
        self.vyska_ctverce = vyska_ctverce
        self.robot_id = None

    def vykresli(self, robot):
        # Mazání předchozí pozice
        if self.robot_id:
            self.canvas.delete(self.robot_id)

        x, y = robot.get_pozice()
        if x is not None and y is not None:
            radius = min(self.sirka_ctverce, self.vyska_ctverce) // 3
            center_x = x * self.sirka_ctverce + self.sirka_ctverce // 2
            center_y = y * self.vyska_ctverce + self.vyska_ctverce // 2

            self.robot_id = self.canvas.create_oval(
                center_x - radius, center_y - radius, center_x + radius, center_y + radius,
                fill="blue", outline="black"
            )

    def vymaz(self):
        if self.robot_id:
            self.canvas.delete(self.robot_id)
            self.robot_id = None

