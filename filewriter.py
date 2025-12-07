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
