# 仕様:
# - append_csv(path, row, fieldnames) は CSV に 1 行追記する
# - 新規ファイル（サイズ0）のときだけヘッダ行を書いてから追記する
# - Windows の空行混入を避けるため open(..., newline="") を使う
# - 列順は fieldnames の順で固定する（不足キーは空文字、余分キーは捨てる）
# - 文字コードは UTF-8、親ディレクトリが無ければ作る