from nltk import word_tokenize, ngrams, pos_tag
from collections import Counter
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from pprint import pprint
import csv


english_stopwords = stopwords.words('english')


def get_word_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    token_list = []
    tokens = word_tokenize(text.lower())
    token_list = token_list + tokens
    frequencies = Counter(token_list)
    for token, count in frequencies.most_common(25):
        print(token, count)


def get_bigram_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    all_bigrams = []
    tokens = word_tokenize(text.lower())
    bigrams = list(ngrams(tokens, 2))
    all_bigrams = all_bigrams + bigrams
    frequencies = Counter(all_bigrams)
    for token, count in frequencies.most_common(100):
        print(token, count)


def get_trigram_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    all_trigrams = []
    tokens = word_tokenize(text.lower())

    trigrams = list(ngrams(tokens, 3))
    all_trigrams = all_trigrams + trigrams
    frequencies = Counter(all_trigrams)
    for token, count in frequencies.most_common(100):
        print(token, count)


def get_pos_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    tokens = word_tokenize(text.lower())
    tags = pos_tag(tokens)
    pprint(tags)


##################################################################


# Accounts for word stems so "changes" and "changed" aren't counted separately.
# Filters stopwords ("the", "at", "a", "an", etc.) and words > 3 characters.


def new_get_word_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    tokens = word_tokenize(text.lower())
    stemmer = PorterStemmer()
    token_list_stemmed = []

    for token in tokens:
        stemmed_token = stemmer.stem(token)
        token_list_stemmed.append(stemmed_token)
    stopwords = [
        x for x in token_list_stemmed if x not in set(english_stopwords)]
    result = [item for item in stopwords if len(item) > 2]
    fdist = FreqDist(result)
    fdist1 = fdist.most_common(100)
    with open('data/' + coach + '_word_freq.csv', 'w') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        writer.writerows(fdist1)


def new_get_bigram_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    all_bigrams = []
    tokens = word_tokenize(text.lower())
    stemmer = PorterStemmer()
    token_list_stemmed = []
    for token in tokens:
        stemmed_token = stemmer.stem(token)
        token_list_stemmed.append(stemmed_token)
    stopwords = [
        x for x in token_list_stemmed if x not in set(english_stopwords)]
    result = [item for item in stopwords if len(item) > 2]
    bigrams = list(ngrams(result, 2))
    all_bigrams = all_bigrams + bigrams
    frequencies = Counter(all_bigrams)
    final = []
    for token, count in frequencies.most_common(100):
        lister = token, count
        final.append(lister)
    with open('data/' + coach + '_bigram_freq.csv', 'w') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        writer.writerows(final)


def new_get_trigram_freq(coach):
    file = open('txt/' + coach + '.txt', 'r')
    text = file.read()
    all_trigrams = []
    tokens = word_tokenize(text.lower())
    stemmer = PorterStemmer()
    token_list_stemmed = []
    for token in tokens:
        stemmed_token = stemmer.stem(token)
        token_list_stemmed.append(stemmed_token)
    stopwords = [
        x for x in token_list_stemmed if x not in set(english_stopwords)]
    result = [item for item in stopwords if len(item) > 2]
    trigrams = list(ngrams(result, 3))
    all_trigrams = all_trigrams + trigrams
    frequencies = Counter(all_trigrams)
    final = []
    for token, count in frequencies.most_common(100):
        lister = token, count
        final.append(lister)
    with open('data/' + coach + '_trigram_freq.csv', 'w') as fp:
        writer = csv.writer(fp, quoting=csv.QUOTE_ALL)
        writer.writerows(final)


coach = input(
    "Which coach? (bobknight, coachk, johnwooden, patsummitt, or philjackson) ")

# get_word_freq(coach)
# get_bigram_freq(coach)
# get_trigram_freq(coach)
# get_pos_freq(coach)

new_get_word_freq(coach)
new_get_bigram_freq(coach)
new_get_trigram_freq(coach)
