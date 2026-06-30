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
    def __init__(self, filepath: str):
        self._filepath = Path(filepath)
        self._frequencies = {}

    def process_file(self) -> bool:
        # TODO: text cleaning will go here
        pass

    def print_report(self):
        #TODO: abc sorting and printing the report will go here
        pass

def main():
    #TODO: menu loop, input validation, and class execution
    pass

if __name__ == "__main__":
    main()