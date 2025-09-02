count = 0
while count <3:
    count += 1
    print(f"ひつじが{count}匹")
print("おやすみなさい")

count = 1
while count <5:
    count += 1
    print(f"よつばが{count}かわいい")
print("よつばちゃん激カワすぎる")

count = 1
while count <5:
    count += 1
    kawaii_level = "★" * count
    print(f"よつばが{count}かわいい {kawaii_level}")

count = 1
while count <7:
    count += 1
    gekikawa_Heart ="❤️" * count
    print(f"よつばちゃんの可愛さは{count}並、{gekikawa_Heart}")
    print("よつばちゃん激カワすぎる")

count = 3
while count <10:
    count += 1
    gekikawa_level = "💖" * count
    print(f"よつばの可愛さは{count}クラス　{gekikawa_level}")

name = "よつば"
index = 0
while index < len(name):
    char = name[index]
    hearts = "💖" * (index + 1)
    print(f"{char}ちゃん{hearts}")
    index += 1
