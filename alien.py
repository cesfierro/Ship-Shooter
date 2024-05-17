import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alien in the fleet"""

    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load alien image and set its rect
        self.image = pygame.image.load('enemyShip.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near the top right of the screen.
        self.rect.x = self.screen_rect.right - (self.rect.width * 1.3)
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)

    def check_edges(self):
        """Return True if alien is at the edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.bottom >= screen_rect.bottom) or (self.rect.top <= 0)

    def update(self):
        """Move the aliens down or up"""
        self.y += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.y = self.y
