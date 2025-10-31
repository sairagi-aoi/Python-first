# Health Journal

Health Journal - A tool for tracking health data

## License

MIT

## Requirements

- Python 3.12+

## Initial Setup / 初期セットアップ

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd python-sync
   ```

2. Create and activate virtual environment
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   pip install pytest
   ```

## Usage / 使い方

### Check version / バージョン確認

```bash
python -m health_journal --version
```

Output:
```
health_journal 0.1.0
```

### Show help / ヘルプ表示

```bash
python -m health_journal --help
```

### Wellness Log / 体調ログ記録

Health Journal allows you to track your daily wellness data including mood, energy levels, symptoms, medications, and notes.

#### Interactive Mode / 対話モード

Run the command without arguments to enter interactive mode:

```bash
python -m health_journal wellness log
```

Example session:
```
体調ログを記録します（Ctrl+C で中断）
気分 (-2=とても悪い, -1=悪い, 0=普通, 1=良い, 2=とても良い): 1
エネルギー (0-10): 7
症状 (カンマ区切り、例: headache,nausea): headache
服薬 (カンマ区切り、任意): ibuprofen
タグ (カンマ区切り、任意): work
メモ (複数行可、空行で終了):
夕方から頭痛。睡眠不足っぽい。

保存しました: journal/2025/10/2025-10-30T213700+0900.md
```

#### Non-Interactive Mode / 非対話モード

Specify all values as command-line arguments:

```bash
python -m health_journal wellness log \
  --mood 1 \
  --energy 7 \
  --symptoms "headache" \
  --meds "ibuprofen" \
  --tags "work" \
  --note "夕方から頭痛。睡眠不足っぽい。"
```

#### Dry-Run Mode / ドライランモード

Preview the output without saving:

```bash
python -m health_journal wellness log \
  --mood 1 \
  --energy 7 \
  --symptoms "headache" \
  --dry-run
```

Output:
```
=== Dry-run: 以下の内容が保存されます ===
---
schema: health-journal/v1
timestamp: '2025-10-30T21:37:00+09:00'
mood: 1
energy: 7
symptoms:
- headache
---
夕方から頭痛。睡眠不足っぽい。
=== 保存先: journal/2025/10/2025-10-30T213700+0900.md ===
```

#### Validation Rules / バリデーションルール

- **mood**: Must be -2, -1, 0, 1, or 2
- **energy**: Must be 0 to 10 (inclusive)
- **symptoms, meds, tags**: Comma-separated lists (optional, can be empty)

#### Output Format / 出力形式

Journal entries are saved as Markdown files with YAML front matter:

**File Path:** `journal/{YYYY}/{MM}/{YYYY-MM-DDTHHMMSS+0900}.md`

**Example:**
```markdown
---
schema: health-journal/v1
timestamp: '2025-10-30T21:37:00+09:00'
mood: 1
energy: 7
symptoms:
- headache
meds:
- ibuprofen
tags:
- work
---
夕方から頭痛。睡眠不足っぽい。
```

**Note:** `meds` and `tags` fields are omitted from the front matter when empty.

### Wellness Stats / 統計情報

View aggregated statistics from your journal entries:

```bash
python -m health_journal wellness stats
```

Output example:
```
Range: last 30d (from 2025-10-01 to 2025-10-30 JST)
Entries: 27
Avg mood: 0.37 / Avg energy: 6.85
Top symptoms: headache(6), nausea(3), fatigue(2)
Top tags: work(7), sleep(5), gym(3)
```

**Period options:**
- `--since 7d` - Last 7 days
- `--since 4w` - Last 4 weeks
- `--since 3m` - Last 3 months (approximate)
- Default: 30d

Examples:
```bash
# Last week
python -m health_journal wellness stats --since 7d

# Last 3 months
python -m health_journal wellness stats --since 3m
```

### Wellness List / エントリ一覧

View a chronological list of journal entries:

```bash
python -m health_journal wellness list
```

Output example (newest first):
```
2025-10-30T22:03:39+09:00  mood=-1  energy=4  journal/2025/10/2025-10-30T220339+0900.md
2025-10-27T14:00:00+09:00  mood=0   energy=5  journal/2025/10/2025-10-27T140000+0900.md
2025-10-26T12:00:00+09:00  mood=-1  energy=4  journal/2025/10/2025-10-26T120000+0900.md
```

**Period options:** Same as stats (`--since 7d`, `--since 4w`, `--since 3m`)

Example:
```bash
# Entries from last week
python -m health_journal wellness list --since 7d
```

### Error Handling / エラー処理

The stats and list commands gracefully handle corrupted or incomplete entries:
- Entries with broken YAML front matter are skipped with a warning
- Entries missing required fields are skipped with a warning
- Exit code is always 0 (success) to avoid breaking automated workflows

Example warning:
```
WARNING: Failed to parse YAML in journal/2025/10/corrupted.md: ...
```

### AI-Assisted Analysis / AI活用分析

For deeper insights, you can use AI tools to analyze your journal data. See [`analysis/README.md`](analysis/README.md) for:
- Workflow for extracting and sharing data with AI assistants (Cursor, ChatGPT, Claude, etc.)
- Sample prompts for trend analysis, pattern recognition, and recommendations
- Front matter specification (schema v1)
- Privacy and security considerations

## Development / 開発

### Run tests / テスト実行

```bash
pytest
```

### Run tests with verbose output / 詳細出力でテスト実行

```bash
pytest -v
```

## Project Structure / プロジェクト構成

```
python-sync/
├── .github/
│   ├── workflows/
│   │   └── ci.yml              # CI workflow
│   └── pull_request_template.md # PR template
├── src/
│   └── health_journal/
│       ├── __init__.py         # Package initialization
│       └── __main__.py         # CLI entry point
├── tests/
│   ├── conftest.py             # pytest configuration
│   ├── test_smoke.py           # Smoke tests
│   └── test_io_csv.py          # CSV I/O tests
├── pyproject.toml              # Project configuration
├── requirements.txt            # Dependencies
└── README.md                   # This file
```
