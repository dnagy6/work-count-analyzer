"""
Program Name: Word Count Analyzer
Author: Dakota Nagy
Purpose: To analyze user-selected text files, calculate word frequencies using 
         Object-Oriented Programming, and output a sorted alphabetical report.
Starter Code: None used. Developed entirely from assignment guidelines.
Date: July 5, 2026

"""

from pathlib import Path
import string

class WordAnalyzer:
    """
    Starts the WordAnalyzer with a private path object and a private dictionary to hold word frequencies.
    """
    def __init__(self, filepath: str):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def process_file(self) -> bool:
        """
        To see if the file exists, and if it does, read the file line by line, removing punctuation, lowercases text,
        and will update the frequency dictionary. Returns True if successful, False if FileNotFoundError.
        """
        if not self._filepath.exists():
            return False
        
        try:
            punctuation_table = str.maketrans('', '', string.punctuation) #NOTE: Punctuation is !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

            with self._filepath.open('r', encoding='utf-8') as file:
                for line in file:

                    cleaned_line = line.lower()
                    cleaned_line = cleaned_line.translate(punctuation_table)
                    words = cleaned_line.split()

                    for word in words:
                        if word in self._frequencies:
                            self._frequencies[word] += 1
                        else:
                            self._frequencies[word] = 1
            return True
        except FileNotFoundError:
            print(f"Error: The file at {self._filepath} could not be found.")
            return False

    def print_report(self):
        """
        Alphabetical sorting and prints the report in the format: word :: frequency. If no data is available,
        it will print a message indicating that the user should process a file first.
        """
        if not self._frequencies:
            print("No data available. Please process a file first.")
            return
        
        sorted_words = sorted(self._frequencies.keys())

        for word in sorted_words:
            count = self._frequencies[word]
            print(f"{word:<12} :: {count}")

def main():
    """
    Main function to handle user interaction, file processing, and report generation."""
    #TODO: menu loop, input validation, and class execution
    pass

if __name__ == "__main__":
    main()