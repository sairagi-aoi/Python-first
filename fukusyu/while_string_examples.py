# while文と文字列の組み合わせ例

print("=== while文と文字列の使用例 ===")

# 例1: 文字列の長さを条件にする
print("1. 文字列の長さを条件にする")
message = "よつば"
index = 0
while index < len(message):
    print(f"{index}番目の文字: {message[index]}")
    index += 1

print("\n" + "="*50)

# 例2: 文字列の中の特定の文字を探す
print("2. 文字列の中の特定の文字を探す")
text = "よつばとひまわり"
index = 0
found = False
while index < len(text) and not found:
    if text[index] == "ひ":
        print(f"'{text[index]}'を{index}番目で発見！")
        found = True
    else:
        print(f"{index}番目: '{text[index]}'")
    index += 1

print("\n" + "="*50)

# 例3: 文字列を一文字ずつ処理
print("3. 文字列を一文字ずつ処理して変換")
original = "yotsuba"
result = ""
index = 0
while index < len(original):
    char = original[index]
    if char in "aeiou":  # 母音の場合
        result += char.upper()  # 大文字にする
    else:
        result += char
    index += 1

print(f"元の文字列: {original}")
print(f"変換後: {result}")

print("\n" + "="*50)

# 例4: 文字列の内容を条件にする
print("4. 文字列の内容を条件にする")
user_input = ""
while user_input != "よつば":
    print(f"現在の入力: '{user_input}'")
    if user_input == "":
        user_input = "あ"
    elif user_input == "あ":
        user_input = "よ"
    elif user_input == "よ":
        user_input = "よつ"
    elif user_input == "よつ":
        user_input = "よつば"
    else:
        user_input = "よつば"
    print(f"次の文字列: '{user_input}'")

print("目標の文字列に到達しました！")

print("\n" + "="*50)

# 例5: 文字列を逆順にする
print("5. 文字列を逆順にする")
word = "よつばちゃん"
reversed_word = ""
index = len(word) - 1  # 最後の文字から開始

while index >= 0:
    reversed_word += word[index]
    print(f"追加: '{word[index]}' → 現在: '{reversed_word}'")
    index -= 1

print(f"元の文字列: {word}")
print(f"逆順: {reversed_word}")

print("\n" + "="*50)

# 例6: 文字列の各文字に番号を付ける
print("6. 文字列の各文字に番号を付ける")
name = "よつば"
char_index = 0
while char_index < len(name):
    char = name[char_index]
    print(f"文字{char_index + 1}: '{char}'")
    char_index += 1

print("\n" + "="*50)

# 例7: 文字列から特定の文字を削除
print("7. 文字列から特定の文字を削除")
text = "よつばとだんぼー"
target_char = "と"
new_text = ""
index = 0

while index < len(text):
    current_char = text[index]
    if current_char != target_char:
        new_text += current_char
        print(f"追加: '{current_char}' → 現在: '{new_text}'")
    else:
        print(f"スキップ: '{current_char}'")
    index += 1

print(f"元の文字列: {text}")
print(f"'{target_char}'を削除後: {new_text}")

print("\n" + "="*50)

# 例8: 文字列の繰り返しパターン
print("8. 文字列の繰り返しパターン")
base_text = "よつば"
repeat_count = 0
full_text = ""

while repeat_count < 3:
    full_text += base_text
    repeat_count += 1
    print(f"{repeat_count}回目: {full_text}")

print(f"最終結果: {full_text}")

print("\n" + "="*50)

# 例9: 文字列を使ったカウンター
print("9. 文字列を使ったカウンター")
counter_text = ""
count = 0

while count < 5:
    count += 1
    counter_text += "♪"
    print(f"カウント{count}: {counter_text}")

print("\n" + "="*50)

# 例10: 文字列の文字数に基づいた処理
print("10. 文字列の文字数に基づいた処理")
words = ["よ", "よつ", "よつば", "よつばちゃん"]
word_index = 0

while word_index < len(words):
    current_word = words[word_index]
    char_count = len(current_word)
    stars = "⭐" * char_count
    print(f"単語: '{current_word}' (文字数: {char_count}) {stars}")
    word_index += 1

print("\n=== まとめ ===")
print("while文と文字列は以下の方法で組み合わせられます:")
print("1. 文字列の長さ（len()）を条件にする")
print("2. 文字列の内容を条件にする")
print("3. 文字列の各文字を順番に処理する")
print("4. 文字列を変更・変換する")
print("5. 文字列を使ってカウンターを作る")

# 例: よつばの名前を一文字ずつ表示
name = "よつば"
index = 0
while index < len(name):
    char = name[index]
    hearts = "💖" * (index + 1)
    print(f"{char}ちゃん {hearts}")
    index += 1