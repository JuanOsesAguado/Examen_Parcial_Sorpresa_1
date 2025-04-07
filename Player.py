class Player(Character):
    def __init__(self, x, y):
        super().__init__(x, y, "player.png", lives=3)
        self.score = 0

    def move(self, dx):
        self.x += dx
        self.rect.x = self.x