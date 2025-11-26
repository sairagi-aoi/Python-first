import csv
import sys
from pathlib import Path
from collections import defaultdict


def append_csv(path, row, fieldnames):
      """
      指定されたCSVファイルに1行分のレコードを追記する。
      
      Args:
          path: 追記対象のCSVファイルのパス
          row: CSVに書き込む1行分のデータを表す辞書
          fieldnames: CSVの列名のリスト
      """
      path = Path(path)
      file_exists = path.exists()

      with open(path, 'a', newline='', encoding='utf-8') as f:
          writer = csv.DictWriter(f, fieldnames=fieldnames)
          if not file_exists:
              writer.writeheader()
          writer.writerow(row)


def read_input_csv(filepath):
      """
      入力CSVファイルを読み込む。
      
      Args:
          filepath: 入力CSVファイルのパス
          
      Returns:
          CSVの各行を辞書形式で格納したリスト
      """
      try:
          with open(filepath, 'r', encoding='utf-8') as f:
              reader = csv.DictReader(f)
              # 必要な列の存在チェック
              required_columns = {'date', 'owner_condition', 'cat_condition'}
              if not required_columns.issubset(set(reader.fieldnames or [])):
                  print(f"エラー: 必要な列 {required_columns} が存在しません。")
                  sys.exit(1)
              return list(reader)
      except FileNotFoundError:
          print(f"エラー: ファイル '{filepath}' が見つかりません。")
          sys.exit(1)
      except Exception as e:
          print(f"エラー: ファイルの読み込み中にエラーが発生しました: {e}")
          sys.exit(1)


def aggregate_by_date(data):
      """
      日付ごとに飼い主と猫の平均体調を集計する。
      
      Args:
          data: CSVデータのリスト（辞書形式）
          
      Returns:
          日付ごとの集計結果のリスト
      """
      daily_data = defaultdict(lambda: {'owner': [], 'cat': []})

      for row in data:
          date = row.get('date', '').strip()
          owner_cond = row.get('owner_condition', '').strip()
          cat_cond = row.get('cat_condition', '').strip()

          # 欠損データのチェック
          if not date or not owner_cond or not cat_cond:
              continue

          try:
              owner_val = float(owner_cond)
              cat_val = float(cat_cond)
              daily_data[date]['owner'].append(owner_val)
              daily_data[date]['cat'].append(cat_val)
          except ValueError:
              # 数値に変換できない場合はスキップ
              continue

      # 平均を計算
      results = []
      for date in sorted(daily_data.keys()):
          owner_vals = daily_data[date]['owner']
          cat_vals = daily_data[date]['cat']

          avg_owner = sum(owner_vals) / len(owner_vals) if owner_vals else 0
          avg_cat = sum(cat_vals) / len(cat_vals) if cat_vals else 0

          results.append({
              'date': date,
              'avg_owner_condition': avg_owner,
              'avg_cat_condition': avg_cat
          })

      return results


def write_summary(results, output_path='summary.csv'):
      """
      集計結果をsummary.csvに書き出す。
      
      Args:
          results: 集計結果のリスト
          output_path: 出力ファイルのパス
      """
      fieldnames = ['date', 'avg_owner_condition', 'avg_cat_condition']

      # 既存ファイルがあれば削除（append_csvを使うため、初回はクリーンな状態にする）
      output_file = Path(output_path)
      if output_file.exists():
          output_file.unlink()

      for row in results:
          append_csv(output_path, row, fieldnames)


def main():
      """
      メイン処理。
      """
      # コマンドライン引数のチェック
      if len(sys.argv) < 2:
          print("使用方法: python taityousoukan.py input.csv")
          sys.exit(1)

      input_filepath = sys.argv[1]

      # CSVの読み込み
      data = read_input_csv(input_filepath)

      # 日付ごとに集計
      results = aggregate_by_date(data)

      # summary.csvに書き出し
      write_summary(results)

      print(f"集計が完了しました。結果は summary.csv に保存されています。")


if __name__ == "__main__":
      main()