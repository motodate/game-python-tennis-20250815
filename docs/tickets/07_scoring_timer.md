# チケット: スコアとタイマー機能

## 概要
ゲームのスコア管理と60秒のカウントダウンタイマーを実装する。

## 実装内容
- プレイヤーとCPUのスコア管理
- 60秒カウントダウンタイマー
- スコアとタイマーの表示
- タイマー終了時のゲーム終了処理

## ToDo（TDD実装順）

### 1. ScoreManagerクラスのテストを作成
- [ ] tests/test_score_manager.pyを作成
- [ ] ScoreManagerクラスの存在テストを記述
- [ ] 初期スコアが0-0であることのテストを追加
- [ ] テストを実行して失敗することを確認

### 2. ScoreManagerクラスの基本実装
- [ ] src/game/managers/__init__.pyを作成
- [ ] src/game/managers/score_manager.pyを作成
- [ ] ScoreManagerクラスを定義
- [ ] player_scoreとcpu_scoreを0で初期化
- [ ] テストを実行して成功することを確認

### 3. スコア加算のテストを作成
- [ ] add_player_point()メソッドのテストを追加
- [ ] add_cpu_point()メソッドのテストを追加
- [ ] スコアが正しく増加することのテストを追加
- [ ] テストを実行して失敗することを確認

### 4. スコア加算を実装
- [ ] add_player_point()メソッドを実装
- [ ] add_cpu_point()メソッドを実装
- [ ] 各メソッドでスコアを1増加
- [ ] テストを実行して成功することを確認

### 5. スコア取得のテストを作成
- [ ] get_player_score()メソッドのテストを追加
- [ ] get_cpu_score()メソッドのテストを追加
- [ ] get_scores()メソッドのテストを追加（タプル返却）
- [ ] テストを実行して失敗することを確認

### 6. スコア取得を実装
- [ ] get_player_score()メソッドを実装
- [ ] get_cpu_score()メソッドを実装
- [ ] get_scores()メソッドを実装（(player, cpu)を返す）
- [ ] テストを実行して成功することを確認

### 7. スコアリセットのテストを作成
- [ ] reset()メソッドのテストを追加
- [ ] スコアが0-0にリセットされることのテストを追加
- [ ] テストを実行して失敗することを確認

### 8. スコアリセットを実装
- [ ] reset()メソッドを実装
- [ ] player_scoreとcpu_scoreを0に設定
- [ ] テストを実行して成功することを確認

### 9. GameTimerクラスのテストを作成
- [ ] tests/test_game_timer.pyを作成
- [ ] GameTimerクラスの存在テストを記述
- [ ] 初期時間が60秒であることのテストを追加
- [ ] テストを実行して失敗することを確認

### 10. GameTimerクラスの基本実装
- [ ] src/game/managers/game_timer.pyを作成
- [ ] GameTimerクラスを定義
- [ ] GAME_DURATION = 60を定義
- [ ] remaining_timeを60で初期化
- [ ] テストを実行して成功することを確認

### 11. タイマー更新のテストを作成
- [ ] update()メソッドのテストを追加
- [ ] delta_timeで時間が減少することのテストを追加
- [ ] 0未満にならないことのテストを追加
- [ ] テストを実行して失敗することを確認

### 12. タイマー更新を実装
- [ ] update(delta_time)メソッドを実装
- [ ] remaining_time -= delta_timeの処理を追加
- [ ] max(0, remaining_time)でクランプ処理
- [ ] テストを実行して成功することを確認

### 13. タイマー状態のテストを作成
- [ ] is_expired()メソッドのテストを追加
- [ ] get_remaining_time()メソッドのテストを追加
- [ ] get_formatted_time()メソッドのテストを追加（MM:SS形式）
- [ ] テストを実行して失敗することを確認

### 14. タイマー状態を実装
- [ ] is_expired()メソッドを実装（remaining_time <= 0）
- [ ] get_remaining_time()メソッドを実装
- [ ] get_formatted_time()メソッドを実装（分:秒形式）
- [ ] テストを実行して成功することを確認

### 15. タイマーリセットのテストを作成
- [ ] reset()メソッドのテストを追加
- [ ] start()メソッドのテストを追加
- [ ] stop()メソッドのテストを追加
- [ ] テストを実行して失敗することを確認

### 16. タイマーリセットを実装
- [ ] reset()メソッドを実装（remaining_time = 60）
- [ ] start()メソッドを実装（is_running = True）
- [ ] stop()メソッドを実装（is_running = False）
- [ ] 全テストを実行して成功することを確認

## 完了条件
- [ ] スコアが正しく加算・表示される
- [ ] 60秒カウントダウンが動作する
- [ ] タイマー終了時に適切な処理が行われる
- [ ] pytest tests/test_score_manager.pyとtest_game_timer.pyが全てパスする