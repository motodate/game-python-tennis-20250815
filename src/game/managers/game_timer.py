class GameTimer:
    GAME_DURATION = 60

    def __init__(self):
        self.remaining_time = self.GAME_DURATION
        self.is_running = False

    def update(self, delta_time):
        self.remaining_time -= delta_time
        self.remaining_time = max(0, self.remaining_time)

    def is_expired(self):
        return self.remaining_time <= 0

    def get_remaining_time(self):
        return self.remaining_time

    def get_formatted_time(self):
        minutes = int(self.remaining_time // 60)
        seconds = int(self.remaining_time % 60)
        return f"{minutes}:{seconds:02d}"

    def reset(self):
        self.remaining_time = self.GAME_DURATION

    def start(self):
        self.is_running = True

    def stop(self):
        self.is_running = False