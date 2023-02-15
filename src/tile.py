import pygame
from src.settings import *

pygame.font.init()


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text, background_image):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE)) 
        self.font_surface = pygame.image.load(background_image)   
        self.x = x
        self.y = y
        self.text = text
        self.rect = self.image.get_rect()
        

        if self.text != "empty":
            self.font = pygame.font.SysFont("Arial", 50)
            self.image.fill(WHITE)
            
            area = ((int(text)%GAMESIZE) * TILESIZE, (int(text)//GAMESIZE)*  TILESIZE)

            self.image.blit(self.font_surface, (x, y), (area[0], area[1], TILESIZE, TILESIZE))

            self.font_size = self.font.size(self.text)
            draw_x = (TILESIZE - self.font_size[0]) // 2
            draw_y = (TILESIZE - self.font_size[1]) // 2
            # self.image.blit(self.font.render(self.text, True, WHITE), (draw_x, draw_y))



    def update(self):
        self.rect.x = START[0] + (self.x  * TILESIZE)
        self.rect.y = START[1] - SLIDE + (self.y * TILESIZE)
        

    def click(self, mouse_pos):
        return (self.rect.left <= mouse_pos[0] <= self.rect.right) and (self.rect.top <= mouse_pos[1] <= self.rect.bottom)

    def right(self):
        return self.rect.x + TILESIZE < GAMESIZE * TILESIZE + START[0]

    def left(self):
        return self.rect.x - TILESIZE >= 0 + START[0]

    def up(self):
        return self.rect.y - TILESIZE >= 0 + START[1] - SLIDE

    def down(self):
        return self.rect.y + TILESIZE < GAMESIZE * TILESIZE + START[1] - SLIDE


