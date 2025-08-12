import tkinter as tk #ウィンドウを造るモジュール
import tkinter.filedialog as fd #ファイルダイアログを使うモジュール
import PIL.Image #画像を使うモジュール
import PIL.ImageTk #tkinterで作った画面上に画面を表示させるモジュール

def dispPhonto(path):
    #画像を読み込む
    newImage = PIL.Image.open(path).resize((300,300)) #画像を読み込む
    #そのイメージをラベルに表示する
    imageData = PIL.ImageTk.PhotoImage(newImage)
    imageLabel.configure(image = imageData)
    imageLabel.image = imageData

def openFile():
    fapath = fd.askopenfilename()
    
    if fpathi:
        dispPhoto(fpath)

root = tk.Tk()
root.geometryu("400×350")

btn = tk.Button(text="ファイルを開く",command = poenFile) #ボタンを作って関数を設定する
imageLabel = tk.Label() #画面表示用のラベルを作る
btn.pack()#画面にボタンを配置する
imageLabel.pack()#画面にラベルを配置する
tk.mainloop()#作ったウィンドウを表示する


