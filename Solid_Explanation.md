# SOLID Principle Violation and Refactoring

## Original Code Analysis

### The Violation: Single Responsibility Principle (SRP)

**What is SRP?**
- A class should have only ONE reason to change
- A class should have only ONE responsibility or job

**Original TextAnalyzer Class:**
```python
class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def word_count(self):           # Responsibility 1: Text Analysis
        words = self.text.split()
        count = len(words)
        print(f"Word count: {count}")
        return count
    
    def save_text_to_file(self, filename):  # Responsibility 2: File I/O
        with open(filename, "w") as f:
            f.write(self.text)
        print(f"Text saved to {filename}")
```

**Why This Violates SRP:**
1. The class has TWO distinct responsibilities:
   - Text analysis (word_count method)
   - File management (save_text_to_file method)

2. The class has TWO reasons to change:
   - If we need to change how word counting works
   - If we need to change how file saving works

3. Problems this creates:
   - Tight coupling between unrelated concerns
   - Harder to test (must test both analysis AND file I/O together)
   - Harder to maintain (changes to file I/O affect text analysis class)
   - Violates separation of concerns

## Refactored Solution

### Separated into Two Classes

**TextAnalyzer - Focused on Text Analysis:**
```python
class TextAnalyzer:
    def __init__(self, text):
        self.text = text
    
    def word_count(self):
        words = self.text.split()
        count = len(words)
        print(f"Word count: {count}")
        return count
```
- Single responsibility: Analyze text
- One reason to change: Text analysis logic changes

**FileWriter - Focused on File Operations:**
```python
class FileWriter:
    def save_text_to_file(self, text, filename):
        with open(filename, "w") as f:
            f.write(text)
        print(f"Text saved to {filename}")
```
- Single responsibility: Write to files
- One reason to change: File I/O logic changes

## Benefits of Refactoring

1. **Better Maintainability**: Each class is simpler and focused
2. **Easier Testing**: Can test text analysis and file I/O independently
3. **More Flexibility**: FileWriter can be reused by other classes
4. **Follows SRP**: Each class has exactly one responsibility
5. **Loose Coupling**: Changes to file I/O don't affect text analysis
