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

def word_stats(word_counts):
    """ Return number of unique words and their frequency."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)
text = read_book("./Books/English/shakespeare/Romeo and Juliet.txt")
word_counts = count_words(text)
(num_unique, counts) = word_stats(word_counts)
print(num_unique)