# DO NOT EDIT THIS CODE!
import os
import pandas as pd
import numpy as np
from collections import Counter

def count_words_fast(text):
    text = text.lower()
    skips = [".", ",", ";", ":", "'", '"', "\n", "!", "?", "(", ")"]
    for ch in skips:
        text = text.replace(ch, "")
    word_counts = Counter(text.split(" "))
    return word_counts

def word_stats(word_counts):
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique, counts)

hamlets = pd.read_csv("hamlets.csv", index_col=0)
language, text = hamlets.iloc[0:3, 0], hamlets.iloc[0]
text = " ".join(text)
counted_text = count_words_fast(text)

data = pd.DataFrame({
    "word": list(counted_text.keys()),
    "count": list(counted_text.values()),
    "length": [len(word) for word in list(counted_text.keys())],
    "frequency": [ "frequent" if count > 10 else "infrequent" if count <= 10 and count > 1 else "unique" for count in list(counted_text.values())]
})
'''
Without using data.groupby()
unique = 0
for i in data['frequency']:
    if i == 'unique':
        unique += 1
print(unique)
'''
data["length"] = data["word"].apply(len)

data.loc[data["count"] > 10,  "frequency"] = "frequent"
data.loc[data["count"] <= 10, "frequency"] = "infrequent"
data.loc[data["count"] == 1,  "frequency"] = "unique"

sub_data = pd.DataFrame({
    "language" : [i for i in range(len(language)) for j in range(len(counted_text))],
    "frequency" : ["frequent" if count > 10 else "infrequent" if count <= 10 and count > 1 else "unique" for count in list(counted_text.values())]
})
print(sub_data)