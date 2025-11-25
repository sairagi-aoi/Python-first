# Python-first 🐍

Pythonプログラミング学習リポジトリ

## 📖 概要

このリポジトリは、Pythonの基礎から実践的なアプリケーション開発までを学ぶための個人学習用プロジェクトです。
基礎練習と実用的なプロジェクト（健康ログアプリ）を組み合わせた、実践的な学習を行っています。

**学習開始日**: [学習を始めた日付を記入]
**現在のレベル**: 初級〜中級初期（関数、ファイルI/O、テスト作成まで習得）

## 🎯 主なプロジェクト

### 健康ログアプリ（体調相関分析）
飼い主（自分）と猫（よつば）の体調を記録し、相関関係を分析するアプリケーション。
日々の体調データをCSVファイルに保存し、後で分析できるようにしています。

- **メインファイル**: `taityoukakinaosi.py`
- **改良版**: `output/taityousoukan.py`
- **データファイル**: `health_cat_log.csv`
- **詳細**: [HEALTH_LOG_PROJECT.md](HEALTH_LOG_PROJECT.md)を参照

## 📁 ディレクトリ構造

```
Python-first/
├── fukusyu/              # 基礎練習ファイル（26ファイル）
│   ├── kata.py          # データ型の基礎
│   ├── mosi.py          # 条件分岐
│   ├── siteikuri.py     # ループ処理
│   └── ...              # その他練習ファイル
├── src/                 # 再利用可能なモジュール
│   └── io_csv.py        # CSV操作ユーティリティ
├── tests/               # テストコード
│   ├── test_io_csv.py   # io_csv.pyのテスト
│   └── conftest.py      # pytest設定
├── output/              # 改良版スクリプト
│   └── taityousoukan.py # 健康ログアプリ改良版
├── taityoukakinaosi.py  # 健康ログアプリ（初版）
├── kakikaji.py          # 健康調査システム
├── gazo.py              # 画像表示GUI
├── omiseko.py           # おみくじアプリ
├── sousa.py             # Tkinterボタン練習
├── health_cat_log.csv   # 体調データ（メイン）
└── requirements.txt     # 依存パッケージ
```

## 🚀 セットアップ

### 必要な環境
- Python 3.10以上

### インストール

```bash
# リポジトリをクローン
git clone [リポジトリURL]
cd Python-first

# 依存パッケージをインストール
pip install -r requirements.txt
```

## 💻 使い方

### 健康ログアプリを実行

```bash
# 基本版
python taityoukakinaosi.py

# 改良版（入力バリデーション強化）
python output/taityousoukan.py
```

### テストを実行

```bash
# すべてのテストを実行
pytest

# 特定のテストを実行
pytest tests/test_io_csv.py

# カバレッジ付きで実行
pytest --cov=src
```

## 📚 学習トピック

### すでに習得したスキル ✅
- [x] 変数とデータ型
- [x] 条件分岐（if/elif/else）
- [x] ループ処理（while）
- [x] 文字列操作
- [x] 関数の定義と使用
- [x] ファイル入出力
- [x] CSV操作（DictWriter）
- [x] エラーハンドリング（try/except）
- [x] モジュール化
- [x] 単体テスト（pytest）
- [x] Tkinter基礎（GUI）
- [x] Git基本操作

### 現在学習中 📖
- [ ] [現在取り組んでいるトピックを記入]

### 次に学ぶ予定 🎓
詳細は [NEXT_STEPS.md](NEXT_STEPS.md) を参照

## 📊 学習の記録

学習の進捗や気づきは [LEARNING_LOG.md](LEARNING_LOG.md) に記録しています。

## ⚠️ トラブルシューティング

問題が発生した場合は [TROUBLESHOOTING.md](TROUBLESHOOTING.md) を参照してください。

## 📝 メモ

- コミットメッセージは日本語で記述
- コード内コメントも日本語を使用
- 練習ファイルは `fukusyu/` フォルダに整理
- 実用アプリはルートまたは `output/` に配置

## 🎯 今後の展開

- [ ] データ分析機能の追加（pandas）
- [ ] グラフ可視化（matplotlib）
- [ ] 相関係数の計算と表示
- [ ] Webアプリ化（Flask/FastAPI）
- [ ] データベース連携（SQLite）

---

**学習は継続が大切です。焦らず、楽しみながら進めていきましょう！** 🚀
