from asyncio import CancelledError
from difflib import get_close_matches
from os import name
from random import choice


DEPT_MASTER ={
    "jimuijika":"医療事務",
    "soudansentar":"相談センター",
    "kango1ns":"一病棟看護",
    "kango2ns":"二病棟看護",
    "kango3ns":"三秒等看護",
    }

VALID_DEPT_IDS = set(DEPT_MASTER.keys()) #部署一覧の辞書からキーを取り出し、それをセットとしてまとめ、その内容をVALID_Dept_idsに代入する


def normalization_dept_id( raw:str) ->str:
    """入力揺れ（大文字小文字、空白など）を吸収して部署コードにする"""
    return raw.strip().lower() 

def show_help() ->None:
    print("\n入力者向け確認手段"),
    print("部署資料配布フォルダ等で確認してください")
    print("-ざっくり手順：1-一覧確認 → 2-正しい番号入力 → 3-再チェック → 4-送信\n") #ユーザーの入力がマスタ辞書になかったときに現れる内容

def show_vaild_deps() -> None:
    print("\n 登録済み部署番号(参考)：")
    for code, name in sorted(DEPT_MASTER.item()):
        print(f"-{code};{name}")

def suggest_sumilar(dept_id:str) -> None:
    """入力ミスっぽい時に似た候補を表示する"""
    candidates = get_close_matches(dept_id,VALID_DEPT_IDS,n=3,cutoff=0.6)
    if candidates:
        print("もしかして：")
        for C in candidates:
            print(f"-{C}:{DEPT_MASTER[C]}")
        print()

def prompt_dept_id() ->str:
    while True:
        raw = input("部署番号を入力してください >")
        dept_id = normalization_dept_id(raw)
        if dept_id:
            return dept_id
        print("[エラー]未入力です。もう一度入力してください")

def supervisor_decision() -> str:
    """上司判断：1=こちらで修正入力 / 2=差し戻し / 3=一覧表示 / 0=中止"""
    print("\n 上司に確認：どうしますか？")
    print("1)こちらで修正入力をする")
    print("2)差し戻す。その際には間違い箇所の説明もする")
    print("3)リストの部署一覧を表示する")
    print("0)部署の照会作業を中止する")
    while True:
        choice = input("選択する番号を入力してください >").strip()
        if choice in {"1","2","3","0"}:
            return choice 
    print("[エラー]1/2/3/0 のいずれかからお選びください")

def main() -> None:
    print("===部署番号チェックツール===")
    print("目的、部署番号が正しいか確認し、誤りなら上司判断（修正、差し戻し）を行う\n")

    dept_id = prompt_dept_id()

    #正常系
    if dept_id in VALID_DEPT_IDS:
        print(f"\n ok:{dept_id}{DEPT_MASTER[dept_id]}")
        print("処理を進めます。")
        print("\nフロー：①部署番号入力 → ②マスタ照合OK → ③処理継続\n")
        return
    
    #異常系
    print(f"\n NG:{dept_id}は登録されていません。")
    suggest_sumilar(dept_id)

    while True:
        choice = supervisor_decision()

        if choice == "0":
            print("\n中止しました。")
            return
        
        if choice == "3":
            print("\n リストの部署一覧を表示する")
            return
        
        if choice == "2":
            print("\n入力者に返却します。部署番号を確認して再提出してください")
            show_help()
            print("フロー：①部署番号入力 → ②マスタ照合NG → ③上司判断=修正 → ④修正値でOK → ⑤処理継続\n")
            return
        
        if choice == "1":
            corrected = prompt_dept_id()
            if corrected in VALID_DEPT_IDS:
                print(f"\n修正しました : {corrected}{DEPT_MASTER[corrected]}")
                show_help()
                print("フロー：①部署番号入力 → ②マスタ照合NG → ③上司判断=修正 → ④修正値でOK → ⑤処理継続\n")
                return
            
            else:
                print(f"\n{corrected}も未登録です。再度上司判断に戻ります。")
                suggest_sumilar(corrected)


if __name__ =="__main__":
    main()








        
    














        


    
