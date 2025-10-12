from datetime import datetime

TEXT_FILE = "health_cat_log.txt" #テキストファイルを作成
OWNER_SCALE ={"最悪":-2,"悪い":-1,"普通":0,"良い":1,"絶好調":2} #飼い主の体調スケール
CAT_SCALE = {"ぐったり":-2,"元気ない":-1,"普通":0,"元気":1,"走り回ってる":2} #飼い猫の体調スケール

def log_entry(): #変数ログエントリーをdefで作成
    owner_condition_choices = "(最悪/悪い/普通/良い/絶好調)"
    cat_condition_choices = "(ぐったり/元気ない/普通/元気/走り回ってる)"

    while True: #ループの始まり
        owner = input("あなたの名前を教えて下さい: ").strip() #ユーザーの名前を尋ねる
        cat = input("飼い猫の名前教えて下さい: ").strip() #ユーザーの飼い猫の名前を尋ねる
        owner_condition = input(f"あなたの体調を教えて下さい{owner_condition_choices} >>").strip()
        cat_condition = input(f"飼い猫の体調を教えて下さい{cat_condition_choices} >>").strip()

        #　入力が正しいか確認する（選択肢にない入力はやり直し）
        if owner_condition not in OWNER_SCALE or cat_condition not in CAT_SCALE:
            print("提示されている選択肢の中からお選びください")
            continue

        #　追加質問が必要な場合
        if (owner_condition in ("最悪","悪い") and 
            cat_condition in ("ぐったり","元気ない")):
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
            # 詳細情報が不要な場合は初期値を設定
            condition_type = condition_since = condition_cause = "="
            condition_yousu = condition_eating = condition_play = condition_drink = condition_toilet = "="

        break #ここでループ終了

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    #出力
    record = (
        f" === 飼い猫と飼い主の健康状態相関調査ログ ({timestamp}) ===\n"
        f"飼い主の名前: {owner}\n" #飼い主の名前を記入して改行
        f"飼い主の体調: {owner_condition} (スコア: {OWNER_SCALE[owner_condition]})\n" #飼い主の体調を記入して改行
        f"飼い猫の名前: {cat}\n"#飼い猫の名前を記入して改行
        f"飼い猫の体調: {cat_condition} (スコア: {CAT_SCALE[cat_condition]})\n" #飼い猫の体調とスコアを記入して改行
        f"体調不良の種類: {condition_type}\n"
        f"発生時期: {condition_since}\n"
        f"原因: {condition_cause}\n"
        f"現在の飼い猫の様子: {condition_yousu}\n"
        f"飼い猫の食欲: {condition_eating}\n"
        f"飼い猫の遊び: {condition_play}\n"
        f"飼い猫の水分接種: {condition_drink}\n"
        f"飼い猫のトイレの様子: {condition_toilet}\n"
        )

    #テキストファイルに保存
    try:
        with open(TEXT_FILE, "a", encoding="utf-8") as f: #テキストファイルを書き込みモードで開き、内容はutf-8で書き込む
            f.write(record)
        print("回答が正常に保存されました。後ほど印刷していただけます。")
    except PermissionError:
        print("保存に失敗しました。ファイルへのアクセス権限がありません。") #ファイルへのアクセス権限が無い場合に出るエラー
    except FileNotFoundError:
        print("保存に失敗しました。指定されたファイルが見つかりません。") #指定されたファイルが見つからないエラーが発生。
    except OSError as e:
        print(f"保存に失敗しました。OSにエラーが発生しました： {e}") 

if __name__ == "__main__": #__name__はマジック変数
    log_entry()
    



