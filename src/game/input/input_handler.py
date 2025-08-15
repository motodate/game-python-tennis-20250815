import pygame


class InputHandler:
    def __init__(self):
        self.keys = None
        self.previous_keys = {}
        self.key_states = {}
        
    def update(self):
        self.previous_keys = self.key_states.copy() if self.key_states else {}
        self.keys = pygame.key.get_pressed()
        
        for key in range(len(self.keys)):
            self.key_states[key] = self.keys[key]
    
    def is_key_pressed(self, key):
        return self.key_states.get(key, False) and not self.previous_keys.get(key, False)
    
    def is_key_held(self, key):
        return self.key_states.get(key, False)
    
    def is_move_up(self):
        return self.is_key_held(pygame.K_w) or self.is_key_held(pygame.K_UP)
    
    def is_move_down(self):
        return self.is_key_held(pygame.K_s) or self.is_key_held(pygame.K_DOWN)
    
    def is_action_pressed(self):
        return self.is_key_pressed(pygame.K_RETURN)
    
    def is_quit_pressed(self):
        return self.is_key_pressed(pygame.K_ESCAPE)
    
    def get_player_movement(self):
        if self.is_move_up():
            return -1
        elif self.is_move_down():
            return 1
        return 0
    
    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                return True
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                pass
        return False