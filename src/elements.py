import pygame
from src.settings import *

"""
    ####################################
    DO NOT CHANGE ANYTHING IN THIS FILE.
    ####################################
"""

class Text:

    def __init__(self, x, y, text, text_size):
        pygame.font.init()
        self.x, self.y = x, y
        self.text = text
        self.text_size = text_size
    
    def draw(self, screen):
        """
            Draws the text on the screen.
        """
        font = pygame.font.SysFont("Arial", self.text_size)
        text = font.render(self.text, True, WHITE)
        screen.blit(text, (self.x, self.y))

class Button:
    
    def __init__(self, x, y, width, height, text, text_size, background_color, text_color, radius = 0):
        pygame.font.init()
        self.x, self.y = x, y
        self.width, self.height = width, height
        self.text = text
        self.text_size = text_size
        self.background_color = background_color
        self.text_color = text_color
        self.radius = radius

    def draw(self, screen):
        """
            Draws the button on the screen.
        """
        pygame.draw.rect(screen, self.background_color, (self.x, self.y, self.width, self.height), border_radius = self.radius)
        self.font = pygame.font.SysFont("Arial", self.text_size)
        text = self.font.render(self.text, True, self.text_color)
        self.font_size = self.font.size(self.text)
        draw_x = self.x + (self.width - self.font_size[0]) // 2
        draw_y = self.y + (self.height - self.font_size[1]) // 2
        screen.blit(text, (draw_x, draw_y))
    
    def click(self, mouse_pos):
        """
            Checks if the button is clicked or not.
            return: bool
        """
        return (self.x <= mouse_pos[0] <= self.x + self.width) and (self.y <= mouse_pos[1] <= self.y + self.height)