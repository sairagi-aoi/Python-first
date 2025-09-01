# while文で無限ループになる例

print("=== 無限ループの例（実行注意！） ===")
print("以下のコードは無限ループになります")

# 例1: 条件変数を更新し忘れ
print("\n例1: 条件変数を更新し忘れ")
print("count = 0")
print("while count < 3:")
print("    print(f'ひつじが{count}匹')")
print("    # count += 1 を忘れる → 無限ループ")

# 例2: 条件が満たされない方向に変更
print("\n例2: 条件が満たされない方向に変更")
print("count = 0")
print("while count < 3:")
print("    count -= 1  # 減算してしまう")
print("    print(f'ひつじが{count}匹')")

# 例3: 条件式の書き間違い
print("\n例3: 条件式の書き間違い")
print("count = 0")
print("while count != 10:")
print("    count += 2  # 2ずつ増加（10を飛び越す）")
print("    print(f'ひつじが{count}匹')")

# 例4: True定数を使う
print("\n例4: True定数を使う")
print("while True:")
print("    print('永遠に続く')")
print("    # break文がない")

# 例5: ネストした条件での更新忘れ
print("\n例5: ネストした条件での更新忘れ")
print("count = 0")
print("while count < 5:")
print("    if count % 2 == 0:")
print("        print(f'偶数: {count}')")
print("        count += 1")
print("    else:")
print("        print(f'奇数: {count}')")
print("        # この場合のcount更新を忘れる")

print("\n=== 正しい書き方（参考） ===")

# 正しい例1
print("\n正しい例1: 基本的なカウンター")
count = 0
while count < 3:
    count += 1
    print(f"ひつじが{count}匹")
print("おやすみなさい")

# 正しい例2: break文を使用
print("\n正しい例2: break文を使用")
count = 0
while True:
    count += 1
    print(f"ひつじが{count}匹")
    if count >= 3:
        break
print("おやすみなさい")

# 正しい例3: 複雑な条件
print("\n正しい例3: 複雑な条件での正しい更新")
count = 0
while count < 5:
    if count % 2 == 0:
        print(f"偶数: {count}")
    else:
        print(f"奇数: {count}")
    count += 1  # 必ず更新
