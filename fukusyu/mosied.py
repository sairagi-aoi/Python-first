#以下while文での繰り返し
name = input("あなたの名前を教えてください>>")
print(f"{name}さん、こんにちは")

while True: #Trueになるまでループする
    condition = input(f"{name}さん、今日の体調を教えてください>>")

    if condition =="良い":
        print("いいですね。その調子で無理なく頑張ってください。")
        break #ここでループを抜ける
    elif condition =="普通":
        print("自分のペースで取り組みましょう")
        break #ここでループを抜ける
    elif condition == "悪い":
        print("時間がたっても体調が良くならない場合は遠慮せずおっしゃってくださいね。")
        break #ここでループを抜ける
    else:
        print("良い、普通、悪いの三つの中から答えてくださいね。")
        #ループの最初に戻る


