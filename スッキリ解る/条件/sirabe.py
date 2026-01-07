
#さらに書き換えた構文
# 1.正しい部署受付番号のリスト（マスターデータ）
#　元のコードのscoreに該当する
valid_dept_ids = ['jimu02','soudan01','kango04','kaigo03']

# 2.チェック対象の入力された番号
# 元のコードの'100'　（チェックする値）に当たる
input_dept_id = input('確認したい部署ナンバーを入力してください')

print(f'入力された部署番号{input_dept_id}') #確認用に表示
print(' ---判定開始---')

# 3.番号が正しいリストにふくまれているのか確認
if input_dept_id in valid_dept_ids:
    print(f'部署番号{input_dept_id}が確認できました。処理を進めます。')

else:
    print('[エラー]番号が正しくないか、入力されt')


    