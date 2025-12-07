"""
Refactored code following the Single Responsibility Principle (SRP)

ORIGINAL VIOLATION:
The original TextAnalyzer class had TWO responsibilities:
1. Text analysis (word counting)
2. File I/O (saving to file)

This violates SRP because the class has multiple reasons to change.

REFACTORED SOLUTION:
Separated concerns into two focused classes:
- TextAnalyzer: Handles ONLY text analysis
- FileWriter: Handles ONLY file operations
"""


class TextAnalyzer:
    """
    Single Responsibility: Analyze text content
ECHO is off.
    This class is focused solely on text analysis operations.
    It has one reason to change: if text analysis logic needs to change.
    """
ECHO is off.
    def __init__(self, text):
        self.text = text
ECHO is off.
    def word_count(self):
        """
        Count the number of words in the text.
ECHO is off.
        Returns:
            int: The number of words
        """
        words = self.text.split()
        count = len(words)
        print(f"Word count: {count}")
        return count


class FileWriter:
    """
    Single Responsibility: Handle file writing operations
ECHO is off.
    This class is focused solely on file I/O operations.
    It has one reason to change: if file writing logic needs to change.
    """
ECHO is off.
    def save_text_to_file(self, text, filename):
        """
        Save text content to a file.
ECHO is off.
        Args:
            text (str): The text to save
            filename (str): The name of the file to write to
        """
        with open(filename, "w") as f:
            f.write(text)
        print(f"Text saved to {filename}")


# Demo usage
if __name__ == "__main__":
    text = "An example that violates a SOLID principle."
ECHO is off.
    # Text analysis is handled by TextAnalyzer
    analyzer = TextAnalyzer(text)
    word_count = analyzer.word_count()
ECHO is off.
    # File operations are handled by FileWriter
    writer = FileWriter()
    writer.save_text_to_file(text, "example.txt")
ECHO is off.
    print("\n✓ Refactoring complete: Each class now has a single responsibility")
