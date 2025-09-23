from datetime import date
import csv, os

FILE = "health_cat_log.csv"
OWNER_SCALE = {"最悪": -2, "悪い": -1, "普通": 0, "良い": 1, "絶好調": 2}
CAT_SCALE = {"ぐったり": -2, "元気ない": -1, "普通": 0, "元気": 1, "走り回ってる": 2}

def log_entry():
    owner = input("あなたの名前を教えてください: ").strip()
    cat = input("飼い猫の名前教えてください: ").strip()

while True:
    OWNWER_condition = input("あなたの体調を教えてください >> ").strip()
    
    if OWNWER_condition in ("最悪","悪い"):
        conddition_type = input("その体調不良は精神面と身体面のどちらですか？それとも両方ですか？（精神面/身体面/両方) >>").strip()
        conddition_since = input("その体調不良はいつ頃から発生していますか？ >> ").strip()
        conddition_cause = input("その体調不良の原因として思い当たることはありますか？（無い場合は「無し」と入力して下さい) >> ").strip()
        break
    elif OWNWER_condition in ("普通","良い","絶好調"):
        print("良いですね！ その調子で無理なく楽しんでお過ごし下さい。")
    else:
        print("提示されている選択肢の中からお選びください")
        break

    CAT_condhition = input("飼い猫の様子を教えて下さい >> ").strip()

    if CAT_condhition in ("ぐったり" ,"元気ない"):
        cat_conthition_type = input("")
