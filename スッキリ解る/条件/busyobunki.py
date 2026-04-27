from difflib import get_close_matches #defflibライブラリからget_close_matchesモジュールをインポートする
from pathlib import Path #pathlibライブラリからpatchモジュールをインポートする
from datetime import datetime #datemeモジュールからdatetimeクラスをインポートする
import csv

DEPT_MASTER = { #部署一覧のマスタ部分
    "jimuijika" : "医療事務",
    "sougousoudan" : "総合相談センター",
    "kango1ns" : "一病棟看護",
    "kango2ns" : "二病棟看護",
    "kango3ns" : "三病棟看護",

}

VALID_DEPT_IDS = set(DEPT_MASTER.keys()) #部署マスタのキーをsetでVALID_DEPT_IDSに代入する

LOG_PATH = Path(__file__).with_name("dept_chek_log.csv") #このPythonファイルのパスをPathクラスに変換しpathlibで扱いやすいpathオブジェクトに変化させてファイル名をdept_chek_log.csvに変化させる
LOG_FIELDS = [
    "timestamp",
    "input_raw",
    "input_norm",
    "initial_result",
    "choice",
    "corrected_raw",
    "corrected_norm",
    "final_result",
    "note",

] #このセクションはCSVファイルの各項目を設定するせくしょんである。

def now_str()->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def append_log(row:dict)->None:
    """CSVに1行追加する(ファイルがなければヘッダも書く)"""
    file_exists = LOG_PATH.exists()
    with LOG_PATH.open("a",newline="", encoding="utf-8-sing")as f:
        writer = csv.DictWriter(f,fieldnames=LOG_FIELDS)
        if not file_exists:
            writer.writerheader()
        writer.writerow(row)
        

def normalize_dept_id(raw:str)->str: #ここは型ヒントであり、実際に文字情報に変化させているわけでは無い。
    return raw.strip().lower()  #ユーザーの生入力データを受け取り、.strip()で前後の空白を削除し、.lower()で大文字を全て小文字に変換し正規化する。

def show_help() ->None:
    print("\n入力向け確認手順")
    print("部署配布フォルダ当で確認してください。")
    print("-ざっくり手順：①一覧確認 → ②正しい番号入力 → ③再チェック → ④送信\n")

def show_vaild_depts() ->None: #型ヒント。->Noneは戻り値が存在しないということ。
    print("登録済み部署番号（参考):") #登録済み部署番号を表示するよという見出し。ユーザーに表示される。
    for code,name in sorted(DEPT_MASTER.items()): #Sortedで並び替えた部署コードを一つずつ取り出ていく。{code}に部署コードがはいり、{nama}に部署ナンバーが入る。
        print(f"{code}-{name}") #{code}に部署コードが入り、{name}に部署名が入る。
    print() #空白行を差し込む用途。


def suggest_sumilar(dept_id:str)->None:
    candidates = get_close_matches(dept_id,VALID_DEPT_IDS,n=3,cutoff=0.6) #get_close_matchesを使い、dept_idとVALID_DEPT_IDSを比較し、類似度が0.6以上の候補を三つ選び、その結果をcandidatesに代入する。
    if candidates:
        print("もしかして：") #canddidatesが空でなければもしかしてとして以下の処理を実行する
        for c in candidates: #candiatesに入っている候補を一つずつ取り出す。
            print(f"-{c}: {DEPT_MASTER[c]}") #候補の部署コードとそれに対応する部署名を表示させる。
        print()


def prompt_dept_id()-> tuple[str,str]:
    while True:
        raw = input("部署コードを入力してください。>")
        dept_id = normalize_dept_id(raw)
        if dept_id:
            return raw,dept_id
        print("エラーです。もう一度入力してください。")
        

def supervisor_decision()->str:
    print("\n上司に確認：どうしますか？")
    print("1)こちらで修正入力する")
    print("2)差し戻す（再提出を依頼する）")
    print("3)登録済み部署一覧を表示する")
    print("0)中止する。")


    while True:
        choice = input("選択する番号を入力してください >>").strip()
        if choice in {"1", "2", "3", "0"}:
            return choice
        print("エラー：1/2/3/0のいずれかを入力してください")

def main()->None:
    print("==部署番号チェックツール==")
    print("目的：部署番号が正しいか確認し、誤りなら上司判断(修正、差し戻し)を行う\n")

    input_raw,dept_id = prompt_dept_id() #上で定義しておいたprompt_dept_idを実行し、その戻り値をinput_rawとdept_idに代入する。
    ts = now_str() #ここで上で定義しておいたnow_strを実行し、帰ってきた現在日時を文字情報にしたものをtsに代入する。

#ここで共通ログの土台を作る。
    base_log = {
    "timestamp": ts,
        "input_raw": input_raw,
        "input_norm": dept_id,
        "initial_result": "",
        "choice": "",
        "corrected_raw": "",
        "corrected_norm": "",
        "final_result": "",
        "note": "",
} #ここまでのセクションはCSVの基本情報となる。


#正常系
    if dept_id in DEPT_MASTER:
        print(f"\n ok {dept_id}:{DEPT_MASTER[dept_id]}")
        print(f"処理を始めます。（デモ。ここで終了)\n")

        append_log(base_log |{
        "initial_result": "ok",
        "final_result" : "ok",

        })
        return


    #異常系

    print (f"\n NG:{dept_id}は登録されていません。")
    suggest_sumilar(dept_id)

    while True:
        choice = supervisor_decision()

        if choice == "0":
            print("\n 中止しました。\n")
            append_log(base_log | {
                "initial_result": "NG",
                "choice": "0",
                "final_result" : "Cansell",
            })

            return

        if choice == "3":
            show_vaild_depts()
            continue

        if choice == "2":
            print("\n記入者に内容を差し戻します。その際には誤りの内容を伝えるのを忘れないでください。\n")
            show_help()
            append_log(base_log | {
                "initial_result" : "NG",
                "choice" : "2",
                "final_result" : "RETERN",

            })
            return
        
        if choice == "1":
            corrected_raw , corrected = prompt_dept_id()
            
            if corrected in DEPT_MASTER:
                print(f"\n 修正しました：{corrected}({DEPT_MASTER[corrected]})")
                show_help()
                append_log(base_log | {
                    "initial_result" : "NG",
                    "choice" : "1",
                    "corrected_raw": corrected_raw,
                    "corrected_norm": corrected,
                    "final_result" : "FIXED_OK",
                    
                })
                return
            print(f"\n{corrected} も未登録です。再度上司判断に戻ります。")
            suggest_sumilar(corrected)
        
if __name__ =="__main__" :
    main()
    


            
        
    




    







    
