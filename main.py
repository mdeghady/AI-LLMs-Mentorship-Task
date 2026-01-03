import re
from collections import Counter
from typing import Dict, List, Tuple


def analyze_text(text: str) -> Dict:
    """
    Analyzes a text string and returns comprehensive statistics.

    Args:
        text: The input text to analyze

    Returns:
        Dictionary containing word_count, sentence_count, and top_words
    """
    # Word count - split by whitespace and filter out empty strings
    words = text.split()
    word_count = len(words)

    # Sentence count - split by sentence terminators
    sentences = re.split(r'[.!?]+', text)
    # Filter out empty strings and whitespace-only strings
    sentences = [s.strip() for s in sentences if s.strip()]
    sentence_count = len(sentences)

    # Top 10 most frequent words (case-insensitive, ignoring punctuation)
    # Remove punctuation and convert to lowercase
    cleaned_words = []
    for word in words:
        # Remove all punctuation including dashes
        cleaned = re.sub(r'[^\w\s]', '', word.lower())
        if cleaned:  # Only add non-empty words
            cleaned_words.append(cleaned)

    # Count word frequencies
    word_freq = Counter(cleaned_words)
    top_words = word_freq.most_common(10)

    return {
        'word_count': word_count,
        'sentence_count': sentence_count,
        'top_words': top_words
    }


def display_statistics(stats: Dict) -> None:
    """
    Displays text analysis statistics in beautiful formatted tables.

    Args:
        stats: Dictionary containing analysis results from analyze_text()
    """
    # Header
    print("\n" + "=" * 60)
    print(" " * 18 + "TEXT ANALYSIS REPORT")
    print("=" * 60 + "\n")

    # Basic Statistics Table
    print("┌" + "─" * 58 + "┐")
    print("│" + " " * 18 + "BASIC STATISTICS" + " " * 24 + "│")
    print("├" + "─" * 58 + "┤")
    print(f"│  Word Count:      {stats['word_count']:<39}│")
    print(f"│  Sentence Count:  {stats['sentence_count']:<39}│")
    print("└" + "─" * 58 + "┘")

    print("\n")

    # Top 10 Words Table
    print("┌" + "─" * 58 + "┐")
    print("│" + " " * 15 + "TOP 10 MOST FREQUENT WORDS" + " " * 17 + "│")
    print("├" + "─" * 10 + "┬" + "─" * 28 + "┬" + "─" * 18 + "┤")
    print("│   Rank   │" + " " * 10 + "Word" + " " * 14 + "│   Frequency      │")
    print("├" + "─" * 10 + "┼" + "─" * 28 + "┼" + "─" * 18 + "┤")

    for i, (word, count) in enumerate(stats['top_words'], 1):
        rank_str = f"#{i}"
        # Truncate long words to fit in the column
        word_display = word[:26] if len(word) > 26 else word
        print(f"│ {rank_str:^8} │  {word_display:<26}│      {count:<10}  │")

    print("└" + "─" * 10 + "┴" + "─" * 28 + "┴" + "─" * 18 + "┘")
    print("\n" + "=" * 60 + "\n")


def main():
    """Main function to read file and display analysis."""
    try:
        # Read the text file
        with open('sample_text.txt', 'r', encoding='utf-8') as f:
            text = f.read()

        # Analyze the text
        stats = analyze_text(text)

        # Display the results
        display_statistics(stats)

    except FileNotFoundError:
        print("Error: sample_text.txt not found!")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()