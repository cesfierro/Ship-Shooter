import pygame

class Ship:
    """Class to manage the ship"""

    def __init__(self, ai_game):
        """Initialize the ship and starting position"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship and create rect
        self.image = pygame.image.load('Ship.bmp')
        self.rect = self.image.get_rect()

        # Start the ship at the mid left of the screen
        self.rect.midleft = self.screen_rect.midleft
    

        # Store a float for the ship's exact veritcal position\
        self.y = float(self.rect.y)

        # Movement flag
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        # Update the ship's position based on flags
        # Update the 'y' value, not the rect
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # Update the rect object for self 'y'
        self.rect.y = self.y

    def blitme(self):
        """Draw the ship at its current location"""
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        """Reset the ship on the screen"""
        self.rect.midleft = self.screen_rect.midleft
        self.y = float(self.rect.y)