# 文字列の掛け算（繰り返し）について詳しく解説

print("=== 文字列 × 数値 の仕組み ===")

# 基本的な例
print("基本例:")
print("'A' * 3 =", 'A' * 3)
print("'Hello' * 2 =", 'Hello' * 2)
print("'★' * 1 =", '★' * 1)
print("'★' * 2 =", '★' * 2)
print("'★' * 3 =", '★' * 3)
print("'★' * 4 =", '★' * 4)
print("'★' * 5 =", '★' * 5)

print("\n" + "="*50)

# よつばコードでの実際の動作
print("=== よつばコードでの実際の動作 ===")
count = 1
while count < 5:
    count += 1
    print(f"count = {count}")
    kawaii_level = "★" * count
    print(f"'★' * {count} = {kawaii_level}")
    print(f"よつばが{count}かわいい {kawaii_level}")
    print("-" * 30)

print("\n" + "="*50)

# ステップバイステップ解説
print("=== ステップバイステップ解説 ===")

print("1回目のループ:")
count = 2  # count += 1 後の値
print(f"  count = {count}")
kawaii_level = "★" * count
print(f"  kawaii_level = '★' * {count}")
print(f"  kawaii_level = {kawaii_level}")
print(f"  結果: よつばが{count}かわいい {kawaii_level}")

print("\n2回目のループ:")
count = 3
print(f"  count = {count}")
kawaii_level = "★" * count
print(f"  kawaii_level = '★' * {count}")
print(f"  kawaii_level = {kawaii_level}")
print(f"  結果: よつばが{count}かわいい {kawaii_level}")

print("\n3回目のループ:")
count = 4
print(f"  count = {count}")
kawaii_level = "★" * count
print(f"  kawaii_level = '★' * {count}")
print(f"  kawaii_level = {kawaii_level}")
print(f"  結果: よつばが{count}かわいい {kawaii_level}")

print("\n" + "="*50)

# 他の文字での例
print("=== 他の文字での例 ===")
count = 3

# ハート
heart_level = "💖" * count
print(f"'💖' * {count} = {heart_level}")

# 音符
music_level = "♪" * count
print(f"'♪' * {count} = {music_level}")

# 感嘆符
exclamation = "!" * count
print(f"'!' * {count} = {exclamation}")

# 文字列
word_repeat = "かわいい" * count
print(f"'かわいい' * {count} = {word_repeat}")

print("\n" + "="*50)

# 実用的な使用例
print("=== 実用的な使用例 ===")

# プログレスバー風
print("プログレスバー風:")
for i in range(1, 6):
    progress = "■" * i + "□" * (5-i)
    print(f"進捗 {i}/5: [{progress}]")

print("\nレベル表示:")
for level in range(1, 6):
    stars = "⭐" * level
    print(f"レベル{level}: {stars}")

print("\n区切り線作成:")
separator = "-" * 40
print(separator)
print("ここは重要な部分です")
print(separator)

print("\n" + "="*50)

# 変数との組み合わせ
print("=== 変数との組み合わせ ===")
favorite_char = "🌸"
repeat_count = 5
result = favorite_char * repeat_count
print(f"好きな文字: {favorite_char}")
print(f"繰り返し回数: {repeat_count}")
print(f"結果: {result}")

print("\n数値が0の場合:")
zero_result = "★" * 0
print(f"'★' * 0 = '{zero_result}' (空文字になります)")

print("\n負の数の場合:")
negative_result = "★" * -1
print(f"'★' * -1 = '{negative_result}' (空文字になります)")
