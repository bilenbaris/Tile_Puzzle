import pygame
from src.settings import *

"""
    ####################################
    DO NOT CHANGE ANYTHING IN THIS FILE.
    ####################################
"""

class Tile(pygame.sprite.Sprite):
    
    def __init__(self, game, x, y, text, background_image):
        pygame.font.init()
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x, self.y = x, y
        self.text = text
        self.background_image = pygame.image.load(background_image) 

        self.image = pygame.Surface((TILESIZE, TILESIZE)) 
        self.rect = self.image.get_rect()
        
        # Set the corresponding background image to the tile.
        if self.text != "empty":
            self.font = pygame.font.SysFont("Arial", 50)
            area = ((int(text) % GAMESIZE) * TILESIZE, (int(text) // GAMESIZE) *  TILESIZE)
            self.image.blit(self.background_image, (x, y), (area[0], area[1], TILESIZE, TILESIZE))

    def update(self):
        """
            Updates the tile's position.
        """
        self.rect.x = START[0] + (self.x  * TILESIZE)
        self.rect.y = START[1] + (self.y * TILESIZE)
        
    def click(self, mouse_pos):
        """
            Checks if the tile is clicked or not.
            return: bool
        """
        return (self.rect.left <= mouse_pos[0] <= self.rect.right) and (self.rect.top <= mouse_pos[1] <= self.rect.bottom)

    def right(self):
        """
            Checks if the tile's right side is empty or not.
            return: bool
        """
        return self.rect.x + TILESIZE < GAMESIZE * TILESIZE + START[0]

    def left(self):
        """
            Checks if the tile's left side is empty or not.
            return: bool
        """
        return self.rect.x - TILESIZE >= 0 + START[0]

    def up(self):
        """
            Checks if the tile's up side is empty or not.
            return: bool
        """
        return self.rect.y - TILESIZE >= 0 + START[1]

    def down(self):
        """
            Checks if the tile's down side is empty or not.
            return: bool
        """
        return self.rect.y + TILESIZE < GAMESIZE * TILESIZE + START[1]