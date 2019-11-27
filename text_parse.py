import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import ne_chunk, pos_tag
from collections import Counter

text = 'This is the song that doesn\'t end. Yes, it goes on and on, my friend. Some people started singing without knowing what it was. And they\'ll continue singing just because...'

sents = sent_tokenize(text)
# print(sents)

words = word_tokenize(text.lower())
# print(words)

# print(nltk.wordpunct_tokenize(text))

# Creates tuple of each word and it's corresponding part of speech
# print(nltk.pos_tag(words))


def entities(text):
    return ne_chunk(
        pos_tag(
            word_tokenize(text)))


tree = entities("Unai Emery’s Arsenal are bad, and everybody knows it. Your eyes tell you when you watch them, and the numbers bear it out too. This, after all, is their worst start to a season in 37 years. For many Arsenal fans there is an almost intuitive sense that Emery is simply the wrong man to lead this team.")
tree.pprint()
# tree.draw()
