def count_words(book_txt):
    num_words = len(book_txt.split())
    return f"Found {num_words} total words"

def count_chars(book_txt):
    counts={}
    text = book_txt.lower()

    for c in text:
        if c.isalpha():
            if c not in counts:
                counts[c] = 0
            counts[c] += 1
    return counts   

def sort_char_dict(char_dict):

    def sort_on(items):
        return items["num"]

    unsorted = []

    # add all the key-value pairs to a list of dictionaries
    for k in char_dict:
        unsorted.append({"char": k, "num": char_dict[k]})
    # sort and return
    unsorted.sort(reverse=True, key=sort_on)
    return unsorted