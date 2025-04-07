class Shot(Entity):
    def __init__(self, x, y, image_path):
        super().__init__(x, y, image_path)

    def move(self):
        self.y -= 5
        self.rect.y = self.y

    def hit_target(self, target):
        return self.rect.colliderect(target.rect)