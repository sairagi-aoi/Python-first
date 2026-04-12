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
    "imput_norm",
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
    """CSVに1行追加する（ファイルがなければヘッダも書く)"""
    file_exists = LOG_PATH.exists()
    with LOG_PATH.open("a",newline="", encoding="utf-8-sing")as f:
        writer = csv.DictWriter(f,fieldnames=LOG_FIELDS)
        if not file_exists:
            writer.writerheader()
        writer.writerow(row)
        

