import pygame
from src.ui.game_window import GameWindow
from src.game.entities.paddle import Paddle
from src.game.entities.ball import Ball
from src.game.managers.score_manager import ScoreManager
from src.game.managers.game_timer import GameTimer
from src.game.state.game_state import GameState
from src.game.input.input_handler import InputHandler
from src.game.ai.cpu_controller import CPUController
from src.game.physics.collision import CollisionHandler
from src.utils.settings import GameSettings


class TennisGame:
    def __init__(self):
        pygame.init()
        self.window = None
        self.player_paddle = None
        self.cpu_paddle = None
        self.ball = None
        self.score_manager = None
        self.game_timer = None
        self.game_state = None
        self.input_handler = None
        self.cpu_controller = None
        self.collision_handler = None
        self.clock = None
        self.font = None
    
    def initialize_components(self):
        """全コンポーネントを初期化"""
        # GameWindowの初期化
        self.window = GameWindow()
        
        # Paddle（プレイヤー、CPU）の作成
        self.player_paddle = Paddle.create_left_paddle()
        self.cpu_paddle = Paddle.create_right_paddle()
        
        # Ballの作成
        self.ball = Ball(
            GameSettings.WINDOW_WIDTH // 2,
            GameSettings.WINDOW_HEIGHT // 2
        )
        
        # ScoreManager、GameTimer、GameStateの初期化
        self.score_manager = ScoreManager()
        self.game_timer = GameTimer()
        self.game_state = GameState()
        
        # InputHandler、CPUController、CollisionHandlerの初期化
        self.input_handler = InputHandler()
        self.cpu_controller = CPUController(self.cpu_paddle)
        self.collision_handler = CollisionHandler()
        
        # その他の初期化
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
    
    def update(self, delta_time):
        """ゲーム更新処理"""
        # 入力処理の更新
        self.input_handler.update()
        
        # ゲーム状態に応じた処理分岐
        if self.game_state.is_waiting():
            if self.input_handler.is_action_pressed():
                self.game_state.start_game()
                self.game_timer.start()
        elif self.game_state.is_playing():
            self.update_playing(delta_time)
    
    def update_playing(self, delta_time):
        """プレイ中の更新処理"""
        # タイマーの更新と終了判定
        if self.game_timer.is_running:
            self.game_timer.update(delta_time)
            if self.game_timer.is_expired():
                self.game_state.end_game({
                    'player': self.score_manager.get_player_score(),
                    'cpu': self.score_manager.get_cpu_score()
                })
                return
        
        # プレイヤーパドルの入力処理
        movement = self.input_handler.get_player_movement()
        if movement == -1:
            self.player_paddle.move_up(300, delta_time)  # 固定速度
        elif movement == 1:
            self.player_paddle.move_down(300, delta_time)  # 固定速度
        
        # CPUパドルのAI更新
        self.cpu_controller.update(self.ball, delta_time)
        
        # ボールの移動更新
        self.ball.update(delta_time)
        
        # 衝突判定と反射処理
        if self.collision_handler.check_paddle_collision(self.ball, self.player_paddle):
            self.collision_handler.handle_paddle_bounce(self.ball, self.player_paddle)
        if self.collision_handler.check_paddle_collision(self.ball, self.cpu_paddle):
            self.collision_handler.handle_paddle_bounce(self.ball, self.cpu_paddle)
        
        if self.collision_handler.check_wall_collision(self.ball):
            self.collision_handler.handle_wall_bounce(self.ball)
        
        # 得点判定とスコア更新
        if self.ball.x <= 0:  # 左側でボールが出た場合（CPUの得点）
            self.score_manager.add_cpu_point()
            self.ball.reset()
        elif self.ball.x >= GameSettings.WINDOW_WIDTH - self.ball.size:  # 右側（プレイヤーの得点）
            self.score_manager.add_player_point()
            self.ball.reset()
    
    def render(self):
        """描画処理"""
        # 画面を黒でクリア
        self.window.screen.fill(GameSettings.BLACK)
        
        # パドルとボールの描画
        self.player_paddle.draw(self.window.screen)
        self.cpu_paddle.draw(self.window.screen)
        self.ball.draw(self.window.screen)
        
        # 中央線の描画
        center_x = GameSettings.WINDOW_WIDTH // 2
        pygame.draw.line(
            self.window.screen,
            GameSettings.WHITE,
            (center_x, 0),
            (center_x, GameSettings.WINDOW_HEIGHT),
            2
        )
        
        # スコアとタイマーの表示
        player_score, cpu_score = self.score_manager.get_scores()
        score_text = f"{player_score}  {cpu_score}"
        self.draw_text(score_text, center_x, 50, center=True)
        
        if self.game_timer.is_running:
            timer_text = self.game_timer.get_formatted_time()
            self.draw_text(timer_text, center_x, 100, center=True)
        
        # ゲーム状態メッセージの表示
        message = self.game_state.get_message()
        if message:
            self.draw_text(message, center_x, GameSettings.WINDOW_HEIGHT // 2, center=True)
        
        # 画面更新
        pygame.display.flip()
    
    def draw_text(self, text, x, y, font_size=36, center=False):
        """テキストを描画する"""
        if font_size != 36:
            font = pygame.font.Font(None, font_size)
        else:
            font = self.font
        
        text_surface = font.render(text, True, GameSettings.WHITE)
        
        if center:
            text_rect = text_surface.get_rect()
            text_rect.center = (x, y)
            self.window.screen.blit(text_surface, text_rect)
        else:
            self.window.screen.blit(text_surface, (x, y))
    
    def run(self):
        """メインループ"""
        running = True
        
        while running:
            # FPS制御
            delta_time = self.clock.tick(GameSettings.FPS) / 1000.0
            
            # イベント処理
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    running = False
            
            # ゲーム更新
            self.update(delta_time)
            
            # 画面描画
            self.render()
        
        pygame.quit()