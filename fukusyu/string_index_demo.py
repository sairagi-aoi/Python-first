# 文字列のインデックス（番号）について詳しく解説

print("=== 文字列のインデックスの仕組み ===")

# 基本的な文字列
name = "よつば"

print(f"文字列: '{name}'")
print(f"文字列の長さ: {len(name)}")

print("\n各文字のインデックス（番号）:")
print("インデックス:  0   1   2")
print("文字:        よ  つ  ば")
print("             ↑   ↑   ↑")
print("            [0] [1] [2]")

print("\n" + "="*50)

# 実際にインデックスで文字を取得
print("=== 実際にインデックスで文字を取得 ===")
print(f"name[0] = '{name[0]}'")
print(f"name[1] = '{name[1]}'")
print(f"name[2] = '{name[2]}'")

print("\n" + "="*50)

# ステップバイステップで解説
print("=== ステップバイステップ解説 ===")

name = "よつば"
print(f"name = '{name}'")
print(f"len(name) = {len(name)}")

print("\nwhile文の動作:")

# 1回目のループ
print("\n【1回目のループ】")
index = 0
print(f"index = {index}")
print(f"index < len(name) → {index} < {len(name)} → {index < len(name)}")
if index < len(name):
    char = name[index]
    print(f"char = name[{index}] = '{char}'")
    hearts = "💖" * (index + 1)
    print(f"hearts = '💖' * ({index} + 1) = '💖' * {index + 1} = '{hearts}'")
    print(f"出力: '{char}ちゃん{hearts}'")
    index += 1
    print(f"index += 1 → index = {index}")

# 2回目のループ
print("\n【2回目のループ】")
print(f"index = {index}")
print(f"index < len(name) → {index} < {len(name)} → {index < len(name)}")
if index < len(name):
    char = name[index]
    print(f"char = name[{index}] = '{char}'")
    hearts = "💖" * (index + 1)
    print(f"hearts = '💖' * ({index} + 1) = '💖' * {index + 1} = '{hearts}'")
    print(f"出力: '{char}ちゃん{hearts}'")
    index += 1
    print(f"index += 1 → index = {index}")

# 3回目のループ
print("\n【3回目のループ】")
print(f"index = {index}")
print(f"index < len(name) → {index} < {len(name)} → {index < len(name)}")
if index < len(name):
    char = name[index]
    print(f"char = name[{index}] = '{char}'")
    hearts = "💖" * (index + 1)
    print(f"hearts = '💖' * ({index} + 1) = '💖' * {index + 1} = '{hearts}'")
    print(f"出力: '{char}ちゃん{hearts}'")
    index += 1
    print(f"index += 1 → index = {index}")

# 4回目（ループ終了）
print("\n【4回目（ループ終了）】")
print(f"index = {index}")
print(f"index < len(name) → {index} < {len(name)} → {index < len(name)}")
print("条件がFalseなので、ループ終了")

print("\n" + "="*50)

# 実際のコードを動かしてみる
print("=== 実際のコードを動かしてみる ===")
name = "よつば"
index = 0
print(f"開始: name = '{name}', index = {index}")

while index < len(name):
    char = name[index]
    hearts = "💖" * (index + 1)
    print(f"ループ{index + 1}: index={index}, char='{char}', hearts='{hearts}'")
    print(f"出力: {char}ちゃん{hearts}")
    index += 1
    print(f"次のindex: {index}")
    print("-" * 30)

print("ループ終了")

print("\n" + "="*50)

# 他の文字列での例
print("=== 他の文字列での例 ===")

# 短い文字列
short_name = "あい"
print(f"\n短い文字列: '{short_name}'")
print("インデックス:  0   1")
print("文字:         あ  い")

index = 0
while index < len(short_name):
    char = short_name[index]
    print(f"index {index}: '{char}'")
    index += 1

# 長い文字列
long_name = "よつばと"
print(f"\n長い文字列: '{long_name}'")
print("インデックス:  0   1   2   3")
print("文字:         よ  つ  ば  と")

index = 0
while index < len(long_name):
    char = long_name[index]
    print(f"index {index}: '{char}'")
    index += 1

print("\n" + "="*50)

# まとめ
print("=== まとめ ===")
print("1. 文字列の各文字には0から始まる番号（インデックス）が付いている")
print("2. name[0]で最初の文字、name[1]で2番目の文字を取得できる")
print("3. len(name)で文字列の長さがわかる")
print("4. indexを0から始めて、len(name)未満の間ループする")
print("5. 毎回index += 1で次の文字に進む")
print("6. indexがlen(name)に達したらループ終了")

print("\n文字列 'よつば' の場合:")
print("- 長さ: 3")
print("- インデックス 0: 'よ'")
print("- インデックス 1: 'つ'")
print("- インデックス 2: 'ば'")
print("- インデックス 3: 範囲外（ループ終了）")
