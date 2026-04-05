from difflib import get_close_matches
from pathlib import Path
from datetime import datetime
import csv

# 次の改変候補メモ:
# 1) 変数名・関数名・表示文のタイポ修正（VALD_DEPT_id / LOG_Path / sugest_similar など）
# 2) `check_dept_id()` のような判定関数を作って、入出力と業務ロジックを分離する
# 3) 追加・修正・差し戻し件数を集計する簡易レポート機能を追加する
# 4) 部署マスタを辞書直書きではなく CSV から読み込むように変更する
# 5) 修正入力時に候補を番号選択で選べるようにして再入力負荷を下げる
# 6) ログ記録処理を共通化して、OK/NG/RETURN/CANCEL の分岐ごとの重複を減らす
# 7) 例外処理やファイルエラーハンドリングを追加して、CSV 書き込み失敗時の原因を分かりやすくする
# 8) `unittest` で正規化・候補表示・分岐判定のテストを追加する
#

DEPT_MASTER = {
    "jimuijika": "医療事務",
    "soudansentar":"相談センター",
    "kango1ns": "一病棟看護",
    "kango2ns": "二病棟看護",
    "kango3ns": "三病棟看護",   
}

VALD_DEPT_IDS = set(DEPT_MASTER.keys()) #部署マスタからキーを取り出してsetを作り、その内容をVALD_DEP_idに代入する

LOG_Path = Path(__file__).with_name("dept_chek_log.csv") #ログ保存用のCSVファイルを作成する
LOG_FIELDS = [
    "timestamp",
    "input_raw",
    "input_norm",
    "initial_result", #ok/NG
    "choice",          
    "corrected_raw",
    "corrected_norm",
    "final_result",
    "note",
] #ここまではCSVファイルにどのように内容を入力するのかを決めるセクション

def not_str() ->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def append_log(row: dict) ->None:
    """csvに一行追加する (ファイルがなければヘッダを開く)"""
    file_extstis = LOG_Path.exists()
    with LOG_Path.open ("a",newline="", encoding= "utf-8-sig" ) as f:
        writer = csv.DictWriter(f, fieldnames= LOG_FIELDS)
        if not file_extstis:
            writer.writeheader()
        writer.writerow(row) #CSVに１行追記する処理ですよ

def normalaization_dept_id(raw:str)->str:
    """入力揺れを吸収して部署コードに変換する"""
    return raw.strip().lower()

def show_help() -> None:
    print("\入力者向け確認手段")
    print("部署配布フォルダ等で確認してください")
    print("- ざっくり手順：①一覧確認 → ②正しい番号入力 → ③再チェック → ④送信\n")

def show_vaild_depts() ->None:
    print("\登録済み部署番号(参考)：")
    for code,name in sorted(DEPT_MASTER.items()): #部署マスタの中からコードと部署名を取り出し、一覧としてユーザー側に表示させる
        print(f"-{code}:{name}")
    print()

def sugest_similar(dept_id : str) ->None:
    """入力ミスの疑いがある場合に似た候補を表示する"""
    candidates = get_close_matches(dept_id,VALD_DEPT_IDS, n=3 ,cutoff=0.6) #ユーザーの入力に0.6以上の類似性がある項目だけを３件返す
    if candidates: #candidatesが空でなければ
        print("もしかして")
        for c in candidates: 
            print(f"-{c}:{DEPT_MASTER[c]}") #candidatesから候補コードを一件づつ取り出して表示する
        print()



def prompt_dept_id() -> tuple[str,str]:
    """(生入力正規化後）を返す"""
    while True:
        raw = input("部署コードを入力してください＞") #ユーザー入力の生データをそのままrawに代入する。この場面ではまだ表記揺れが残っている
        dept_id = normalaization_dept_id(raw) #ユーザーのなま入力を整えてdept_idに代入する
        if dept_id:
            return raw,dept_id #rawと整えられたnユーザー入力の二つを返す
        print("[エラー]未入力です。もう一度入力してください")

def supervisor_decision() ->str:
    """上司判断 : 1=こちらで修正入力 / 2=差し戻し / 3=一覧表示 / 0=中止 """
    print("\上司に確認 : どうしますか？")
    print("1こちらで修正作業を行う")
    print("2)差し戻す（再提出を依頼する)")
    print("3)登録済み部署一覧を表示する")
    print("0)中止する")


    while True:
       choice = input("選択する番号を入力してください >").strip()
       if choice in {"1","2","3","0"}:
           return choice
       print("エラー 1/2/3/0のいずれかで入力してください")

def main()->None:
    print("===部署番号チェックツール===")
    print("目的 : 部署番号が正しいか確認し、誤りなら上司判断(修正・差し戻し)を行う\n")

    input_raw,dept_id = prompt_dept_id()
    ts = not_str()

    #正常系
    if dept_id in DEPT_MASTER:
        print(f"\n ok {dept_id}:{DEPT_MASTER[dept_id]}")
        print("処理を始めます。（デモ：ここで終了)\n")

        append_log({
            "timestamp" : ts,
            "input_raw" :input_raw,
            "input_norm":dept_id,
            "initial_result":"OK",
            "choice":"",
            "corrected_norm": "",
            "final_result":"OK",
            "note":"",

        })
        return
    
    #異常系
    print(f"\nNG: {dept_id}は登録されていません")

    while True:
        choice = supervisor_decision()

        if choice =="0":
            print("\n中止しました\n")
            append_log({
                "timestamp":ts,
                "input_raw":input_raw,
                "input_norm":"dept_id",
                "initial_result":"NG",
                "choice" : "0",
                "corrected_raw" : "",
                "corrected_norm":"",
                "final_result":"CANCEL",
                "note": "",   
            })
            return
        
        if choice == "3":
            show_vaild_depts()
            continue

        if choice =="2":
            print("\n記入者に差し戻します。その際には間違いについての説明を記入者へ忘れず行ってください。\n")
            show_help()
            append_log({
                "timestamp":ts,
                "input_raw":input_raw,
                "input_norm":dept_id,
                "initial_result":"NG",
                "choice":"2",
                "corrected_raw":"",
                "corrected_norm":"",
                "final_result":"RETURN",
                "note":"",

            })
            return
        

        if choice =="1":
            corrected_raw, corrected = prompt_dept_id()
            if corrected in DEPT_MASTER:
                print(f"\n修正しました：{corrected} ({DEPT_MASTER[corrected]})")
                show_help()
                append_log({
                    "timestamp":ts,
                    "input_raw":input_raw,
                    "input_norm" : dept_id,
                    "initial_result": "NG",
                    "choice": "1",
                    "corrected_raw": corrected_raw,
                    "corrected_norm": corrected,
                    "final_result": "FIXED_OK",
                    "note":"",

                })
                return
            
            print(f"\n{corrected}も未登録です。再度上司判断に戻ります。") #修正入力後のデータも部署マスタに該当しない場合にこのエラー分が出力される
            sugest_similar(corrected)

            
if __name__ == "__main__":
    main()

            



        


            

