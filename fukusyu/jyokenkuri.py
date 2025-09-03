is_awake = True
count = 0
while is awake == True:
    count += 1
    print(f"ひつじが{count}匹")
    key = input("もう眠りそうですか？(y/n) >>")
    if key == "y":
        is_awake = False
print("おやすみなさい")
