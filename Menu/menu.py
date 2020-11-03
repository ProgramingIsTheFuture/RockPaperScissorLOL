import pygame

IMAGES = [pygame.image.load("Imgs/0.png"), pygame.image.load("Imgs/1.png"), pygame.image.load("Imgs/2.png")]


def draw_menu(screen) -> None:
    w, h = pygame.display.get_surface().get_size()
    draw_rock(screen, w, h)
    draw_paper(screen, w, h)
    draw_scissor(screen, w, h)
    draw_lines(screen, w, h)


def draw_rock(screen, w, h) -> None:
    screen.blit(pygame.transform.scale(IMAGES[0], (w//3, w//3)), (0, 1.5*h//5))


def draw_paper(screen, w, h) -> None:
    w, h = pygame.display.get_surface().get_size()
    screen.blit(pygame.transform.scale(IMAGES[1], (w // 3, w // 3)), (w//3, 1.5 * h // 5))


def draw_scissor(screen, w, h) -> None:
    w, h = pygame.display.get_surface().get_size()
    screen.blit(pygame.transform.scale(IMAGES[2], (w // 3, w // 3)), (2*w//3, 1.5 * h // 5))


def draw_lines(screen, w, h) -> None:
    pygame.draw.line(screen, (255, 255, 255), (w//3, 4*h//5), (w//3, h//5))
    pygame.draw.line(screen, (255, 255, 255), (2*w//3, 4*h//5), (2*w//3, h//5))
