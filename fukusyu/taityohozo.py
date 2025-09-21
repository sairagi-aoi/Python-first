import datetime

department = input("あなたの部署名を教えてください>>")
print(f"おはようございます。{department}所属なのですね")

while True:
    problem = input(f"あなたの部署である{department}では、何か問題がありますか？>>")
    if problem =="有る":
        problem_type = input("それはどの様な問題ですか？人間関係、業務内容、その他、これらのどれに該当しますか？ >>")
        problem_since = input("その問題はいつから発生していますか？ >>")
        problem_impact = input("その問題はあなたにどの様な影響を与えていますか？ >>")
        problem_action = input("その問題を解決するために、あなたはどの様な行動をとりましたか？ >>")

        #現在時刻を取得
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        #出力内容を組み立て
        record = (
            f" === 相談記録 ({timestamp}) ===\n"
            f"部署 : {department}\n"
            f"問題の有無 : 有る\n" #有る場合にしかこの出力はされないから有るだけで良いんだ
            f"問題の種類 : {problem_type}\n
            f"発生時期: {problem_since}\n"
            f"影響 : {problem_impact}\n"
            f"取った行動 : {problem_action}\n"
            + "-" * 40 + "\n\n"   
        )

        #テキストファイルに保存
        try:
            with open("相談記録.txt" , "a", encoding="utf-8") as f:
                f.write(record)
            print("記録を保存しました。後ほど印刷していただけます。")
        except PermissionError:
            print("保存に失敗しました:ファイルへのアクセス権限がありません。別の場所に保存するか、管理者に連絡してください。")
        except FileNotFoundError:
            print("保存に失敗しました : 保存先フォルダが見つかりません。パスを確認してください。")
        except OSError as e:
            print(f"保存に失敗しました(OSエラー) : {e}")

        break
    elif problem in ("無し","ない"):
        print("それはよかったです。今後もし何かありましたら遠慮なく産業医までお知らせください。")
        break
    else:
        print("「有る（ある）」か「無し」でお答えください。")
        

