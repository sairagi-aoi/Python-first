from pathlib import Path
import csv
from datetime import datetime

def append_csv(path: str | Path, row: dict, fieldnames: list[str]) -> None:
    """
    csvに１行追加する


    - 新規ファイル（サイズ0)の場合のみ、最初にヘッダ行を書いてから追記
    -Windowsの空行混入対策として newline = ""を必須指定
    - 列順はfieldnames で固定し、欠損キーは "", 余分キーは無視
    """
    p = Path(path) #path文字列から　Pathオブジェクトを作る
    p.parent.mkdir(parents=True, exist_ok=True) #Path　.mkdirの呼び出し　
    is_new = (not p.exists())or (p.stat().st_size == 0)

    with p.open("a", encoding = "utf-8" , newline="") as f:
        w = csv.DictWriter(f , fieldnames = fieldnames)
        if is_new:
            w.writeheader()
        # タイムスタンプ列が定義されていて、かつrowに含まれていない場合はここで自動付与する
        if"timestamp" in fieldnames and "timestamp" not in row:
            # 元のdictを壊さないためにコピーしてから書き換える
            row = dict(row)
            row["timestamp"] = datetime.cow().strftime("%Y-%m-%d %H:%M:%s")
        safe_row = {k: row.get(k, "") for k in fieldnames}
        w.writerow(safe_row)