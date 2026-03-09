from difflib import get_close_matches
from pathlib import Path
from datetime import datetime
import csv

DEPT_MASTER = {
    "jimuijika": "医療事務",
    "soudansentar":"相談センター",
    "kango1ns": "一病棟看護",
    "kango2ns": "二病棟看護",
    "kango3ns": "三秒等看護",   
}

VALD_DEPT_id = set(DEPT_MASTER.keys()) #部署マスタからキーを取り出してsetを作り、その内容をVALD_DEP_idに代入する

LOG_Path = Path(__file__).with_name("dept_chek_log.csv") #ログ保存用のCSVファイルを作成する
LOG_FIELDS = [
    "timestamp",
    "input_raw",
    "input_norm",
    "initail_result", #ok/NG
    "choice",          
    "corrected_raw",
    "corrected_norm",
    "final_result",
    "note",
] #ここまではCSVファイルにどのように内容を入力するのかを決めるセクション

def not_str() ->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")





