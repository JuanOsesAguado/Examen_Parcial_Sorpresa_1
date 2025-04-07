class Character(Entity):
    def __init__(self, x, y, image_path, lives):
        super().__init__(x, y, image_path)
        self.lives = lives
        self.is_alive = True

    def shoot(self):
        return Shot(self.x + self.rect.width // 2, self.y, "shot.png")

    def collide(self):
        self.lives -= 1
        if self.lives <= 0:
            self.is_alive = False