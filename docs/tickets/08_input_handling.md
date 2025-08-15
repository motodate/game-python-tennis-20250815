# チケット: 入力処理システム

## 概要
キーボード入力を処理し、プレイヤーパドルの操作とゲーム状態の制御を行う。

## 実装内容
- W/S キーまたは上下矢印キーでパドル操作
- Enterキーでゲーム開始/リスタート
- ESCキーでゲーム終了
- 入力状態の管理

## ToDo（TDD実装順）

### 1. InputHandlerクラスのテストを作成
- [x] tests/test_input_handler.pyを作成
- [x] InputHandlerクラスの存在テストを記述
- [x] テストを実行して失敗することを確認

### 2. InputHandlerクラスの基本実装
- [x] src/game/input/__init__.pyを作成
- [x] src/game/input/input_handler.pyを作成
- [x] InputHandlerクラスを定義
- [x] テストを実行して成功することを確認

### 3. キー状態管理のテストを作成
- [x] update()メソッドのテストを追加
- [x] is_key_pressed()メソッドのテストを追加
- [x] is_key_held()メソッドのテストを追加
- [x] テストを実行して失敗することを確認

### 4. キー状態管理を実装
- [x] update()メソッドを実装（pygame.key.get_pressed()を使用）
- [x] is_key_pressed()メソッドを実装（単発押下判定）
- [x] is_key_held()メソッドを実装（押し続け判定）
- [x] key_states辞書で状態を管理
- [x] テストを実行して成功することを確認

### 5. 移動入力のテストを作成
- [x] is_move_up()メソッドのテストを追加
- [x] is_move_down()メソッドのテストを追加
- [x] WキーとUPキーの両方をテスト
- [x] SキーとDOWNキーの両方をテスト
- [x] テストを実行して失敗することを確認

### 6. 移動入力を実装
- [x] is_move_up()メソッドを実装（K_w or K_UP）
- [x] is_move_down()メソッドを実装（K_s or K_DOWN）
- [x] pygame.K_w, K_s, K_UP, K_DOWNの定数を使用
- [x] テストを実行して成功することを確認

### 7. アクション入力のテストを作成
- [x] is_action_pressed()メソッドのテストを追加
- [x] Enterキー押下のテストを追加
- [x] 単発押下のみ反応することのテストを追加
- [x] テストを実行して失敗することを確認

### 8. アクション入力を実装
- [x] is_action_pressed()メソッドを実装（K_RETURN）
- [x] previous_keysで前フレームの状態を保存
- [x] 押下開始時のみTrueを返す処理を実装
- [x] テストを実行して成功することを確認

### 9. システム入力のテストを作成
- [x] is_quit_pressed()メソッドのテストを追加
- [x] ESCキー押下のテストを追加
- [x] テストを実行して失敗することを確認

### 10. システム入力を実装
- [x] is_quit_pressed()メソッドを実装（K_ESCAPE）
- [x] 単発押下判定を使用
- [x] テストを実行して成功することを確認

### 11. 移動速度計算のテストを作成
- [x] get_player_movement()メソッドのテストを追加
- [x] 上移動時に-1を返すテストを追加
- [x] 下移動時に1を返すテストを追加
- [x] 無入力時に0を返すテストを追加
- [x] テストを実行して失敗することを確認

### 12. 移動速度計算を実装
- [x] get_player_movement()メソッドを実装
- [x] is_move_up()で-1を返す
- [x] is_move_down()で1を返す
- [x] 両方または無入力で0を返す
- [x] テストを実行して成功することを確認

### 13. イベント処理のテストを作成
- [x] handle_events()メソッドのテストを追加
- [x] pygame.QUITイベントのテストを追加
- [x] キーイベントの処理テストを追加
- [x] テストを実行して失敗することを確認

### 14. イベント処理を実装
- [x] handle_events(events)メソッドを実装
- [x] pygame.QUITイベントの処理を追加
- [x] KEYDOWNとKEYUPイベントの処理を追加
- [x] 全テストを実行して成功することを確認

## 完了条件
- [x] W/S/↑/↓キーでパドルが操作できる
- [x] Enterキーでゲームが開始/リスタートする
- [x] ESCキーでゲームが終了する
- [x] pytest tests/test_input_handler.pyが全てパスする