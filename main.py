def count_character_occurrences(text):
    """
    Takes a string and returns a dictionary with the count of each alphabetic character,
    converting all characters to lowercase.
    """
    text = text.lower()
    char_count = {}
    for char in text:
        if char.isalpha():  # Only count alphabetic characters
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

def generate_report(text):
    """
    Generates and prints a report of character frequencies.
    """
    char_frequencies = count_character_occurrences(text)
    print("Character Frequency Report:")
    for char, count in sorted(char_frequencies.items()):
        print(f"'{char}': {count}")

# Read the file once
file_path = "/home/kamil/workspace/github.com/kamilkoz7/bookbot/books/frankenstein.txt"
with open(file_path, "r") as f:
    book_text = f.read()

# Print word count
word_count = len(book_text.split())
print(f"Total Words: {word_count}")

# Generate report
generate_report(book_text)