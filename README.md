# AI/LLMs Mentorship

A Python tool that analyzes text files and displays beautiful statistics in the console.

## Features

- **Word Count**: Counts total number of words in the text
- **Sentence Count**: Counts sentences (split by `.`, `!`, `?`)
- **Top 10 Frequent Words**: Shows the most common words (case-insensitive, ignoring punctuation)

## Requirements

- Python 3.6 or higher
- No external dependencies (uses only standard library)

## Installation

No installation required. Just download the script and you're ready to go.

## Usage

1. Place `text_analyzer.py` and `sample_text.txt` in the same directory

2. Run the script:
```bash
python text_analyzer.py
```

3. The script will analyze `sample_text.txt` and display formatted tables with statistics

## Output Example

```
============================================================
                  TEXT ANALYSIS REPORT
============================================================

┌──────────────────────────────────────────────────────────┐
│                  BASIC STATISTICS                        │
├──────────────────────────────────────────────────────────┤
│  Word Count:      150                                    │
│  Sentence Count:  25                                     │
└──────────────────────────────────────────────────────────┘


┌──────────────────────────────────────────────────────────┐
│               TOP 10 MOST FREQUENT WORDS                 │
├──────────┬────────────────────────────┬──────────────────┤
│   Rank   │          Word              │   Frequency      │
├──────────┼────────────────────────────┼──────────────────┤
│    #1    │  ai                        │      5           │
│    #2    │  we                        │      4           │
└──────────┴────────────────────────────┴──────────────────┘

============================================================
```

## Functions

### `analyze_text(text: str) -> Dict`
Analyzes the input text and returns a dictionary with:
- `word_count`: Total number of words
- `sentence_count`: Total number of sentences
- `top_words`: List of tuples containing (word, frequency) for top 10 words

### `display_statistics(stats: Dict) -> None`
Takes the statistics dictionary and displays it in beautifully formatted console tables.

## Customization

To analyze a different file, modify the filename in the `main()` function:
```python
with open('your_file.txt', 'r', encoding='utf-8') as f:
    text = f.read()
```

## Author

Mostafa Deghady