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
- [x] tests/test_score_manager.pyを作成
- [x] ScoreManagerクラスの存在テストを記述
- [x] 初期スコアが0-0であることのテストを追加
- [x] テストを実行して失敗することを確認

### 2. ScoreManagerクラスの基本実装
- [x] src/game/managers/__init__.pyを作成
- [x] src/game/managers/score_manager.pyを作成
- [x] ScoreManagerクラスを定義
- [x] player_scoreとcpu_scoreを0で初期化
- [x] テストを実行して成功することを確認

### 3. スコア加算のテストを作成
- [x] add_player_point()メソッドのテストを追加
- [x] add_cpu_point()メソッドのテストを追加
- [x] スコアが正しく増加することのテストを追加
- [x] テストを実行して失敗することを確認

### 4. スコア加算を実装
- [x] add_player_point()メソッドを実装
- [x] add_cpu_point()メソッドを実装
- [x] 各メソッドでスコアを1増加
- [x] テストを実行して成功することを確認

### 5. スコア取得のテストを作成
- [x] get_player_score()メソッドのテストを追加
- [x] get_cpu_score()メソッドのテストを追加
- [x] get_scores()メソッドのテストを追加（タプル返却）
- [x] テストを実行して失敗することを確認

### 6. スコア取得を実装
- [x] get_player_score()メソッドを実装
- [x] get_cpu_score()メソッドを実装
- [x] get_scores()メソッドを実装（(player, cpu)を返す）
- [x] テストを実行して成功することを確認

### 7. スコアリセットのテストを作成
- [x] reset()メソッドのテストを追加
- [x] スコアが0-0にリセットされることのテストを追加
- [x] テストを実行して失敗することを確認

### 8. スコアリセットを実装
- [x] reset()メソッドを実装
- [x] player_scoreとcpu_scoreを0に設定
- [x] テストを実行して成功することを確認

### 9. GameTimerクラスのテストを作成
- [x] tests/test_game_timer.pyを作成
- [x] GameTimerクラスの存在テストを記述
- [x] 初期時間が60秒であることのテストを追加
- [x] テストを実行して失敗することを確認

### 10. GameTimerクラスの基本実装
- [x] src/game/managers/game_timer.pyを作成
- [x] GameTimerクラスを定義
- [x] GAME_DURATION = 60を定義
- [x] remaining_timeを60で初期化
- [x] テストを実行して成功することを確認

### 11. タイマー更新のテストを作成
- [x] update()メソッドのテストを追加
- [x] delta_timeで時間が減少することのテストを追加
- [x] 0未満にならないことのテストを追加
- [x] テストを実行して失敗することを確認

### 12. タイマー更新を実装
- [x] update(delta_time)メソッドを実装
- [x] remaining_time -= delta_timeの処理を追加
- [x] max(0, remaining_time)でクランプ処理
- [x] テストを実行して成功することを確認

### 13. タイマー状態のテストを作成
- [x] is_expired()メソッドのテストを追加
- [x] get_remaining_time()メソッドのテストを追加
- [x] get_formatted_time()メソッドのテストを追加（MM:SS形式）
- [x] テストを実行して失敗することを確認

### 14. タイマー状態を実装
- [x] is_expired()メソッドを実装（remaining_time <= 0）
- [x] get_remaining_time()メソッドを実装
- [x] get_formatted_time()メソッドを実装（分:秒形式）
- [x] テストを実行して成功することを確認

### 15. タイマーリセットのテストを作成
- [x] reset()メソッドのテストを追加
- [x] start()メソッドのテストを追加
- [x] stop()メソッドのテストを追加
- [x] テストを実行して失敗することを確認

### 16. タイマーリセットを実装
- [x] reset()メソッドを実装（remaining_time = 60）
- [x] start()メソッドを実装（is_running = True）
- [x] stop()メソッドを実装（is_running = False）
- [x] 全テストを実行して成功することを確認

## 完了条件
- [x] スコアが正しく加算・表示される
- [x] 60秒カウントダウンが動作する
- [x] タイマー終了時に適切な処理が行われる
- [x] pytest tests/test_score_manager.pyとtest_game_timer.pyが全てパスする