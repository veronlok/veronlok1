import pygame
pygame.init()

# consts
WINDOW_WIDHT, WINDOW_HEIGHT = 800, 600
ROCKET_IMG = 'rocket.png'
BALL_IMG = 'ball.png'
BG_COLOR = (70, 70, 70)
#consts

class sprite(pygame.sprite.Sprite):
    def __init__(self, image, x=0, y=0, widht = 0, height = 0):
        image = pygame.image.load(image)
        self.image = pygame.transform.scale(Image, (widht, height))
        self.rect = pygame.Rect(x, y, widht, height)

    def draw(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(sprite):
    def __init__(
        self, image, x=0, y=0, widht=0, height=0, speed = 5,
        k_up=pygame.K_UP, k_down=pygame.K_DOWN,
    ):
        super().__init__(image, x, y, widht, height)
        self.speed = speed
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[self.k_up] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[self.k_down] and self.rect.y < (
            WINDOW_HEIGHT - self.rect.height
        ):
            self.rect.y += self.speed

window = pygame.display.set_mode((WINDOW_WIDHT, WINDOW_HEIGHT))
pygame.display.set_caption('Пинг понг')
window.fill(BG_COLOR)
clock = pygame.time.Clock()

player_left = Player(
    ROCKET_IMG, 5, 5, 30, 100, 5, pygame.K_w, pygame.K_s
)
player_right = Player(
    ROCKET_IMG, WINDOW_WIDHT - 35, WINDOW_HEIGHT - 105,
    30, 100, 5, pygame.K_UP, pygame.K_DOWN
)

game_status = 'game'
while game_status != 'off':
    window.fill(BG_COLOR)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_status = 'off'

    clock.tick(60)
    pygame.display.update()