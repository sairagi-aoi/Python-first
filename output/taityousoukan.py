from datetime import datetime

TEXT_FILE = "health_cat_log.txt"
OWNER_SCALE = {"最悪": -2, "悪い": -1, "普通": 0, "良い": 1, "絶好調": 2}
CAT_SCALE = {"ぐったり": -2, "元気ない": -1, "普通": 0, "元気": 1, "走り回ってる": 2}

def log_entry():
    owner = input("あなたの名前を教えてください: ").strip()
    cat = input("飼い猫の名前教えてください: ").strip()

    while True:
        OWNER_condition = input("あなたの体調を教えてください >> ").strip()

        if OWNER_condition in ("最悪","悪い"):
            condition_type = input("その体調不良は精神面と身体面のどちらですか？それとも両方ですか？（精神面/身体面/両方) >>").strip()
            condition_since = input("その体調不良はいつ頃から発生していますか？ >> ").strip()
            condition_cause = input("その体調不良の原因として思い当たることはありますか？（無い場合は「無し」と入力して下さい) >> ").strip()
            break
        elif OWNER_condition in ("普通","良い","絶好調"):
             print("良いですね！ その調子で無理なく楽しんでお過ごし下さい。")
        else:
             print("提示されている選択肢の中からお選びください")
    
    while True:
        CAT_condition = input("飼い猫の様子を教えて下さい >> ").strip()

        if CAT_condition in ("ぐったり" ,"元気ない"):
            condition_yousu = input("現在の飼い猫の様子はいつごろから続いていますか？ >>").strip()
            condition_eating = input("飼い猫さんの食欲はありますか？ >>").strip()
            condition_play = input("飼い猫さんは遊んでいますか? >>").strip()
            condition_drink = input("飼い猫さんは水を飲んでいますか？ >>").strip()
            condition_toilet = input("飼い猫さんのトイレの様子はどうですか？ >>").strip()
            break
        elif CAT_condition in ("普通","元気","走り回ってる"):
            print("いいですね！ 飼い猫さんがその調子を維持できるようにサポートを続けてあげて下さいね。")

    else:
        print("提示されている選択肢の中からお選びください")
    
# 現在時刻を取得
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    #出力形式を組み立て
    record = (
        f"=== 飼い猫と飼い主の健康状態相関調査ログ ({timestamp}) ===\n"
        f"飼い主の名前: {owner}\n"
        f"飼い主の体調: {OWNER_condition}\n"
        f"体調不良の種類: {condition_type}\n"
        f"発生時期: {condition_since}\n"
        f"原因: {condition_cause}\n"

        f"飼い猫の体調: {CAT_condition}\n"
        f"現在の飼い猫の様子{condition_yousu}\n"
        f"飼い猫の食欲"{condhition_eating}\n"
        
        



    )

