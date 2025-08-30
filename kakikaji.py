name = input("あなたの名前を教えてください。 >>")
department = input("あなたの所属部署を教えてください。>>")
condition = input("今日の体調は10点満点中何点ですか？ >>")
sleep = input("昨晩の睡眠時間を教えてください。 >>")
fatigue = input("怠さや疲れは10点満点中何点ですか？ >>")
feeling = input("今日の気分を教えてください。 >>")

print(f"おはようございます{name}さん。{department}所属ですね。")
print(f"今日の体調は{condition}とのことですね。無理なさらずに頑張ってください。")
print(f"昨晩の睡眠時間は{sleep}とのことですね。")
print(f"怠さや疲れの数値は{fatigue}とのことですね。")
print(f"今日の気分は{feeling}とのことですね。")
print(f"回答ありがとうございました。この健康調査の内容は週末に平均値が出ますので、ご自身の体調管理に役立ててください。")

# =============================================================================
# 改良版サンプルコード
# =============================================================================

import datetime
import csv
import os

def get_valid_score(prompt, min_val=1, max_val=10):
    """指定された範囲内の数値を取得する関数"""
    while True:
        try:
            score = int(input(prompt))
            if min_val <= score <= max_val:
                return score
            else:
                print(f"  ⚠️  {min_val}から{max_val}の間で入力してください")
        except ValueError:
            print("  ⚠️  数値で入力してください")

def get_valid_sleep_time(prompt):
    """睡眠時間を取得する関数（小数点も許可）"""
    while True:
        try:
            sleep_time = float(input(prompt))
            if 0 <= sleep_time <= 24:
                return sleep_time
            else:
                print("  ⚠️  0から24時間の間で入力してください")
        except ValueError:
            print("  ⚠️  数値で入力してください（例：7.5）")

def collect_health_data():
    """健康データを収集する関数"""
    print("="*50)
    print("🌅 朝の健康調査システム")
    print("="*50)
    
    # 基本情報の収集
    name = input("👤 あなたの名前を教えてください >> ")
    while not name.strip():
        print("  ⚠️  名前を入力してください")
        name = input("👤 あなたの名前を教えてください >> ")
    
    department = input("🏢 あなたの所属部署を教えてください >> ")
    while not department.strip():
        print("  ⚠️  部署名を入力してください")
        department = input("🏢 あなたの所属部署を教えてください >> ")
    
    # 数値データの収集
    condition = get_valid_score("💪 今日の体調は10点満点中何点ですか？（1-10）>> ")
    sleep_time = get_valid_sleep_time("😴 昨晩の睡眠時間を教えてください（時間、例：7.5）>> ")
    fatigue = get_valid_score("😵 怠さや疲れは10点満点中何点ですか？（1-10）>> ")
    
    feeling = input("😊 今日の気分を教えてください >> ")
    while not feeling.strip():
        print("  ⚠️  気分を入力してください")
        feeling = input("😊 今日の気分を教えてください >> ")
    
    return {
        'date': datetime.date.today().strftime('%Y-%m-%d'),
        'name': name.strip(),
        'department': department.strip(),
        'condition': condition,
        'sleep_time': sleep_time,
        'fatigue': fatigue,
        'feeling': feeling.strip()
    }

def display_summary(data):
    """収集したデータのサマリーを表示する関数"""
    print("\n" + "="*50)
    print("📋 入力内容の確認")
    print("="*50)
    print(f"👤 お名前: {data['name']}さん")
    print(f"🏢 所属部署: {data['department']}")
    print(f"📅 日付: {data['date']}")
    print(f"💪 体調: {data['condition']}点/10点")
    print(f"😴 睡眠時間: {data['sleep_time']}時間")
    print(f"😵 疲労度: {data['fatigue']}点/10点")
    print(f"😊 気分: {data['feeling']}")
    
    # 簡単な健康アドバイス
    print("\n" + "-"*30)
    print("💡 今日のアドバイス")
    print("-"*30)
    
    if data['condition'] <= 5:
        print("🚨 体調が良くないようです。無理をせず、必要に応じて休憩を取ってください。")
    elif data['condition'] <= 7:
        print("⚠️ 体調がやや低めです。水分補給を忘れずに。")
    else:
        print("✅ 体調良好ですね！今日も頑張りましょう。")
    
    if data['sleep_time'] < 6:
        print("😴 睡眠不足のようです。今夜は早めに就寝することをお勧めします。")
    elif data['sleep_time'] > 9:
        print("😪 睡眠時間が長めですね。睡眠の質も大切です。")
    
    if data['fatigue'] >= 7:
        print("🔋 疲労が蓄積しているようです。適度な休憩を心がけてください。")

def save_data(data):
    """データをCSVファイルに保存する関数"""
    filename = 'health_survey_data.csv'
    file_exists = os.path.exists(filename)
    
    try:
        with open(filename, 'a', newline='', encoding='utf-8') as file:
            fieldnames = ['date', 'name', 'department', 'condition', 'sleep_time', 'fatigue', 'feeling']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            
            # ファイルが新規作成の場合はヘッダーを書く
            if not file_exists:
                writer.writeheader()
            
            writer.writerow(data)
        
        print(f"\n💾 データが正常に保存されました（{filename}）")
    except Exception as e:
        print(f"\n❌ データの保存に失敗しました: {e}")

def confirm_save():
    """保存の確認を取る関数"""
    while True:
        save_choice = input("\n💾 このデータを保存しますか？ (y/n) >> ").lower().strip()
        if save_choice in ['y', 'yes', 'はい']:
            return True
        elif save_choice in ['n', 'no', 'いいえ']:
            return False
        else:
            print("  ⚠️  'y'または'n'で回答してください")

def main():
    """メイン関数"""
    try:
        # データ収集
        health_data = collect_health_data()
        
        # サマリー表示
        display_summary(health_data)
        
        # 保存確認と実行
        if confirm_save():
            save_data(health_data)
        else:
            print("\n📝 データは保存されませんでした。")
        
        print("\n" + "="*50)
        print("✨ 健康調査を完了しました。今日も良い一日をお過ごしください！")
        print("="*50)
        
    except KeyboardInterrupt:
        print("\n\n👋 プログラムが中断されました。お疲れ様でした。")
    except Exception as e:
        print(f"\n❌ エラーが発生しました: {e}")

# 改良版を実行する場合は以下のコメントアウトを外してください
# if __name__ == "__main__":
#     main()

name = input("あなたの名前を教えてください。 >>")
department = input("あなたの所属部署を教えてください。>>")
condition = ""
while not condition
condition = input("今日の体調は10点満点中何点ですか？ >>")

sleep = input("昨晩の睡眠時間を教えてください。 >>")
fatigue = input("怠さや疲れは10点満点中何点ですか？ >>")
feeling = input("今日の気分を教えてください。 >>")

print(f"おはようございます{name}さん。{department}所属ですね。")
print(f"今日の体調は{condition}とのことですね。無理なさらずに頑張ってください。")
print(f"昨晩の睡眠時間は{sleep}とのことですね。")
print(f"怠さや疲れの数値は{fatigue}とのことですね。")
print(f"今日の気分は{feeling}とのことですね。")
print(f"回答ありがとうございました。この健康調査の内容は週末に平均値が出ますので、ご自身の体調管理に役立ててください。")