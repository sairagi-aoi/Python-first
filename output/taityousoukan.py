from datetime import datetime

TEXT_FILE = "health_cat_log.txt"
OWNER_SCALE = {"最悪": -2, "悪い": -1, "普通": 0, "良い": 1, "絶好調": 2}
CAT_SCALE = {"ぐったり": -2, "元気ない": -1, "普通": 0, "元気": 1, "走り回ってる": 2}

def ask_choice(prompt: str, choices: list[str]) -> str: #プロンプトと選択肢を整数化
    """choices以外は受け付けずに再入力させる"""
    visible = "/".join(choices)
    while True:
        x = input(f"{prompt} {visible} >> ").strip()
        if x in choices:
            return x
        print(f"入力は{visible}から選んでください。")

def ask_nonempty(prompt: str) -> str:
    """空文字を禁止する"""
    while True:
        x = input(prompt).strip()
        if x:
            return x
        print("空欄は不可です。もう一度入力してください。")


def log_entry():
    owner = ask_nonempty("あなたの名前を教えてください: ")
    cat = ask_nonempty("飼い猫の名前教えてください: ")

#飼い主の体調　（選択肢バリデーション）

cat_condition = ask_choice("飼い猫の様子を教えて下さい",list(CAT_SCALE.keys()))
cat_detail = {}
if cat_condition in ("ぐったり","元気ない"):
    cat_detail["since"] = ask_nonempty("いつ頃から続いていますか？ >> ")
    cat_detail["eating"] ask_choice("食欲はありますか？", ["ある","ない", "不明"])
    cat_detail["play"] = ask_choice("遊んでいますか？",["遊ぶ","遊ばない","不明"])
    cat_detail["drink"] = ask_choice("水を飲んでいますか？",["飲む","飲まない","不明"])
    cat_detail["toilet"] = ask_choice("トイレの様子はどうですか？" ,["正常","下痢","便秘","嘔吐あり","不明"])

else:
    print("いいですね！ その調子を維持できる様にサポートしてあげて下さい。")

#保存条件：どちらかが不調の時だけ
should_save = (OWNER_condition in ("最悪","悪い")) or (cat_condition in ("ぐったり","元気ない")
if not should_save:
    print("両者とも良好の為、今回は記録をスキップしました。")
    return
    
    
    
# 現在時刻を取得
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #出力形式を組み立て
    lines = [
        f" === 飼い猫と飼い主の健康状態相関調査ログ" ({timestamp}) ===",
        f"飼い主の名前： {owner}",
        f"飼い主の体調： {OWNER_condition} ({OWNER_SCALE{owner_condition}})",
    ]
    if owner_detail:
        lines +=[
            f"体調不良の種類: {owner_detail['type']}",
            f"発生時期 : {owner_detail['since']}",
            f"原因: {owner_detail['cause']}",

        ]
    line += [
        f"飼い猫の名前: {cat}",
        f"飼い猫の体調: {cat_condition} ({CAT_SCALE[cat_condition]})",
    ]
    if cat_detail:
        lines += [
            f"現在の飼い猫の様子 (開始時期) : {cat_detail['sine']}",
            f"飼い猫の食欲 : {cat_detail['eating']}",
            f"飼い猫の遊び: {cat_detail['play']}",
            f"飼い猫の水分摂取: {cat_detail['drink']}",
            f"飼い猫のトイレの様子: {cat_detail['toilet']}",
        ]

    record = "\n".join(lines)+"\n\n"

    #ここまで書いた（2025/11/04 21:45）
    


    ]
    


#　テキストファイルに保存（エラー種別ごとに案内）
try:
    with open(TEXT_FILE, "a", encoding="utf-8") as f:
        f.write(record)
    print("回答が正常に保存されました。後ほど印刷していただけます。")
except PermissionError:
    print("保存に失敗しました。ファイルへのアクセス権限がありません。")
except FileNotFoundError:
    print("保存に失敗しました。指定されたファイルが見つかりません。")
except OSError as e:
    print(f"保存に失敗しました。OSにエラーが発生しました: {e}")


elif OWNER_condition in ("普通","良い","絶好調") and CAT_condition in ("普通","元気","走り回ってる"):
    print("いいですね！ その調子で過ごしましょう！")
    break
else :
    print("表示されている選択肢の中からお選びください。")