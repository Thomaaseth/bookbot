def get_word_count(book: str):
    count = book.split()
    return len(count)

def get_character_count(book: str):
    char = book.lower()
    
    total_char = {}

    for letter in char:
        if letter in total_char: 
            total_char[letter] += 1
        else:
            total_char[letter] = 1
    return total_char

def sort_char_count(total_char): 
    char_list = []

    for char, count in total_char.items():
        char_list.append({"char": char, "count": count})

    char_list.sort(reverse=True, key=lambda dict: dict["count"])


    return char_list

    
    