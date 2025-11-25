# トラブルシューティング 🔧

プログラミング中によく遭遇する問題と解決方法をまとめています。

## 📋 目次

1. [ファイル操作関連](#ファイル操作関連)
2. [CSV関連](#csv関連)
3. [文字コード関連](#文字コード関連)
4. [構文エラー](#構文エラー)
5. [論理エラー](#論理エラー)
6. [Tkinter/GUI関連](#tkinergui関連)
7. [Git関連](#git関連)
8. [環境・インストール関連](#環境インストール関連)

---

## ファイル操作関連

### ❌ PermissionError: [Errno 13] Permission denied

**エラー例**:
```
PermissionError: [Errno 13] Permission denied: 'health_cat_log.csv'
```

**原因**:
- ファイルが他のアプリケーション（Excel等）で開かれている
- ファイルに書き込み権限がない
- ディレクトリに書き込み権限がない

**解決方法**:
1. **ファイルを閉じる**
   - Excel やテキストエディタでファイルを開いている場合は閉じる

2. **権限を確認**
   ```bash
   # Linux/Mac
   ls -l health_cat_log.csv
   chmod 644 health_cat_log.csv  # 書き込み権限を付与

   # Windows
   # ファイルを右クリック → プロパティ → セキュリティタブで確認
   ```

3. **コードでエラーハンドリング**
   ```python
   try:
       with open("health_cat_log.csv", "a") as f:
           # 処理
   except PermissionError:
       print("❌ ファイルが他のプログラムで開かれています")
       print("   Excelなどを閉じてから再試行してください")
   ```

---

### ❌ FileNotFoundError: [Errno 2] No such file or directory

**エラー例**:
```
FileNotFoundError: [Errno 2] No such file or directory: 'data/health_cat_log.csv'
```

**原因**:
- ファイルやディレクトリが存在しない
- パスの指定が間違っている
- カレントディレクトリが想定と違う

**解決方法**:
1. **ディレクトリの自動作成**
   ```python
   from pathlib import Path

   path = Path("data/health_cat_log.csv")
   path.parent.mkdir(parents=True, exist_ok=True)  # ディレクトリを作成

   with path.open("a") as f:
       # 処理
   ```

2. **パスの確認**
   ```python
   import os
   print(f"現在のディレクトリ: {os.getcwd()}")
   print(f"ファイルは存在する？: {Path('health_cat_log.csv').exists()}")
   ```

3. **絶対パスを使う**
   ```python
   from pathlib import Path

   # スクリプトと同じディレクトリのファイルを指定
   script_dir = Path(__file__).parent
   csv_path = script_dir / "health_cat_log.csv"
   ```

---

## CSV関連

### ❌ CSVファイルのヘッダーが重複する

**問題**:
CSVファイルを開くたびにヘッダー行が追加されてしまう。

**原因**:
ファイルの存在チェックをせずに毎回ヘッダーを書き込んでいる。

**解決方法**:
```python
import csv
from pathlib import Path

def append_csv(path, row, fieldnames):
    path = Path(path)
    file_exists = path.exists()  # ファイルの存在チェック

    with path.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        if not file_exists:  # 存在しない場合のみヘッダー書き込み
            writer.writeheader()
        writer.writerow(row)
```

---

### ❌ タイムスタンプが空になる

**問題**:
CSVファイルのtimestampカラムにデータが入らない。

**原因**:
- タイムスタンプの生成を忘れている
- 辞書のキー名が間違っている（`timstamp` ← typo）

**解決方法**:
```python
from datetime import datetime

# タイムスタンプを自動で追加
row = {
    "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # ← これを忘れずに
    "owner": owner_name,
    "cat": cat_name,
    # ...
}

# キー名のタイポに注意
# ❌ "timstamp"  → ✅ "timestamp"
```

---

## 文字コード関連

### ❌ CSVファイルが文字化けする（Excelで開いた時）

**問題**:
ExcelでCSVを開くと、日本語が文字化けする。

**原因**:
- ExcelはデフォルトでShift_JISを期待する
- PythonはデフォルトでUTF-8で保存

**解決方法**:

**方法1: UTF-8 with BOMで保存**（推奨）
```python
with open("health_cat_log.csv", "a", newline="", encoding="utf-8-sig") as f:
    # utf-8-sig を使うとBOM付きで保存され、Excelでも正しく表示される
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(row)
```

**方法2: Shift_JISで保存**
```python
with open("health_cat_log.csv", "a", newline="", encoding="shift_jis") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writerow(row)
```

**方法3: Excelで文字コードを指定して開く**
1. Excelを開く
2. データタブ → テキストまたはCSVから
3. 文字コードをUTF-8に設定

---

## 構文エラー

### ❌ SyntaxError: invalid syntax

**エラー例**:
```python
# kakikaji.py:179
while    # ← 条件式が書かれていない
```

**原因**:
- 文が未完成
- コロン `:` の忘れ
- 括弧の閉じ忘れ
- インデントの誤り

**解決方法**:
```python
# ❌ 間違い
while
    print("Hello")

# ✅ 正しい
while True:
    print("Hello")
```

---

### ❌ IndentationError: unexpected indent

**原因**:
インデント（字下げ）が正しくない。

**解決方法**:
1. **タブとスペースを混在させない**
   - エディタの設定でスペース4つに統一（推奨）

2. **ブロックの開始と終了を確認**
   ```python
   # ✅ 正しい
   if True:
       print("Hello")    # 4スペース
       print("World")    # 4スペース

   # ❌ 間違い
   if True:
       print("Hello")    # 4スペース
         print("World")  # 6スペース（ずれている）
   ```

---

### ❌ NameError: name 'xxx' is not defined

**原因**:
- 変数を定義する前に使っている
- 変数名のタイポ

**解決方法**:
```python
# ❌ 間違い
print(owner_name)
owner_name = "佐藤"

# ✅ 正しい
owner_name = "佐藤"
print(owner_name)

# ❌ タイポ
owner_name = "佐藤"
print(ownre_name)  # ← タイポ

# ✅ 正しい
owner_name = "佐藤"
print(owner_name)
```

---

## 論理エラー

### ❌ 無限ループから抜け出せない

**問題**:
プログラムが止まらなくなった。

**原因**:
- `break`文がない
- `break`条件に到達しない

**解決方法**:
```python
# ❌ 危険：抜け出せない
while True:
    answer = input("続けますか？(yes/no): ")
    # breakがない！

# ✅ 安全
while True:
    answer = input("続けますか？(yes/no): ")
    if answer == "no":
        break  # ← 必ず抜け出せる条件を用意

# ✅ より安全：最大回数を設定
max_attempts = 10
for i in range(max_attempts):
    answer = input("続けますか？(yes/no): ")
    if answer == "no":
        break
else:
    print("最大試行回数に達しました")
```

**緊急停止方法**:
- `Ctrl + C` で強制終了

---

### ❌ 条件分岐が想定通りに動かない

**問題**:
if文が期待通りの動作をしない。

**よくある原因と解決方法**:

**原因1: 比較演算子の間違い**
```python
# ❌ 代入になってしまう
if x = 5:  # SyntaxError

# ✅ 比較
if x == 5:
```

**原因2: 文字列比較の失敗（大文字小文字、空白）**
```python
answer = input("yes/no: ")  # ユーザーが "Yes " と入力（大文字＋空白）

# ❌ 一致しない
if answer == "yes":
    print("YES!")

# ✅ 小文字に変換＋空白削除
if answer.strip().lower() == "yes":
    print("YES!")
```

**原因3: 型の不一致**
```python
age = input("年齢: ")  # "25" ← 文字列

# ❌ 比較できない
if age >= 20:  # TypeError

# ✅ 数値に変換
age = int(input("年齢: "))
if age >= 20:
    print("成人です")
```

---

## Tkinter/GUI関連

### ❌ NameError: name 'tkinter' is not defined

**原因**:
Tkinterがインポートされていない。

**解決方法**:
```python
import tkinter as tk

root = tk.Tk()
root.mainloop()
```

---

### ❌ _tkinter.TclError: couldn't open "image.png"

**原因**:
画像ファイルのパスが間違っている。

**解決方法**:
```python
from pathlib import Path
from tkinter import PhotoImage

# スクリプトと同じディレクトリの画像を開く
image_path = Path(__file__).parent / "image.png"

if image_path.exists():
    img = PhotoImage(file=str(image_path))
else:
    print(f"❌ 画像が見つかりません: {image_path}")
```

---

## Git関連

### ❌ git push時にエラーが出る

**エラー例**:
```
! [rejected] main -> main (fetch first)
```

**原因**:
リモートに新しいコミットがあり、ローカルとずれている。

**解決方法**:
```bash
# リモートの変更を取得してマージ
git pull origin main

# コンフリクトがあれば解決

# 再度プッシュ
git push origin main
```

---

### ❌ コミットメッセージを間違えた

**解決方法**:
```bash
# 直前のコミットメッセージを修正
git commit --amend -m "正しいメッセージ"

# プッシュ前なら問題なし
# プッシュ後の場合は注意（force pushが必要）
```

---

## 環境・インストール関連

### ❌ ModuleNotFoundError: No module named 'xxx'

**原因**:
必要なパッケージがインストールされていない。

**解決方法**:
```bash
# パッケージをインストール
pip install パッケージ名

# requirements.txtから一括インストール
pip install -r requirements.txt

# 仮想環境を有効化しているか確認
# venv/bin/activate (Linux/Mac)
# venv\Scripts\activate (Windows)
```

---

### ❌ pytestが動かない

**問題**:
`pytest`コマンドが見つからない、またはテストが実行されない。

**解決方法**:
```bash
# pytestをインストール
pip install pytest

# テストを実行
pytest

# 詳細表示で実行
pytest -v

# カバレッジ付きで実行
pip install pytest-cov
pytest --cov=src
```

---

## 💡 デバッグのコツ

### 1. エラーメッセージをよく読む
エラーメッセージには問題の原因と行番号が書かれています。

### 2. print()デバッグ
```python
# 変数の値を確認
print(f"owner_name: {owner_name}")
print(f"owner_score: {owner_score}")

# 処理の流れを確認
print("--- ここまで来た ---")
```

### 3. 小さく確認
一度にたくさん書かずに、少しずつ動作確認しながら書く。

### 4. コメントアウトで原因を特定
```python
# エラーが出る行をコメントアウトして原因を特定
# problematic_function()
print("ここまでは動く")
```

### 5. 公式ドキュメントを読む
エラーメッセージでGoogle検索すると、同じ問題を経験した人の解決策が見つかる。

---

## 📚 参考リソース

- [Python公式ドキュメント - エラーと例外](https://docs.python.org/ja/3/tutorial/errors.html)
- [Stack Overflow](https://stackoverflow.com/) - プログラミングQ&Aサイト
- [Python公式FAQ](https://docs.python.org/ja/3/faq/)

---

**エラーは学びのチャンス！焦らず一つずつ解決していきましょう 🚀**
