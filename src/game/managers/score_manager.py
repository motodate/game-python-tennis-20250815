class ScoreManager:
    def __init__(self):
        self.player_score = 0
        self.cpu_score = 0

    def add_player_point(self):
        self.player_score += 1

    def add_cpu_point(self):
        self.cpu_score += 1

    def get_player_score(self):
        return self.player_score

    def get_cpu_score(self):
        return self.cpu_score

    def get_scores(self):
        return (self.player_score, self.cpu_score)

    def reset(self):
        self.player_score = 0
        self.cpu_score = 0