# Pythonでユーザー入力を受け付ける方法

# 1. 基本的な入力（文字列として受け取る）
name = input("お名前を入力してください: ")
print(f"こんにちは、{name}さん！")

# 2. 数値として受け取る場合
age = int(input("年齢を入力してください: "))
print(f"あなたは{age}歳ですね")

# 3. 小数点を含む数値の場合
height = float(input("身長を入力してください（cm）: "))
print(f"身長は{height}cmですね")

# 4. 複数の値を一度に受け取る場合
print("好きな食べ物を3つ、スペース区切りで入力してください:")
foods = input().split()
print(f"好きな食べ物: {foods}")

# 5. エラーハンドリングを含む入力
try:
    score = int(input("テストの点数を入力してください: "))
    if 0 <= score <= 100:
        print(f"点数: {score}点")
    else:
        print("0〜100の範囲で入力してください")
except ValueError:
    print("数値を入力してください")

# 6. Yes/Noの判定
answer = input("続けますか？(y/n): ")
if answer.lower() in ['y', 'yes']:
    print("続行します")
else:
    print("終了します")