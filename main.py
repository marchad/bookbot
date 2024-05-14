def main():
    book_path = "books/frankenstein.txt"

    def get_text(p):
        with open(p) as f:
            text = f.read()
            return text     

    def word_count(c):
        count_nwords = len(c.split())
        return count_nwords
        
    def count_letters(a):
        alph_dict = {}
        a_min = a.lower()
        alphabet= "abcdefghijklmnopqrstuvwxyz"
        counter=int()
        for i in alphabet:
            counter = a_min.count(i)
            entry={i:counter}
            alph_dict.update(entry)
        return alph_dict    
    

    def frankenstein_report(b):
        print("*** THE FRANKENSTEIN REPORT ***")
        print(f"There are {count_words} words in this book.")
        for key in b:
            print(f"The letter {key} has {b[key]} occurences in this text.\n")
        print('--- END OF REPORT---')
    


    book_content = get_text(book_path)
    count_words = word_count(book_content)
    alpha_dict = count_letters(book_content)
    frankenstein_report(alpha_dict)


main()