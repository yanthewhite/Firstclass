# DSC 510
# Week 9
# Programming Assignment Week 9
# Author TOUKA
# 10/20/2024
#Program to analyze the text of the Gettysburg.txt

import string

def add_word(word, word_dict):
    """
    Adds a word to the dictionary or updates its count if it already exists.
    :param word: str : The word to add
    :param word_dict: dict : The dictionary to update
    """
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1

def process_line(line, word_dict):
    """
    Processes a line by stripping off punctuation and splitting into words,
    then adds each word to the dictionary.
    :param line: str : The line to process
    :param word_dict: dict : The dictionary to update
    """
    # Remove punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))
    # Split line into words
    words = line.split()
    # Add each word to the dictionary
    for word in words:
        add_word(word.lower(), word_dict)  # Convert to lowercase for uniformity

def process_file(word_dict, file):
    """
    Nicely write  the dictionary to the file.
    :param file: The file to write to.
    :param word_dict: dict : The dictionary to print
    """
    sorted_words = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words:
         file.write(f'{word}: {count}\n')  # write out text from a variable

def main():
    """
    The main function that opens the file, processes each line, and prints the results.
    """
    word_dict = {}

    # Opening the file and processing each line
    try:
        gba_file = open('gettysburg.txt', 'r')
        for line in gba_file:
            process_line(line, word_dict)
        gba_file.close()
    except FileNotFoundError:
        print("Error: The file 'gettysburg.txt' was not found.")
        return
    file_name = input("what is the name of the file")
    file = open(file_name, 'a')
    file.write(str(len(word_dict)))
    process_file(word_dict,file)
    file.close()

if __name__ == "__main__":
    main()

