def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    # print(text)
    word_count = get_word_count(text)
    print(word_count)

def get_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

main()