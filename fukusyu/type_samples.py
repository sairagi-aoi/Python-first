# type()関数のサンプルコード集
# Python初学者から発展レベルまで

print("=" * 50)
print("🔰 初学者向け：基本的なtype()の使い方")
print("=" * 50)

# 1. 基本的なデータ型の確認
print("1. 基本的なデータ型の確認")
name = "佐藤"
age = 25
height = 170.5
is_student = True

print(f"name = '{name}' のデータ型: {type(name)}")
print(f"age = {age} のデータ型: {type(age)}")
print(f"height = {height} のデータ型: {type(height)}")
print(f"is_student = {is_student} のデータ型: {type(is_student)}")
print()

# 2. 型変換前後での型確認
print("2. 型変換前後での型確認")
x = "123"
print(f"変換前: x = '{x}', type: {type(x)}")

y = int(x)
print(f"変換後: y = {y}, type: {type(y)}")

z = float(x)
print(f"変換後: z = {z}, type: {type(z)}")
print()

# 3. リストと辞書の型確認
print("3. リストと辞書の型確認")
fruits = ["りんご", "バナナ", "みかん"]
student_info = {"名前": "田中", "年齢": 20}

print(f"fruits = {fruits}, type: {type(fruits)}")
print(f"student_info = {student_info}, type: {type(student_info)}")
print()

print("=" * 50)
print("🚀 発展向け：実用的なtype()の活用")
print("=" * 50)

# 4. 条件分岐でのtype()活用
print("4. 条件分岐でのtype()活用")
def process_data(data):
    """データの型に応じて異なる処理を行う関数"""
    if type(data) == str:
        return f"文字列: '{data}' (文字数: {len(data)})"
    elif type(data) == int:
        return f"整数: {data} (2倍すると: {data * 2})"
    elif type(data) == float:
        return f"浮動小数点数: {data} (小数点以下: {data % 1})"
    elif type(data) == list:
        return f"リスト: 要素数 {len(data)} 個"
    elif type(data) == dict:
        return f"辞書: キー数 {len(data)} 個"
    else:
        return f"未対応の型: {type(data)}"

# テストデータ
test_data = ["Hello", 42, 3.14, [1, 2, 3], {"key": "value"}, (1, 2)]

for data in test_data:
    print(process_data(data))
print()

# 5. isinstance()との比較
print("5. isinstance()との比較")
number = 10

print(f"type(number) == int: {type(number) == int}")
print(f"isinstance(number, int): {isinstance(number, int)}")

# 継承関係がある場合の違い
class Animal:
    pass

class Dog(Animal):
    pass

my_dog = Dog()
print(f"\nmy_dog の型: {type(my_dog)}")
print(f"type(my_dog) == Animal: {type(my_dog) == Animal}")
print(f"isinstance(my_dog, Animal): {isinstance(my_dog, Animal)}")
print()

# 6. デバッグ用のtype()活用
print("6. デバッグ用のtype()活用")
def debug_info(variable_name, variable):
    """変数の詳細情報を表示するデバッグ関数"""
    print(f"変数名: {variable_name}")
    print(f"値: {variable}")
    print(f"型: {type(variable)}")
    print(f"型名: {type(variable).__name__}")
    if hasattr(variable, '__len__'):
        print(f"長さ: {len(variable)}")
    print("-" * 30)

# デバッグ例
test_variables = {
    "message": "こんにちは",
    "score": 85,
    "grades": [90, 85, 92],
    "settings": {"theme": "dark", "lang": "ja"}
}

for var_name, var_value in test_variables.items():
    debug_info(var_name, var_value)

# 7. エラーハンドリングでのtype()活用
print("7. エラーハンドリングでのtype()活用")
def safe_divide(a, b):
    """安全な除算関数（型チェック付き）"""
    if type(a) not in [int, float] or type(b) not in [int, float]:
        return f"エラー: 数値以外が入力されました。a={type(a)}, b={type(b)}"
    
    if b == 0:
        return "エラー: ゼロで割ることはできません"
    
    return a / b

# テスト
print(safe_divide(10, 2))      # 正常
print(safe_divide("10", 2))    # 型エラー
print(safe_divide(10, 0))      # ゼロ除算エラー
print()

print("=" * 50)
print("📝 まとめ")
print("=" * 50)
print("type()は以下の場面で活用できます：")
print("✅ 変数のデータ型確認（デバッグ時）")
print("✅ 型に応じた条件分岐")
print("✅ エラーハンドリング")
print("✅ データ検証")
print("✅ 動的な処理の実装")
