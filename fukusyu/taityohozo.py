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

        #テキストファイルに保存
        while open("相談記録.txt","a",encoding="utf-8") as file:
            file.write(f"=== 相談記録 ({timestamp}) ===\n")
            file.write(f"部署: {department}\n")
            file.write(f"問題の有無: {problem}\n")
            file.write(f"問題の種類: {problem_type}\n")
            file.write(f"発生時期: {problem_since}\n")
            file.write(f"影響: {problem_impact}\n")
            file.write(f"取った行動: {problem_action}\n")
            

