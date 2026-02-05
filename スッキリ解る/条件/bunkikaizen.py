from asyncio import CancelledError
from curses import raw
from difflib import get_close_matches
from operator import itemgetter
from os import name
from random import choice


DEPT_MASTER ={
    "jimuijika":"医療事務",
    "soudansentar":"相談センター",
    "kango1ns":"一病棟看護",
    "kango2ns":"二病棟看護",
    "kango3ns":"三秒等看護",
    }

VALID_DEPT_IDS = set [str](DEPT_MASTER.keys())

if __name__ == "__main__":
    print("loaded")
    print(VALID_DEPT_IDS)


def normalization_dept_it( dept_id:str) ->str:
    """入力揺れ（大文字小文字、空白など）を吸収して部署コードにする"""
    return raw.strip.lower() 

def show_help() ->None:
    print("\n入力者向け確認手段"),
    print("部署資料配布フォルダ等で確認してください")
    print("-ざっくり手順：1-一覧確認 → 2-正しい番号入力 → 3-再チェック → 4-送信\n") #ユーザーの入力がマスタ辞書になかったときに現れる内容

def show_vaild_deps() -> None:
    print("\n 登録済み部署番号(参考)：")
    for code name in sorted(DEPT_MASTER.item())
    
