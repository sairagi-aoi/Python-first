# Analysis / 分析

This directory contains guidelines and tools for analyzing health journal data with AI assistance.

## AI-Assisted Analysis Workflow / AI解析ワークフロー

### Step 1: Extract Data / データ抽出

You have several options to extract your journal data for AI analysis:

#### Option A: Use stats command (Quick Overview) / stats コマンド（概要把握）

```bash
python -m health_journal wellness stats --since 90d
```

This provides aggregated statistics:
- Entry count
- Average mood and energy
- Top symptoms and tags

Copy the output and share with your AI assistant (Cursor, ChatGPT, Claude, etc.)

#### Option B: Use list command (Detailed Timeline) / list コマンド（詳細タイムライン）

```bash
python -m health_journal wellness list --since 90d
```

This provides a chronological list of entries with mood, energy, and file paths.

#### Option C: Direct File Access / ファイル直接アクセス

Journal entries are stored in `journal/YYYY/MM/*.md` with structured YAML front matter.

You can:
1. Share individual files with AI for deep analysis
2. Create a script to extract specific fields
3. Use tools like `grep`, `awk`, or Python scripts to process bulk data

### Step 2: Request AI Analysis / AI分析依頼

#### Sample Prompts / サンプルプロンプト

**For trend analysis (using stats output):**
```
Here are my health statistics for the last 90 days:
[paste stats output]

Please analyze:
1. Overall wellness trends (mood and energy patterns)
2. Correlation between symptoms and mood/energy
3. Potential triggers based on tags
4. Recommendations for improving wellness
```

**For detailed pattern recognition (using list output):**
```
Here is my health journal timeline for the last 90 days:
[paste list output]

Please identify:
1. Weekly patterns (are weekends better/worse?)
2. Mood/energy cycles (any recurring patterns?)
3. Anomalies or significant changes
4. Suggestions for data collection improvements
```

**For custom analysis (using raw files):**
```
I'm sharing several journal entries from [date range].
Each entry has:
- timestamp
- mood (-2 to +2)
- energy (0 to 10)
- symptoms
- medications (if any)
- tags
- free-form notes

Please:
1. Identify correlations between symptoms and mood/energy
2. Suggest potential lifestyle factors affecting wellness
3. Recommend visualization approaches
```

### Step 3: Visualization Requirements / 可視化要件

After initial analysis, you can ask AI to help create visualizations:

**Sample prompt:**
```
Based on this data, please suggest Python visualization code using matplotlib or plotly to show:
1. Mood/energy trends over time (line chart)
2. Symptom frequency (bar chart)
3. Tag distribution (pie chart or word cloud)
4. Correlation matrix (heatmap)

Please provide complete, runnable Python code.
```

## Front Matter Specification v1 / Front Matter 仕様 v1

All journal entries follow this schema:

```yaml
---
schema: health-journal/v1      # Schema version (fixed)
timestamp: "YYYY-MM-DDTHH:MM:SS+09:00"  # ISO8601 with JST timezone
mood: -2 | -1 | 0 | 1 | 2      # Required: -2=very bad, -1=bad, 0=neutral, 1=good, 2=very good
energy: 0..10                  # Required: 0=exhausted, 10=fully energized
symptoms:                      # Required: Array of strings (can be empty)
  - headache
  - nausea
meds:                         # Optional: Array of medications (omitted if empty)
  - ibuprofen
tags:                         # Optional: Array of tags (omitted if empty)
  - work
  - sleep
---
Free-form notes (body text, can be multi-line)
```

### Field Definitions / フィールド定義

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `schema` | string | Yes | Always `"health-journal/v1"` |
| `timestamp` | string | Yes | ISO8601 datetime with timezone |
| `mood` | integer | Yes | -2, -1, 0, 1, or 2 |
| `energy` | integer | Yes | 0 to 10 (inclusive) |
| `symptoms` | array | Yes | List of symptom strings (lowercase normalized) |
| `meds` | array | No | List of medication strings (omitted if empty) |
| `tags` | array | No | List of tag strings (omitted if empty) |

### Data Quality Notes / データ品質に関する注意

- All symptoms and tags are normalized to lowercase during processing
- Entries with missing or invalid front matter are skipped with warnings
- Timestamps are in JST (Asia/Tokyo timezone)
- Missing `mood` or `energy` values exclude that entry from average calculations

## Example Analysis Scenarios / 分析シナリオ例

### Scenario 1: Identify Sleep Impact / 睡眠の影響を特定

**Goal:** Determine if poor sleep correlates with low energy/mood

**Approach:**
1. Extract entries tagged with "sleep"
2. Compare mood/energy on days with/without sleep issues
3. Look for symptoms more common on poor sleep days

### Scenario 2: Medication Effectiveness / 薬効の評価

**Goal:** Assess if specific medications improve symptoms

**Approach:**
1. Extract entries with `meds` field containing target medication
2. Compare symptom frequency before/after medication introduction
3. Track mood/energy trends during medication periods

### Scenario 3: Work Stress Analysis / 仕事ストレス分析

**Goal:** Understand work-related stress patterns

**Approach:**
1. Filter entries tagged with "work"
2. Identify mood/energy patterns on work days vs. non-work days
3. Correlate specific symptoms with work stress

## Privacy and Security / プライバシーとセキュリティ

**Important:** Journal entries may contain sensitive health information.

When sharing data with AI services:
- ✅ Use local AI models (Ollama, etc.) for maximum privacy
- ✅ Anonymize data before sharing with cloud AI services
- ✅ Remove or redact sensitive medication names if needed
- ✅ Use aggregate statistics (stats output) rather than raw notes when possible
- ❌ Avoid sharing identifiable information (names, specific locations, etc.)

## Contributing Custom Analysis / カスタム分析の貢献

If you develop useful analysis scripts or notebooks, consider:
1. Creating a `scripts/` subdirectory with your analysis code
2. Documenting data requirements and output format
3. Sharing visualization examples

Example structure:
```
analysis/
├── README.md (this file)
├── scripts/
│   ├── mood_energy_plot.py
│   ├── symptom_heatmap.py
│   └── weekly_report.py
└── examples/
    ├── sample_output.png
    └── sample_report.md
```
