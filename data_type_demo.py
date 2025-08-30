# データ型の違いを確認するデモ

print("=== input()のデータ型確認 ===")

# 1. input()をそのまま使った場合
age_str = input("年齢を入力してください: ")
print(f"入力値: {age_str}")
print(f"データ型: {type(age_str)}")
print(f"これは文字列なので計算できません: age_str + 5 → エラーになります")

print("\n=== int()で変換した場合 ===")

# 2. int()で変換した場合
age_int = int(age_str)
print(f"変換後の値: {age_int}")
print(f"データ型: {type(age_int)}")
print(f"これは数値なので計算できます: {age_int} + 5 = {age_int + 5}")

print("\n=== 文字列と数値の違い ===")
print(f"文字列の場合: '25' + '5' = {'25' + '5'} (文字の連結)")
print(f"数値の場合: 25 + 5 = {25 + 5} (数学的な足し算)")

print("\n=== エラーの例 ===")
try:
    # これはエラーになります
    result = age_str + 5
except TypeError as e:
    print(f"エラー: {e}")
    print("文字列と数値は直接計算できません")
