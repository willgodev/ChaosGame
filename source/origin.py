import pygame
from pygame import gfxdraw
from pygame import Color
import random

def main():
    pixel_positions = []
    latest_pixel_pos = None
    start_simulation = False
    original_length = 0

    pygame.init()
    screen = pygame.display.set_mode((1920, 1080))
    pygame.Surface.fill(screen, Color(0, 0, 0))

    running = True
    while running:
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                pixel_positions.append(pos)
                gfxdraw.pixel(screen, pos[0], pos[1], Color(255, 255, 255))
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    start_simulation = not start_simulation
                if event.key == pygame.K_ESCAPE:
                    running = False
                if event.key == pygame.K_r and not start_simulation:
                    screen.fill(Color(0, 0, 0))
                    pixel_positions = []
                    latest_pixel_pos = None
            if event.type == pygame.QUIT:
                running = False

        if start_simulation:
            if not latest_pixel_pos:
                original_length = len(pixel_positions)
                rand_pos1 = pixel_positions[random.randint(0, len(pixel_positions) - 1)]
                rand_pos2 = pixel_positions[random.randint(0, len(pixel_positions) - 1)]
                while rand_pos1 == rand_pos2:
                    rand_pos2 = pixel_positions[random.randint(0, len(pixel_positions) - 1)]
                mp = get_midpoint(rand_pos1, rand_pos2)
                gfxdraw.pixel(screen, mp[0], mp[1], Color(255, 255, 255))
                latest_pixel_pos = mp
            else:
                rand_pos = pixel_positions[random.randint(0, original_length - 1)]
                mp = get_midpoint(rand_pos, latest_pixel_pos)
                gfxdraw.pixel(screen, mp[0], mp[1], Color(255, 255, 255))
                latest_pixel_pos = mp


def get_midpoint(pos1, pos2):
    new_x = (pos1[0] + pos2[0]) // 2
    new_y = (pos1[1] + pos2[1]) // 2
    return (new_x, new_y)


if __name__=="__main__":
    main()
