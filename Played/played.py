from Menu.menu import IMAGES
import pygame
import random


def check_clicks(w: int, h: int, screen) -> None:
    x, y = pygame.mouse.get_pos()
    if x < w // 3 and 1.5 * h // 5 < y < 4 * h // 5 and pygame.mouse.get_pressed() == (1, 0, 0):
        move = random.randint(0, 2)
        if move == 0:
            text = f"Tie!"
        elif move == 1:
            text = f"You Lose!"
        else:
            text = f"You Won!"
        plays(0, w, h, screen, move, text)

    elif w // 3 < x < 2 * w // 3 and 1.5 * h // 5 < y < 4 * h // 5 and pygame.mouse.get_pressed() == (1, 0, 0):
        move = random.randint(0, 2)
        if move == 0:
            text = f"You Won!"
        elif move == 1:
            text = f"Tie!"
        else:
            text = f"You Lose!"
        plays(1, w, h, screen, move, text)

    elif x > 2 * w // 3 and 1.5 * h // 5 < y < 4 * h // 5 and pygame.mouse.get_pressed() == (1, 0, 0):
        move = random.randint(0, 2)
        if move == 0:
            text = f"You Lose!"
        elif move == 1:
            text = f"You Won!"
        else:
            text = f"Tie!"
        plays(2, w, h, screen, move, text)


def bot_move(screen, w: int, h: int, move) -> None:
    screen.blit(pygame.transform.scale(IMAGES[move], (w//3, w//3)), (2*w//3, 1.5*h//5))


def plays(image_val: int, w: int, h: int, screen, move, text) -> None:
    font = pygame.font.Font("Itim/Itim-Regular.ttf", 40)
    who_won = font.render(text, True, (255, 255, 255))
    play_again = font.render("Press any key to continue", True, (255, 255, 255))

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                running = False

        screen.fill((0, 0, 0))
        screen.blit(pygame.transform.scale(IMAGES[image_val], (w // 3, w // 3)), (0, 1.5 * h // 5))

        screen.blit(who_won, ((w//2) - 50, ((h//5)//2) - 20))
        screen.blit(play_again, ((w//2) - 217, (4*h//5)))

        bot_move(screen, w, h, move)

        pygame.display.update()

