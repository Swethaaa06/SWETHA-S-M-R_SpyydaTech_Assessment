import re
from collections import Counter
def word_frequency_counter(text: str):
    text = text.lower()
    words = re.findall(r"[a-zA-Z]+", text)
    counts = Counter(words)
    for word, freq in sorted(counts.items(), key=lambda x: (-x[1], x[0])):
        print(f"{word} - {freq}")
# Example
if __name__ == "__main__":
    paragraph = "Hello world, hello Spyyda"
    word_frequency_counter(paragraph)