class Player:
    def __init__(self):
        self.health = 100  # Initialize health attribute

    def update_health(self, damage):
        self.health -= damage