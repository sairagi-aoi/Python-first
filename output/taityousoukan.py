from datetime import date
import csv, os

FILE = "health_cat_log.csv"
OWNER_SCALE = {"最悪": -2, "悪い": -1, "普通": 0, "良い": 1, "絶好調": 2}
CAT_SCALE = {"ぐったり": -2, "元気ない": -1, "普通": 0, "元気": 1, "走り回ってる": 2}

def log_entry():
    owner = input("あなたの名前を教えてください: ").strip()
    cat = input("飼い猫の名前教えてください: ").strip()

while True:
    