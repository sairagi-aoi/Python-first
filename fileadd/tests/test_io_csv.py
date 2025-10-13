from pathlib import Path
import csv

from src.io_csv import append_csv

FIELDNAMES = ["timestamp","owner","cat"]

def read_csv(path:path):
    with path.open("r", encoding="utf-8" , newline="") as f:
        return list(csv.reader(f))

def test_append_csv_writes_header_once(tmp_pathi):
    p = tmp_path / "log.csv"
    row1 = {"timestamp":"t1","owner":"o1","cat":"c1"}
    row2 = {"timestamp":"t2","owner":"o2","cat":"c2"}
    