"""Taller evaluable"""

import os
import re
from collections import Counter
import pandas as pd


#
# Escriba la función job, la cual orquesta las funciones anteriores.
#
def run_job(input_directory, output_directory):
    """Job"""
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Initialize word counter
    word_counts = Counter()
    
    # Process all text files in input directory
    for filename in os.listdir(input_directory):
        if filename.endswith('.txt'):
            file_path = os.path.join(input_directory, filename)
            
            # Read file content
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            
            # Clean and tokenize text
            # Convert to lowercase and extract words (letters only)
            words = re.findall(r'\b[a-zA-Z]+\b', content.lower())
            
            # Update word counts
            word_counts.update(words)
    
    # Sort words alphabetically for consistent output
    sorted_words = sorted(word_counts.items())
    
    # Write word counts to part-00000 file
    output_file = os.path.join(output_directory, 'part-00000')
    with open(output_file, 'w', encoding='utf-8') as file:
        for word, count in sorted_words:
            file.write(f"{word}\t{count}\n")
    
    # Create _SUCCESS file to indicate successful completion
    success_file = os.path.join(output_directory, '_SUCCESS')
    with open(success_file, 'w', encoding='utf-8') as file:
        file.write('')


if __name__ == "__main__":

    run_job(
        "files/input",
        "files/output",
    )
