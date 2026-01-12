from difflib import get_close_matches #difflibモジュールからget_close_matches関数をインポートする

#　部署マスタ（コード -> 部署名）
DEPT_MASTER = {
    "jimuijika":"事務(医事課)",
    "soudansentta":"相談センター",
    "kango1ns":"看護1NS",
    "kango2ns":"看護2NS",
    "kaigo1ns":"介護1NS",
    } #ユーザー側に表示される部署名の辞書

VALID_DEPT_IDS = set(DEPT_MASTER.keys()) #辞書の左側のキーをセットにしてDEP_MASTERに代入する

def normalize_dept_id(raw:str) ->str:#入力を受け取って部署コードに変形する
    """入力揺れ（前後空白・大文字小文字・類似語）を吸収して部署コードにする"""
    return raw.strip().lower() #前後の空白を削除し大文字を小文字に変換して返す

def show_help() -> None:
    print("" \
    "入力者向け確認手段:")
    print()


