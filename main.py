import sys
from stats import count_words, count_chars, sort_char_dict

def get_book_text(path_to_file):
    # open, read and return the file contents.
    with open(path_to_file) as f:
        text = f.read()
    return text

def main():

    if len(sys.argv) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    # read the book
    data_block = get_book_text(file_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")

    # split it up and count
    print("----------- Word Count ----------")
    print(count_words(data_block))

    # count letters
    counts = count_chars(data_block)
    #print(counts)

    # sort the counts as a list of dicts
    print("--------- Character Count -------")
    sorted_list = sort_char_dict(counts)
    for d in sorted_list:
        print(f"{d['char']}: {d['num']}")

    print("============= END ===============")
    return 

main()