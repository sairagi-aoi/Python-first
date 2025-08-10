import tkinter as tk
import random

def dispLabel():
   kuji = ["大吉", "中吉", "小吉", "凶"]
   lbl.configure(text=random.choice(kuji))

root = tk.Tk() #画面を造る
root.geometry("200x100")

lbl = tk.Label(text="LABEL")#ラベルを作る
btn = tk.Button(text= "PUSH",command = dispLabel)

lbl.pack()#画面にラベルを配置する
btn.pack()#画面にボタンを配置する
tk.mainloop()#作ったウィンドウを表示する