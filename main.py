import sys
from stats import get_num_words, get_num_char, convert_dict_to_sortedlistdict



def get_book_text(path_to_file):
    booktext = ""

    with open(path_to_file, encoding="utf8") as f:
        booktext = f.read()
    return booktext



def main():

    if len(sys.argv) != 2:

        # Wrong number of parameters: error message and exit
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    else:

        strpath = sys.argv[1]
        print("")
        print("")
        print(f"Found arg strpath: {sys.argv[1]}")
        print("")

        strbook = get_book_text(strpath)
        num_words = get_num_words(strbook)
        dict_countletters = get_num_char(strbook)
        sorted_listletters= convert_dict_to_sortedlistdict(dict_countletters)

        print("")
        
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {strpath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        #print sorted list of dictionaries
        for dictitem in sorted_listletters:
            if dictitem['char'].isalpha():
                print(f"{dictitem['char']}: {dictitem['num']}")

        print("============= END ===============")

        print("")



main()