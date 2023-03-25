class GameStats:
    """Track statistics for the Game."""

    def __init__(self,game):
        """Initialize statistics."""
        self.settings = game.settings
        self.reset_stats()
        # Start the Game in an active stats.
        self.game_active = True
    
    def reset_stats(self):
        self.ship_left = self.settings.ship_health