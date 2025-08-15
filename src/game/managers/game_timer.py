class GameTimer:
    GAME_DURATION = 60

    def __init__(self):
        self.remaining_time = self.GAME_DURATION

    def update(self, delta_time):
        self.remaining_time -= delta_time
        self.remaining_time = max(0, self.remaining_time)