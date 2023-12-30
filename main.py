def load_text(relative_path):
    # Open file and read contents in as a string
    with open(relative_path) as f:
        file_contents = f.read()

    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    # Create dictionary to hold counts of each letter
    character_dict = {}

    for character in text:
        # convert all characters to lowercase
        c = character.lower()
        # If lowercase character c is already in the dictionary increment count by one
        # Else initialize character count to one
        if c in list(character_dict.keys()):
            character_dict[c] += 1
        else:
            character_dict[c] = 1
    
    return character_dict

def print_report(character_dict, word_count, book_path):
    # Sort values
    dictionary_keys = list(character_dict.keys())
    dictionary_keys.sort()

    print("--- Begin report of " + book_path + " ---")
    print(f"{word_count} words found in the document")
    print("")
    for key in dictionary_keys:
        if key.isalpha():
            print(f"The {key} character was found {character_dict[key]} times")

def main():
    book_path = "books/frankenstein.txt"

    frankenstein_text = load_text(book_path)
    word_count = count_words(frankenstein_text)
    letter_dict = count_letters(frankenstein_text)
    print_report(letter_dict, word_count, book_path)

main()