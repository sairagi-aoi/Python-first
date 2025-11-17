from datetime import datetime
from src.io_csv import append_csv

TEXT_FILE = "health_cat_log.txt"
CSV_FILE = "health_cat_log.csv"

FIELDNAMES = [
    "timestamp", "owner", "cat",
    "owner_condition", "cat_condition",
    "owner_score", "cat_score",
    "condition_type", "condition_since", "condition_cause",
    "condition_yousu", "condition_eating", "condition_play",
    "condition_drink", "condition_toilet"
]

OWNER_SCALE = {"最悪": -2, "悪い": -1, "普通": 0, "良い": 1, "絶好調": 2}
CAT_SCALE = {"ぐったり": -2, "元気ない": -1, "普通": 0, "元気": 1, "走り回ってる": 2}

def ask_choice(prompt: str, choices: list[str]) -> str: #プロンプトと選択肢を整数化
    """choices以外は受け付けずに再入力させる"""
    visible = "/".join(choices)
    while True:
        x = input(f"{prompt} ({visible}) >> ").strip()
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
    owner_condition = ask_choice("あなたの体調を教えて下さい", list(OWNER_SCALE.keys()))
    cat_condition = ask_choice("飼い猫の様子を教えて下さい。", list(CAT_SCALE.keys()))

    #不調時のみ詳細
    owner_detail = {}
    if owner_condition in ("最悪", "悪い"):
        owner_detail["type"] = ask_choice("その体調不良は？", ["精神面","身体面","両方"])
        owner_detail["since"] = ask_nonempty("いつ頃から発生していますか？ >> ")
        owner_detail["cause"] = ask_nonempty("原因として思いあたることはありますか？ (なければ「無し」と答えて下さい) >> ")

    cat_detail = {}
    if cat_condition in ("ぐったり","元気ない"):
        cat_detail["since"] = ask_nonempty(" (猫) その様子はいつ頃から続いていますか？ >> ")
        cat_detail["eating"] = ask_choice(" (猫) 食欲はありますか?", ["ある","ない","どちらともいえない"])
        cat_detail["play"] = ask_choice("(猫) 遊びの様子はどうですか？",["遊んでいる","あまり遊ばない","全く遊ばない"])
        cat_detail["drink"] = ask_choice("(猫) 水は飲んでいますか？",["よく飲んでいる","いつも通り","あまり飲まない","全く飲まない"])
        cat_detail["toilet"] = ask_choice("(猫) トイレの様子は？",["通常","下痢","便秘","その他"])
    else:
        print("いいですね！ その調子を維持できる様にサポートしてあげて下さい。")

    #保存条件：どちらかが不調の時だけ
    should_save = (owner_condition in ("最悪","悪い")) or (cat_condition in ("ぐったり","元気ない"))
    if not should_save:
        print("両者とも良好の為、今回は記録をスキップしました。")
        return
    
    
    
    #出力形式を組み立て
    lines = [
        f" === 飼い猫と飼い主の健康状態相関調査ログ ({timestamp}) ===",
        f"飼い主の名前： {owner}",
        f"飼い主の体調： {owner_condition} ({OWNER_SCALE[owner_condition]})",
    ]
    if owner_detail:
        lines += [
            f"体調不良の種類: {owner_detail['type']}",
            f"発生時期 : {owner_detail['since']}",
            f"原因: {owner_detail['cause']}",

        ]
    lines += [
        f"飼い猫の名前: {cat}",
        f"飼い猫の体調: {cat_condition} ({CAT_SCALE[cat_condition]})",
    ]
    if cat_detail:
        lines += [
            f"現在の飼い猫の様子 (開始時期) : {cat_detail['since']}",
            f"飼い猫の食欲 : {cat_detail['eating']}",
            f"飼い猫の遊び: {cat_detail['play']}",
            f"飼い猫の水分摂取: {cat_detail['drink']}",
            f"飼い猫のトイレの様子: {cat_detail['toilet']}",
        ]

    record = "\n".join(lines)+"\n\n"
    row = {
        "timstamp": timestamp,
        "owner": owner,
        "cat": cat,
        "owner_condition": owner_condition,
        "cat_condition":cat_condition,
        "owner_score": OWNER_SCALE[owner_condition],
        "cat_score": CAT_SCALE[cat_condition],
        "condition_type": owner_detail.get("type", ""),
        "condition_sine": owner_detail.get("sine", "") or cat_detail.get("sine",""),
        "condition_cause": owner_detail.get("since",""),
        "condition_yousu": cat_condition if cat_detail else "",
        "condition_eating": cat_detail.get("eating", ""),
        "condition_play": cat_detail.get("drink",""),
        "condition_drink":cat_detail.get("drink", ""),
        "condition_toilet": cat_detail.get("toilet", "")
    }

    #　テキストファイルに保存（エラー種別ごとに案内）
    try:
        with open(TEXT_FILE, "a", encoding="utf-8") as f:
            f.write(record)
        print("回答が正常に保存されました。後ほど印刷していただけます。")
    except PermissionError:
        print("保存に失敗しました。ファイルへのアクセス権限がありません。")
    except OSError as e:
        print(f"保存に失敗しました。OSにエラーが発生しました: {e}")

    try:
        with open(TEXT_FILE, "a", encoding="utf-8") as f:
            f.write(record)
        append_csv(CSV_FILE, row, FIELDNAMES)
        print("回答がcsvファイルにも保存されました")
    except PermissionError:
        print("保存に失敗しました。ファイルへのアクセス権限がありません。")
    except OSError as e:
        print("保存に失敗しました。 OSにエラーが発生しました")

def main():
    log_entry()

if __name__ == "__main__":
    main()