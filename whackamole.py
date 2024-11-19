import pygame
import random

def draw_mole(new_x, new_y, mole_image, screen):
    #draws mole and then returns the coordinates in a tuple
    screen.blit(mole_image, mole_image.get_rect(topleft=(32 * new_x, 32 * new_y)))
    mole_coords = (new_x, new_y)
    return mole_coords


def main():
    try:
        pygame.init()
        # You can draw the mole with this snippet:
        # screen.blit(mole_image, mole_image.get_rect(topleft=(x,y)))
        mole_image = pygame.image.load("mole.png")
        screen = pygame.display.set_mode((640, 512))
        clock = pygame.time.Clock()
        #sets starting mole location to 0,0
        mole_location = (0,0)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    coordinate = event.pos
                    #checks if click hits mole
                    if (coordinate[0]//32, coordinate[1]//32) == mole_location:
                        #draws mole at new random location and sets mole_location to (new_x, new_y)
                        mole_location = draw_mole(random.randrange(0,20),random.randrange(0,16) , mole_image, screen)
            screen.fill("light green")
            #draws screen lines
            for i in range(21):
                pygame.draw.line(screen, "black", (32 * (i - 1), 0), (32 * (i - 1), 512))
            for i in range(17):
                pygame.draw.line(screen, "black", (0, 32 * (i - 1)), (640, 32 * (i - 1)))
            #keeps drawing mole based on mole_location coordinates (mole_x, mole_y)
            draw_mole(mole_location[0], mole_location[1], mole_image, screen)
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()


if __name__ == "__main__":
    main()
