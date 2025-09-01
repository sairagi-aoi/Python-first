# while文の実務での使用例

import time
import random

print("=== while文の実務での使用例 ===\n")

# 1. ユーザー入力の検証
print("1. ユーザー入力の検証")
print("例: パスワード入力（正しいまで繰り返し）")
correct_password = "python123"
attempts = 0
max_attempts = 3

# 実際のコード例（デモ用）
print("コード例:")
print("while True:")
print("    password = input('パスワードを入力してください: ')")
print("    if password == correct_password:")
print("        print('ログイン成功！')")
print("        break")
print("    else:")
print("        attempts += 1")
print("        if attempts >= max_attempts:")
print("            print('ログイン試行回数を超過しました')")
print("            break")
print()

# 2. ファイル処理
print("2. ファイル処理")
print("例: ログファイルの監視")
print("while True:")
print("    try:")
print("        with open('log.txt', 'r') as f:")
print("            new_lines = f.readlines()")
print("            if new_lines:")
print("                process_log_lines(new_lines)")
print("    except FileNotFoundError:")
print("        print('ログファイルが見つかりません')")
print("    time.sleep(5)  # 5秒待機")
print()

# 3. ネットワーク通信の再試行
print("3. ネットワーク通信の再試行")
print("例: API呼び出しの再試行")
retry_count = 0
max_retries = 3
success = False

print("while retry_count < max_retries and not success:")
print("    try:")
print("        response = api_call()")
print("        if response.status_code == 200:")
print("            success = True")
print("            print('API呼び出し成功')")
print("        else:")
print("            raise Exception('APIエラー')")
print("    except Exception as e:")
print("        retry_count += 1")
print("        print(f'再試行 {retry_count}/{max_retries}')")
print("        time.sleep(2)  # 2秒待機してから再試行")
print()

# 4. データ処理
print("4. データ処理")
print("例: リストの要素を順次処理")
tasks = ["タスク1", "タスク2", "タスク3", "タスク4"]
index = 0

print("tasks = ['タスク1', 'タスク2', 'タスク3', 'タスク4']")
print("index = 0")
print("while index < len(tasks):")
print("    current_task = tasks[index]")
print("    print(f'処理中: {current_task}')")
print("    # タスクの処理")
print("    process_task(current_task)")
print("    index += 1")
print()

# 実際の動作例
print("=== 実際の動作例 ===")
print("4. データ処理の実行:")
while index < len(tasks):
    current_task = tasks[index]
    print(f"処理中: {current_task}")
    time.sleep(0.5)  # 処理時間をシミュレート
    index += 1
print("すべてのタスクが完了しました")
print()

# 5. ゲームループ
print("5. ゲームループ")
print("例: 簡単なじゃんけんゲーム")
print("game_running = True")
print("while game_running:")
print("    player_choice = input('じゃんけん (グー/チョキ/パー/終了): ')")
print("    if player_choice == '終了':")
print("        game_running = False")
print("    else:")
print("        computer_choice = random.choice(['グー', 'チョキ', 'パー'])")
print("        result = judge_winner(player_choice, computer_choice)")
print("        print(f'結果: {result}')")
print()

# 6. サーバーの監視
print("6. サーバーの監視")
print("例: システムリソースの監視")
print("while True:")
print("    cpu_usage = get_cpu_usage()")
print("    memory_usage = get_memory_usage()")
print("    ")
print("    if cpu_usage > 80:")
print("        send_alert('CPU使用率が高すぎます')")
print("    if memory_usage > 90:")
print("        send_alert('メモリ使用率が高すぎます')")
print("    ")
print("    time.sleep(60)  # 1分間隔で監視")
print()

# 7. データベース処理
print("7. データベース処理")
print("例: 大量データの分割処理")
print("offset = 0")
print("batch_size = 1000")
print("while True:")
print("    records = fetch_records_from_db(offset, batch_size)")
print("    if not records:")
print("        break  # データがなくなったら終了")
print("    ")
print("    for record in records:")
print("        process_record(record)")
print("    ")
print("    offset += batch_size")
print("    print(f'{offset}件処理完了')")

print("\n=== while文が実務で重要な理由 ===")
print("1. 条件が満たされるまで処理を継続したい場合")
print("2. ユーザーの操作を待つ場合")
print("3. 外部システムとの連携で再試行が必要な場合")
print("4. リアルタイム処理や監視システム")
print("5. 大量データを分割して処理する場合")
