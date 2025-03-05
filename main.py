import sys
from stats import get_word_count, get_character_count, sort_char_count

def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        return f.read()
    
if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
    
def main():

    book_path = sys.argv[1]
    text = get_book_text(book_path)    

    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print(f"----------- Word Count ----------")
    print(f"Found {get_word_count(text)} total words")
    print(f"----------- Character Count ----------")
    
    char_count_dict = get_character_count(text)
    sorted_char = sort_char_count(char_count_dict)

    for char_dict in sorted_char:
        char = char_dict["char"]
        count = char_dict["count"]

        if char.isalpha():
            print(f"{char}: {count}")
    print(f"----------- END ----------")

main()