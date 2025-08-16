import tkinter as tk

def dispLabel():
    lbl.configure(text="こんにちは")

root = tk.Tk() #画面を造る
root.geometry("200x100")

lbl = tk.Label(text="LABEL")#ラベルを作る
btn = tk.Button(text= "PUSH",command = dispLabel)

lbl.pack()#画面にラベルを配置する
btn.pack()#画面にボタンを配置する
tk.mainloop()#作ったウィンドウを表示する

print("早く進めたいね")
