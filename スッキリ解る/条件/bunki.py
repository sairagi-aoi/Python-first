from asyncio import CancelledError
from difflib import get_close_matches
from os import name
from random import choice #difflibモジュールからget_close_matches関数をインポートする

#　部署マスタ（コード -> 部署名）
DEPT_MASTER = {
    "jimuijika":"事務(医事課)",
    "soudansentta":"相談センター",
    "kango1ns":"看護1NS",
    "kango2ns":"看護2NS",
    "kaigo1ns":"介護1NS",
    } #ユーザー側に表示される部署名の辞書

VALID_DEPT_IDS = set(DEPT_MASTER.keys()) # 辞書のキー（部署コード）一覧を set にしたもの（in 判定を高速＆意図を明確にする）

def normalize_dept_id(raw: str) -> str:  # 入力（文字列）を前後空白除去＋小文字化して正規化する
    """入力揺れ（前後空白・大文字小文字・類似語）を吸収して部署コードにする"""
    return raw.strip().lower() #前後の空白を削除し大文字を小文字に変換して返す

def show_help() -> None:
    print("\n入力者向け確認手段：")
    print("- 部署番号一覧(社内の部署マスタ / 共有フォルダ / 配布資料)で確認してください。")
    print("-ざっくり手順：1-一覧確認 → 2-正しい番号入力 → 3-再チェック → 4-送信\n") #ユーザーの入力がマスタ辞書になかったときに現れる内容
    
def show_valid_depts() -> None:#ここでは関数を定義しているだけであるから、他の場所でこの関数が呼び出されない限り実行されない
    print("\n登録済み部署番号(参考):")
    for code, name in sorted(DEPT_MASTER.items()):
        print(f"- {code}: {name}")
    print()

def suggest_similar(dept_id: str) -> None: #型ヒント
    """入力ミスっぽい時に近い候補を出す（任意）"""
    candidates = get_close_matches(dept_id, VALID_DEPT_IDS, n=3, cutoff=0.6) # dept_id に似ている候補を VALID_DEPT_IDS から最大3件取得（類似度が cutoff 以上のもの）
    if candidates:
        print("もしかして：")
        for c in candidates:
            print(f"- {c}: {DEPT_MASTER[c]}")
        print()

def prompt_dep_id() -> str:
    while True:
        raw = input("部署番号を入力して下さい > ") #ユーザーの入力をrawに代入する
        dept_id = normalize_dept_id(raw) #空白や表記揺れを吸収して部署番号の形に整える
        if dept_id: # 空文字でなければその値を返して入力ループを終了する
            return dept_id
        print("[エラー]未入力です。もう一度入力してください。")

def supervisor_decision() -> str:
    """上司判断: 1=こちらで修正入力 / 2=突き返し / 3=一覧表示 / 0=中止"""
    print("\n上司に確認：どうしますか？") #ここから
    print(" 1) こちらで修正入力する")
    print(" 2) 入力者に突き返す (再提出依頼)")
    print(" 3) 登録済み一覧を表示する")
    print(" 0) 中止する") #ここまででユーザーに選択肢を表示する
    while True:
        choice = input("選択して下さい (1/2/3/0) > ").strip() #ユーザーの入力を余分な空白を除去し整形した状態でchoiceに代入する
        if choice in {"1","2","3","0"}: #もしこのいずれかの数字が入力されたなら
            return choice #関数は終了
        print("[エラー]1/2/3/0のいずれかで入力して下さい。") #そのいずれでもない場合はこのエラー内容を出力し、入力に戻ることでループを継続する

def main() -> None:
    print("=== 部署番号チェックツール ===")
    print("目的 : 部署番号が正しいか確認し、誤りなら上司判断（修正/突き返し)を行う\n")

    dept_id = prompt_dep_id()

    #正常系
    if dept_id in VALID_DEPT_IDS:
        print(f"\nOk: {dept_id}({DEPT_MASTER[dept_id]})")
        print("処理を進めます。")
        print("\nフロー：①部署番号入力 → ②マスタ照合OK → ③処理継続\n")
        return
    
    #異常系
    print(f"\n NG: {dept_id} は登録されていません。") #ユーザーの入力が部署ナンバーの辞書の中になかった場合にこのエラー表示が出力される
    suggest_similar(dept_id) #ユーザー入力(dept_id)を引数としてsuggest_similarに渡して似ている候補を表示する

    while True:
        choice = supervisor_decision()

        if choice == "0":
            print("\n中止しました。")
            return

        if choice == "3":
            show_valid_depts()
            continue

        if choice == "2":
            print("\n入力者に突き返します:部署番号を確認して再提出して下さい")
            show_help()
            print("フロー：①部署番号入力 → ②マスタ照合NG → ③上司判断=修正 → ④修正値でOK → ⑤処理継続\n")
            return
        
        if choice =="1":
            corrected = prompt_dep_id()
            if corrected in VALID_DEPT_IDS:
                print(f"\n修正しました : {corrected}({DEPT_MASTER[corrected]})")
                show_help()
                print("フロー：①部署番号入力 → ②マスタ照合NG → ③上司判断=修正 → ④修正値でOK → ⑤処理継続\n")
                return
        else:
            print(f"\n[エラー]{corrected} も未登録です。再度上司判断へ戻ります。")
            suggest_similar(corrected)


if __name__ == "__main__":
    main()














    


    
