from Menu.menu import draw_menu
from Played.played import plays, check_clicks
import pygame


def main() -> None:
    pygame.init()

    screen = pygame.display.set_mode((900, 750))
    pygame.display.set_caption("Rock Paper Scissor")

    font = pygame.font.Font("Itim/Itim-Regular.ttf", 40)
    start_game = font.render("Choose one", True, (255, 255, 255))

    w, h = pygame.display.get_surface().get_size()
    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if pygame.key == pygame.K_ESCAPE:
                    running = False
                    pygame.quit()

            check_clicks(w, h, screen)

        screen.fill((0, 0, 0))
        draw_menu(screen)
        screen.blit(start_game, ((w // 2) - 110, ((h // 5) // 2) - 15))

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
