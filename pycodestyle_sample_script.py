import numpy as np, pandas as pd

# Take the users input
words = raw_input("Enter some text to translate to pig latin: " )

# Break apart the words into a list
words_list = words.split(' ' )

for word in words_list:
    if len(word) >= 3 : # For this pig latin translation, we only want to translate words greater than 3 characters
        pig_latin = word + "%say" % (word[0])
        pig_latin = pig_latin[ 1: ]
        print(pig_latin )
    else:
        pass