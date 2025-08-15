# チケット: ゲーム状態管理

## 概要
ゲームの状態（開始前、プレイ中、ゲームオーバー）を管理し、状態遷移とメッセージ表示を制御する。

## 実装内容
- ゲーム状態の定義（WAITING、PLAYING、GAME_OVER）
- 状態遷移の管理
- 各状態でのメッセージ表示
- Enterキーによる状態遷移処理

## ToDo（TDD実装順）

### 1. GameStateクラスのテストを作成
- [x] tests/test_game_state.pyを作成
- [x] GameStateクラスの存在テストを記述
- [x] 初期状態がWAITINGであることのテストを追加
- [x] テストを実行して失敗することを確認

### 2. GameStateクラスの基本実装
- [x] src/game/state/__init__.pyを作成
- [x] src/game/state/game_state.pyを作成
- [x] GameStateクラスを定義
- [x] State列挙型を定義（WAITING、PLAYING、GAME_OVER）
- [x] 初期状態をWAITINGに設定
- [x] テストを実行して成功することを確認

### 3. 状態遷移のテストを作成
- [x] set_state()メソッドのテストを追加
- [x] get_state()メソッドのテストを追加
- [x] 状態変更が正しく反映されることのテストを追加
- [x] テストを実行して失敗することを確認

### 4. 状態遷移を実装
- [x] set_state(new_state)メソッドを実装
- [x] get_state()メソッドを実装
- [x] current_state属性で状態を管理
- [x] テストを実行して成功することを確認

### 5. 状態別処理のテストを作成
- [x] is_waiting()メソッドのテストを追加
- [x] is_playing()メソッドのテストを追加
- [x] is_game_over()メソッドのテストを追加
- [x] テストを実行して失敗することを確認

### 6. 状態別処理を実装
- [x] is_waiting()メソッドを実装
- [x] is_playing()メソッドを実装
- [x] is_game_over()メソッドを実装
- [x] テストを実行して成功することを確認

### 7. ゲーム開始処理のテストを作成
- [x] start_game()メソッドのテストを追加
- [x] WAITINGからPLAYINGへの遷移テストを追加
- [x] GAME_OVERからWAITINGへのリセットテストを追加
- [x] テストを実行して失敗することを確認

### 8. ゲーム開始処理を実装
- [x] start_game()メソッドを実装
- [x] 状態をPLAYINGに変更
- [x] ゲーム開始時の初期化処理を追加
- [x] テストを実行して成功することを確認

### 9. ゲーム終了処理のテストを作成
- [x] end_game()メソッドのテストを追加
- [x] PLAYINGからGAME_OVERへの遷移テストを追加
- [x] 最終スコアの保存テストを追加
- [x] テストを実行して失敗することを確認

### 10. ゲーム終了処理を実装
- [x] end_game(final_score)メソッドを実装
- [x] 状態をGAME_OVERに変更
- [x] final_score属性に最終スコアを保存
- [x] テストを実行して成功することを確認

### 11. リセット処理のテストを作成
- [x] reset()メソッドのテストを追加
- [x] GAME_OVERからWAITINGへの遷移テストを追加
- [x] スコアがクリアされることのテストを追加
- [x] テストを実行して失敗することを確認

### 12. リセット処理を実装
- [x] reset()メソッドを実装
- [x] 状態をWAITINGに変更
- [x] スコアやタイマーのリセット処理を追加
- [x] テストを実行して成功することを確認

### 13. メッセージ取得のテストを作成
- [x] get_message()メソッドのテストを追加
- [x] WAITING時のメッセージテストを追加
- [x] GAME_OVER時のメッセージテストを追加
- [x] テストを実行して失敗することを確認

### 14. メッセージ取得を実装
- [x] get_message()メソッドを実装
- [x] WAITING: "Press Enter to Start"を返す
- [x] GAME_OVER: "Game Over"を返す
- [x] PLAYING: Noneを返す
- [x] 全テストを実行して成功することを確認

## 完了条件
- [x] 3つの状態が正しく管理される
- [x] 状態遷移が適切に動作する
- [x] 各状態で適切なメッセージが表示される
- [x] pytest tests/test_game_state.pyが全てパスする