from stats import count_words
from stats import count_characters
from stats import list_dicts_sort
import sys

#main...nuff said
def main():

    if len(sys.argv)!= 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    #capture dict in var
    #number_of_each_character = count_characters(None)

    #print report intro
    print("="*12 + " BOOKBOT " + "="*12)
    print(f"Analyzing book found at {sys.argv[1]}...")

    #print word count
    print("-"*11 + " Word Count " + "-"*10)
    print(f"Found {count_words(sys.argv[1])} total words")

    #print dict each character count
    print("-"*9 + " Character Count " + "-"*7)

    #capture output of list_dicts_sort() in var
    list_dicts = list_dicts_sort(sys.argv[1])
    #print list of dicts for letters counts only
    for d in list_dicts:
        print(f"{d["char"]}: {d["num"]}")

    print("="*13 + " END " + "="*15)

main()