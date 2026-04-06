from difflib import get_close_matches #defflibライブラリからget_close_matchesモジュールをインポートする
from pathlib import path #pathlibライブラリからpatchモジュールをインポートする
from datetime import datetime #datemeモジュールからdatetimeクラスをインポートする
import csv

DEPT_MASTER = {
    "jimuijika" : "医療事務",
    "sougousoudan" : "総合相談センター",
    "kango1ns" : "一病棟看護",
    "kango2ns" : "二病棟看護",
    "kango3ns" : "三病棟看護",

}

VALID_DEPT_IDS = set(DEPT_MASTER.keys()) #部署マスタのキーをsetでVALID_DEPT_IDSに代入する



