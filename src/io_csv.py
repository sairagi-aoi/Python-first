from pathlib import Path
import csv

def append_csv(path: str | Path, row: dict, fieldnames: list[str]) -> None:
    """
    csvに１行追加する

    - 新規ファイル（サイズ0)の場合のみ、最初にヘッダ行を書いてから追記
    -Windowsの空行混入対策として newline = ""を必須指定
    - 列順はfieldnames で固定し、欠損キーは "", 余分キーは無視
    """
    p = Path(path)
    p.parent.mkdir(parnts=True, exist_ok=True)
    is_new = (not p.ecists())or (p.stat().st_size == 0)

    