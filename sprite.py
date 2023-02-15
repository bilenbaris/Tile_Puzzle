import pygame
from settings import *

pygame.font.init()


class Tile(pygame.sprite.Sprite):
    def __init__(self, game, x, y, text):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = pygame.Surface((TILESIZE, TILESIZE))       
        self.x = x
        self.y = y
        self.text = text
        self.rect = self.image.get_rect()

        if self.text != "empty":
            self.font = pygame.font.SysFont("Arial", 50)
            font_surface = self.font.render(self.text, True, BLACK)
            self.image.fill(WHITE)
            self.font_size = self.font.size(self.text)
            draw_x = (TILESIZE - self.font_size[0]) // 2
            draw_y = (TILESIZE - self.font_size[1]) // 2
            self.image.blit(font_surface, (draw_x, draw_y))


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


class UIElement:
    def __init__(self, x, y, text, size):
        self.x = x
        self.y = y
        self.text = text
        self.size = size
    
    def draw(self, screen):
        font = pygame.font.SysFont("Arial", self.size)
        text = font.render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))

class Button:
    def __init__(self, x, y, width, height, text, color, text_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color

    def draw(self, screen):
        # pygame.draw.ellipse(screen, self.color, (self.x, self.y, self.width, self.height))
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=25)
        self.font = pygame.font.SysFont("Arial", 25)
        text = self.font.render(self.text, True, self.text_color)
        self.font_size = self.font.size(self.text)
        draw_x = self.x + (self.width - self.font_size[0]) // 2
        draw_y = self.y + (self.height - self.font_size[1]) // 2
        screen.blit(text, (draw_x, draw_y))
    
    def click(self, mouse_pos):
        return (self.x <= mouse_pos[0] <= self.x + self.width) and (self.y <= mouse_pos[1] <= self.y + self.height)