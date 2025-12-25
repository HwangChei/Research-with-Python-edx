from collections import Counter
text = "This is my test text. We're keeping this text short to keep things manageable."
def count_words(text):
    """
    Count the number of occurrences of each word in a text string. Skip punctuation.

    """ 
    text = text.lower()
    skips = [".", ",", ";", ":", "'", "\"", "“", "”", "‘", "’"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = {}
    for word in text.split(" "):
        #known word
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
        #unknown word
    return word_counts

text = "This is my test text. We're keeping this text short to keep things manageable."
def count_words_fast(text):
    """
    Count the number of occurrences of each word in a text string. Skip punctuation.

    """ 
    text = text.lower()
    skips = [".", ",", ";", ":", "'", "\"", "“", "”", "‘", "’"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts
print(len(count_words("This comprehension check is to check for comprehension.")))
print(count_words_fast(text))
if count_words(text) == count_words_fast(text):
    print(True)
if count_words(text) is count_words_fast(text):
    print(True)
'''
    def read_book(title_path):
        """Read a book and return it as a string."""
        with open(title_path, "r", encoding = "utf8") as current_file:
            text = current_file.read()
            text = text.replace("\n", "").replace("\r", "")
            return text
    text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
    ind =text.find("What's in a name?")
    ind
    sample_text = text[ind :ind + 1000]
    sample_text
'''
