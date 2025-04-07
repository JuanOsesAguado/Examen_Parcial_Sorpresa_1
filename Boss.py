class Boss(Opponent):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.image = pygame.image.load("boss.png")
        self.lives = 3

    def move(self):
        self.y += 4  # Se mueve el doble de rápido que un enemigo normal
        self.rect.y = self.y