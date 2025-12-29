#以下テキスト例文（P124)
name = input(' あなたの名前を教えて下さい >>')
print(f'{name}さん、こんにちは')
food = input(f'{name}さんの好きな食べ物について教えて下さい >>')
if food == 'カレー':
    print('素敵です。カレーは最高ですよね!!')
else:
    print(f'私も{food}が好きですよ')


#　以下自分での書き換え
country = input('あなたの出身地を教えてください >>')
print(f'{country}からいらっしゃったんですね。')
place = input(f'{country}の最も有名な場所を教えて下さい >>')
if place == 'ニューヨーク':
    print('やば、めっちゃ有名じゃん')
elif place == 'ロサンゼルス':
    print('あーしもめっちゃ行きたいんですけど')
else:
    print(f'え？ どこそれ？ 知らんし')

breakfast = input('あなたはいつもどんな朝食を食べますか？')
print