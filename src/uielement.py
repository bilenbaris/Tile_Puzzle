import pygame
from src.settings import *

class Text:
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
    def __init__(self, x, y, width, height, text, color, text_color, radius = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.color = color
        self.text_color = text_color
        self.radius = radius

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=self.radius)
        self.font = pygame.font.SysFont("Arial", 25)
        text = self.font.render(self.text, True, self.text_color)
        self.font_size = self.font.size(self.text)
        draw_x = self.x + (self.width - self.font_size[0]) // 2
        draw_y = self.y + (self.height - self.font_size[1]) // 2
        screen.blit(text, (draw_x, draw_y))
    
    def click(self, mouse_pos):
        return (self.x <= mouse_pos[0] <= self.x + self.width) and (self.y <= mouse_pos[1] <= self.y + self.height)