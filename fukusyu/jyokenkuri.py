is_awake = True
count = 0
while is_awake == True:
    count += 1
    print(f"ひつじが{count}匹")
    key = input("もう眠りそうですか？(y/n) >>")
    if key == "y":
        is_awake = False
print("おやすみなさい")

is_otituki = False
count = 0
while is_otituki == False:
    count += 1
    print(f"深呼吸してみましょう。{count}回目")
    key = input("落ち着きいてきましたか？(y/n) >>")
    if key == "y":
        is_otituki = True
print("おつかれ様でした。この後は無理なくゆっくり過ごしてくださいね。")


is_calm = False #落ち着きを英語で書き直し
count = 0
MAX_ROUNDS = 10

YES = {"y","yes","y","はい"}
NO = {"n","no","n","いいえ"} #条件の色々な入力パターン

try:
    while not is_calm:
        if count >= MAX_ROUNDS:#カウントがMax_round以上だったらTrueになる
            print("今日はここまで。水を飲む・横になる・ゆっくり深呼吸を続けるなど、無理せず休みましょう。")
            break

    print(f"深呼吸してみましょう。{count +1}回目")
    ans =input("落ち着いてきましたか？(y/n) >>").strip().lower()

    if ans in YES:
        is_calm = True
    elif ans in NO:
        count += 1
    else:
        print("yかnで答えてください。")
except KeyboardInterrupt:
   print("\n中断しました。おつかれさまでした。この後は無理なくゆっくり過ごしてくださいね。")
else:
    if is_calm:
        print("おつかれ様でした。この後は無理なくゆっくり過ごしてくださいね。")







