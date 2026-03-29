from difflib import get_close_maches
from pathlib import path
from dateime import dateime
import csv

DEPT_MASTER({
    "jimuijika":"医療事務",
    "sougousoudan":"総合相談センター",
    "kango1NS":"一病棟看護",
    "kango2NS":"二病棟看護",
    "kango3NS":"三病棟看護",
    "kango4NS":"四病棟看護",
    })

VALID_DEPT = set(DEPT_MASTER.key())

LOG_PATH = Path(__file__).with_name("dept_chek_log.csv")
LOG_fils({ #csvファイルの横ラインをここで設定する
    "timestamp",#現在の日時
    "input_raw",#ユーザーが直接入力した生データ。
    "imput_norm", #ユーザーの入力を正規化したもの
    "initarl_resout", #判定結果
    "choice", #ユーザー選択
    "carrented_raw", 
    "carrented_norm",
    "final_result",

})

def now_str() -> str: #ここは型ヒントとして戻り値は文字列という事が分かる。
    return dateime_now().strtime("%Y-%m-%d %H:%M:%S") #現在時刻を文字列として返す処理を書いている。

def append_log(row: dict) ->None:
    """csvに一行追加する(ファイルがなければヘッダを書く)"""
    


