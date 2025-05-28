# function to return book from file
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()
# function to call contents of file
def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)
# execute
main()
