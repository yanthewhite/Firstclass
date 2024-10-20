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

def pretty_print(word_dict):
    """
    Nicely prints the dictionary sorted by word frequency.
    :param word_dict: dict : The dictionary to print
    """
    sorted_words = sorted(word_dict.items(), key=lambda item: item[1], reverse=True)
    for word, count in sorted_words:
        print(f"{word}: {count}")

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

    pretty_print(word_dict)

if __name__ == "__main__":
    main()

