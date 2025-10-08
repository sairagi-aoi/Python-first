from datetime import datetime
from sqlite3.dbapi2 import Timestamp #現在の日付を習得する

TEXT_FILE = "health_cat_log.txt" #テキストファイルを作成
OWNER_SCALE ={"最悪":-2,"悪い":-1,"普通":0,"良い":1,"絶好調":2} #飼い主の体調スケール
CAT_SCALE = {"ぐったり":-2,"元気ない":-1,"普通":0,"元気":1,"走り回ってる":2} #飼い猫の体調スケール

def log_entry(): #変数ログエントリーをdefで作成
    OWNER_condition_choices = "(最悪\悪い\普通\良い\絶好調)" #飼い主の体調選択肢
    cat_condition_choices = "(ぐったり\元気ない\普通\元気\走り回ってる)" #飼い猫の体調選択肢

    while True: #ループの始まり
        owner = input("あなたの名前を教えて下さい: ").strip() #ユーザーの名前を尋ねる
        cat = input("飼い猫の名前教えて下さい: ").strip() #ユーザーの飼い猫の名前を尋ねる
        owner_condition = input(f"あなたの体調を教えて下さい{OWNER_condition_choices} >>").strip() #ユーザーの体調を選択肢の中から尋ねる
        cat_condition = input(f"飼い猫の体調を教えて下さい{cat_condition_choices} >>").strip() #ユーザーの飼い猫の体調を選択肢の中から尋ねる

        #　入力が正しいか確認する（選択肢にない入力はやり直し）
        if owner_condition not in OWNER_SCALE or cat_condition not in CAT_SCALE:
            print("提示されている選択肢の中からお選びください")
            continue

        #　追加質問が必要な場合
        if owner_condition in ("最悪","悪い") and cat_condition in ("ぐったり","元気ない"): #これらの入力の際にのみテキストファイルへの記入が必要になる
            condition_type = input("その体調不良は精神面と身体面のどちらですか？それとも両方ですか？（精神面/身体面/両方) >>").strip() #ユーザーの体調不良の種類を尋ねる
            condition_since = input("その体調不良はいつ頃から発生していますか？ >> ").strip() #ユーザーの体調不良の発生時期を尋ねる
            condition_cause = input("その体調不良の原因として思い当たる事はありますか？ (無い場合は「無し」と入力して下さい) >>").strip() #ユーザーの体調不良の発生原因を尋ねる
            condition_yousu = input("現在の飼い猫さんの様子はいつ頃から続いていますか？ >>").strip() #ユーザーの飼い猫の様子を尋ねる
            condition_eating = input("飼い猫さんの食欲はありますか？ >> ").strip() #ユーザーの飼い猫の食欲を尋ねる
            condition_play = input("飼い猫さんは遊んでいますか？ >> ").strip() #ユーザーに飼い猫の遊びの様子を尋ねる
            condition_drink = input("飼い猫さんは水を飲んでいますか？ >> ").strip() #ユーザーに飼い猫の水のみ事情を尋ねる
            condition_toilet = input("飼い猫さんのトイレの様子はどうですか? >>").strip() #ユーザーに飼い猫さんのトイレの様子を尋ねる
        else:
            print("いいですね！ その調子で過ごしましょう！")
            #未質問の項目はだっしゅで埋める
            condition_type =condition_since = condition_cause = "="
            condition_yousu = condition_eating = condition_play = condition_drink = condition_toilet = "="

        break #ここでループ終了

    Timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") #現在の日時を取得して指定された形式に変換する
    









