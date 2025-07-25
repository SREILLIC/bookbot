from stats import count_words
from stats import count_characters

#main...nuff said
def main():
    #capture dict in var
    number_of_each_character = count_characters("books/frankenstein.txt")

    #print word count
    print(f"{count_words("books/frankenstein.txt")} words found in the document")
    #print dict None
    print(number_of_each_character)

main()