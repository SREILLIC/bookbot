# get string data from text
def get_book_text(book):
    with open(book) as f:
        file_contents = f.read()
    return file_contents

# take text as string
#split words into separate strings
#count number of words/strings in text
def count_words(book):
    #call get_book_text to get text
    #get_book_text(book) #(returns text as string (file_contents))

    list_words = get_book_text(book).split() #split the text returned from "get_book_text()"
    #text.split() allready makes a list of words (no need to append)
    
    number_of_words = len(list_words) #get number of words via len()
    return number_of_words
