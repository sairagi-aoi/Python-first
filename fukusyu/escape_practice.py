# Python初学者向け：重要なエスケープシーケンス練習

print("=" * 50)
print("Python初学者が覚えるべきエスケープシーケンス")
print("=" * 50)

# 【最重要】1. 改行（\n）
print("\n【1. 改行 \\n】")
print("使用例:")
print("こんにちは\n世界")
print("名前: 田中太郎\n年齢: 25歳\n職業: プログラマー")

# 【重要】2. タブ文字（\t）
print("\n【2. タブ文字 \\t】")
print("使用例:")
print("商品名\t価格\t在庫")
print("りんご\t100円\t50個")
print("バナナ\t80円\t30個")

# 【よく使う】3. クォートのエスケープ
print("\n【3. クォートのエスケープ \\\" \\'】")
print("使用例:")
print("彼は\"おはよう\"と挨拶した")
print('私は\'Python\'を学んでいます')

# 【よく使う】4. バックスラッシュ
print("\n【4. バックスラッシュ \\\\】")
print("使用例:")
print("ファイルパス: C:\\Users\\Documents\\python_files")

# 【便利】5. 生文字列
print("\n【5. 生文字列 r\"\"】")
print("使用例:")
print("通常の書き方:", "C:\\Users\\Documents\\python_files")
print("生文字列:", r"C:\Users\Documents\python_files")

print("\n" + "=" * 50)
print("練習問題:")
print("=" * 50)

# 練習問題
print("\n【問題1】以下の情報を見やすく表示してください:")
print("名前: 佐藤花子")
print("メール: hanako@example.com") 
print("電話: 090-1234-5678")

print("\n答え:")
print("名前:\t佐藤花子\nメール:\thanako@example.com\n電話:\t090-1234-5678")

print("\n【問題2】以下のセリフを表示してください:")
print("「今日は\"いい天気\"ですね」と彼女は言った")

print("\n答え:")
print("「今日は\\\"いい天気\\\"ですね」と彼女は言った")
