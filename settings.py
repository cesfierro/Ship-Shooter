class Settings:
    """A class for all of the game settigns"""
    def __init__(self):
        # Initialize game settings
        # Screen
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship Settings
        self.ship_speed = 1.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 3.5
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_shift_speed = 200
        # Fleet direction of 1 represents down, -1 represents up
        self.fleet_direction = 1
