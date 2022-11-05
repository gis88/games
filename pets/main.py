import pygame
import random
pygame.init()

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Runny Animals")
icon = pygame.image.load("media/fox_logo.png")
pygame.display.set_icon(icon)

rick_width = 80
rick_height = 40

rick_x = display_width // 3
rick_y = display_height - rick_height - 40

# Enemies variables
bottle_width = 15
bottle_height = 45

bottle_x = display_width - 45
bottle_y = display_height - bottle_height - 45


bottle_img = [pygame.image.load("media/beer_bottle.png"), pygame.image.load("media/cola.png"), pygame.image.load("media/poo.png")]
bottle_options = [32, 520, 32, 480, 12, 500]
clock = pygame.time.Clock()

make_jump = False
jump_counter = 30


class Bottle:
    def __init__(self, x, y, width, image, speed):
        self.x = x
        self.y = y
        self.width = width
        self.image = image
        self.speed = speed

    def move(self):
        if self.x >= -self.width:
            display.blit(self.image, (self.x, self.y))
            # pygame.draw.rect(display, (0, 204, 0), (self.x, self.y, self.width, self.height))
            self.x -= self.speed
            return True
        else:
            return False

    def return_self(self, radius, y, width, image):
        self.x = radius
        self.y = y
        self.width = width
        self.image = image
        display.blit(self.image, (self.x, self.y))


def run_game():
    global make_jump
    game = True
    bottle_arr = []
    create_bottle(bottle_arr)
    land = pygame.image.load("media/background.png")

    while game:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            make_jump = True

        if make_jump:
            jump()

        display.blit(land, (0, 0))
        draw_bottle(bottle_arr)

        pygame.draw.rect(display, (153, 0, 75), (rick_x, rick_y, rick_width, rick_height))
        pygame.display.update()
        clock.tick(80)


def jump():
    global rick_y, jump_counter, make_jump
    if jump_counter >= -30:
        rick_y -= jump_counter / 2.5
        jump_counter -= 1
    else:
        jump_counter = 30
        make_jump = False


def create_bottle(array):  # vars: x, y, width, height, speed
    choice = random.randrange(0, 3)
    img = bottle_img[choice]
    width = bottle_options[choice * 2]
    height = bottle_options[choice * 2 + 1]
    array.append(Bottle(display_width + 20, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = bottle_img[choice]
    width = bottle_options[choice * 2]
    height = bottle_options[choice * 2 + 1]
    array.append(Bottle(display_width + 300, height, width, img, 4))

    choice = random.randrange(0, 3)
    img = bottle_img[choice]
    width = bottle_options[choice * 2]
    height = bottle_options[choice * 2 + 1]
    array.append(Bottle(display_width + 600, height, width, img, 4))


def find_radius(array):
    maximum = max(array[0].x, array[1].x, array[2].x)

    if maximum < display_width:
        radius = display_width
        if radius - maximum < 50:
            radius += 100
    else:
        radius = maximum

    choice = random.randrange(0, 5)
    if choice == 0:
        radius += random.randrange(10, 15)
    else:
        radius += random.randrange(200, 350)
    return radius


def draw_bottle(array):
    for bottle in array:
        check = bottle.move()
        if not check:
            radius = find_radius(array)
            choice = random.randrange(0, 3)
            img = bottle_img[choice]
            width = bottle_options[choice * 2]
            height = bottle_options[choice * 2 + 1]

            bottle.return_self(radius, height, width, img)


run_game()
