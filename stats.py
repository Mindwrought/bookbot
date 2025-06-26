def get_book_text(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()

def count_words(text):
    """
    Counts the number of words in the given text string using split method.
    """
    words = text.split()
    return len(words)

def count_characters(text):
    """
    Counts the number of times each character appears in the text, case insensitive.
    Returns a dictionary with characters as keys and counts as values.
    """
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts

def char_count_dict_to_sorted_list(char_counts):
    """
    Converts a character count dictionary to a sorted list of dictionaries,
    each with keys "char" and "num", sorted by count descending.
    """
    char_list = [{"char": char, "num": count} for char, count in char_counts.items()]
    char_list.sort(key=lambda x: x["num"], reverse=True)
    return char_list

