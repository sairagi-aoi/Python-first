# よつばコードの発展例

import random
import time

print("=== 基本コード ===")
count = 1
while count < 5:
    count += 1
    print(f"よつばが{count}かわいい")
print("よつばちゃん激カワすぎる")

print("\n" + "="*50)

# 発展例1: かわいさレベルを追加
print("=== 発展例1: かわいさレベル追加 ===")
count = 1
while count < 5:
    count += 1
    kawaii_level = "★" * count  # かわいさを星で表現
    print(f"よつばが{count}かわいい {kawaii_level}")
print("よつばちゃん激カワすぎる ★★★★★★")

print("\n" + "="*50)

# 発展例2: ランダムな形容詞
print("=== 発展例2: ランダムな形容詞 ===")
adjectives = ["かわいい", "愛らしい", "キュート", "癒し系", "天使みたい", "最高"]
count = 1
while count < 5:
    count += 1
    random_adj = random.choice(adjectives)
    print(f"よつばが{count}{random_adj}")
print("よつばちゃん激カワすぎる")

print("\n" + "="*50)

# 発展例3: よつばの行動パターン
print("=== 発展例3: よつばの行動パターン ===")
actions = ["笑ってる", "遊んでる", "走ってる", "歌ってる", "踊ってる", "寝てる"]
count = 1
while count < 6:
    count += 1
    action = random.choice(actions)
    print(f"よつば{count}: {action}姿がかわいい")
    time.sleep(0.5)  # 0.5秒間隔
print("よつばちゃんの全ての行動が愛おしい")

print("\n" + "="*50)

# 発展例4: ユーザーとの対話
print("=== 発展例4: ユーザーとの対話（デモ版） ===")
print("よつばのかわいさを評価してください（1-10）:")
# 実際の対話版のコード例を表示
print("コード例:")
print("count = 1")
print("total_score = 0")
print("while count <= 3:")
print("    score = int(input(f'シーン{count}のかわいさは？: '))")
print("    total_score += score")
print("    print(f'よつばシーン{count}: {score}点！')")
print("    count += 1")
print("average = total_score / 3")
print("print(f'よつばの平均かわいさ: {average:.1f}点')")

print("\n" + "="*50)

# 発展例5: データ構造を使った発展
print("=== 発展例5: データ構造を使った発展 ===")
yotsuba_data = [
    {"scene": "お花を摘む", "cuteness": 9, "energy": 7},
    {"scene": "だんぼーと遊ぶ", "cuteness": 10, "energy": 8},
    {"scene": "お昼寝", "cuteness": 8, "energy": 2},
    {"scene": "ケーキを食べる", "cuteness": 9, "energy": 9},
    {"scene": "お父さんと散歩", "cuteness": 10, "energy": 5}
]

count = 0
while count < len(yotsuba_data):
    scene_data = yotsuba_data[count]
    print(f"シーン{count+1}: {scene_data['scene']}")
    print(f"  かわいさ: {'💚' * scene_data['cuteness']}")
    print(f"  元気度: {'⚡' * scene_data['energy']}")
    count += 1

print("全シーンが最高にかわいい！")

print("\n" + "="*50)

# 発展例6: 条件分岐を追加
print("=== 発展例6: 条件分岐を追加 ===")
count = 1
super_kawaii_count = 0

while count < 8:
    count += 1
    kawaii_level = random.randint(1, 10)
    
    if kawaii_level >= 9:
        print(f"よつば{count}: 超絶かわいい！！ (レベル{kawaii_level})")
        super_kawaii_count += 1
    elif kawaii_level >= 7:
        print(f"よつば{count}: とってもかわいい (レベル{kawaii_level})")
    else:
        print(f"よつば{count}: かわいい (レベル{kawaii_level})")

print(f"超絶かわいいシーンが{super_kawaii_count}回もありました！")

print("\n" + "="*50)

# 発展例7: ネストしたループ
print("=== 発展例7: ネストしたループ ===")
day = 1
while day <= 3:
    print(f"\n{day}日目のよつば:")
    activity_count = 1
    while activity_count <= 3:
        activities = ["お絵描き", "外遊び", "お手伝い", "読書", "お菓子作り"]
        activity = random.choice(activities)
        print(f"  活動{activity_count}: {activity}をしてるよつばがかわいい")
        activity_count += 1
    day += 1

print("3日間のよつば観察完了！毎日かわいすぎる！")

print("\n" + "="*50)

# 発展例8: 関数化
print("=== 発展例8: 関数化 ===")

def yotsuba_kawaii_counter(start, end, message_func):
    """よつばのかわいさカウンター（関数版）"""
    count = start
    while count < end:
        count += 1
        message = message_func(count)
        print(message)
    return count

def simple_message(count):
    return f"よつばが{count}かわいい"

def special_message(count):
    emotions = ["😊", "🥰", "😍", "🤗", "💕"]
    return f"よつば{count}番目のかわいさ {random.choice(emotions)}"

# 関数を使用
print("シンプル版:")
yotsuba_kawaii_counter(1, 4, simple_message)

print("\n特別版:")
yotsuba_kawaii_counter(1, 4, special_message)

print("\nよつばちゃん、いつでもかわいい！")
