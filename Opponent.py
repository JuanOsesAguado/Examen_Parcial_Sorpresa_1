class Opponent(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "opponent.png", lives=1)
        self.is_star = False

    def move(self):
        self.y += 2
        self.rect.y = self.y