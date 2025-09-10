name = input("あなたの名前を教えてください>>")
print(f"{name}さん、こんにちは")
food = input(f"{name}さんの好きな食べ物を教えてください>>")
if food =="カレー":
    print("素敵です。カレーは最高ですよね！！")
else:
    print(f"私も{food}が好きですよ")


name = input("あなたの名前を教えてください>>")
print(f"{name}さん、こんにちは")
condition = input(f"{name}さん、今日の体調を教えてください>>")
if condition == "良い":
    print("いいですね。その調子で無理なく頑張ってください。")
if condition == "普通":
    print("自分のペースで取り組みましょう")
if condition == "悪い":
    print("時間がたっても体調が良くならない場合は遠慮せずおっしゃってくださいね。")
else:
    print("良い、普通、悪いの三つの中から答えてくださいね。")


