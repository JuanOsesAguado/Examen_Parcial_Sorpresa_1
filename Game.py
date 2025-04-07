class Game:
    def __init__(self):
        self.player = Player(WIDTH // 2, HEIGHT - 50)
        self.opponents = [Opponent(random.randint(0, WIDTH - 50), random.randint(-100, -40)) for _ in range(5)]
        self.shots = []
        self.is_running = True
        self.score = 0

    def start(self):
        while self.is_running:
            self.update()
            self.draw()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player.move(-5)
        if keys[pygame.K_RIGHT]:
            self.player.move(5)
        if keys[pygame.K_SPACE]:
            self.shots.append(self.player.shoot())

        for opponent in self.opponents:
            opponent.move()
            if opponent.rect.y > HEIGHT:
                opponent.y = random.randint(-100, -40)

        for shot in self.shots[:]:
            shot.move()
            for opponent in self.opponents[:]:
                if shot.hit_target(opponent):
                    self.opponents.remove(opponent)
                    self.shots.remove(shot)
                    self.score += 1
                    if self.score % 5 == 0:  # Aparece el jefe final cada 5 enemigos derrotados
                        self.opponents.append(Boss(random.randint(0, WIDTH - 50), -50))

        if self.player.lives <= 0:
            self.is_running = False
            self.end_game()

    def draw(self):
        screen.fill(WHITE)
        self.player.draw(screen)
        for opponent in self.opponents:
            opponent.draw(screen)
        for shot in self.shots:
            shot.draw(screen)
        pygame.display.flip()
        clock.tick(60)

    def end_game(self):
        print("Game Over! Score:", self.score)
        pygame.quit()
        exit()