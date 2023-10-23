from metaphone import doublemetaphone
import Levenshtein
from nltk.corpus import stopwords
import nltk
import numpy as np

sentence = "I have been prescribed two important drugs today during my visit to clinic"

# Removing stopwords
stop_words = set(stopwords.words('english'))

# Tokenize the sentence into words and remove stopwords
words = nltk.word_tokenize(sentence)
filtered_words = [word for word in words if word.lower() not in stop_words]
print(filtered_words)

# Create a matrix to store the phonetic distances
phonetic_distance_matrix = np.zeros((len(filtered_words), len(filtered_words)))

# Calculate the edit distance between Double Metaphone codes of each pair of words
for i in range(len(filtered_words)):
    for j in range(len(filtered_words)):
        if i != j:
            # Calculate Double Metaphone codes for each word
            metaphone_i = doublemetaphone(filtered_words[i])[0]
            metaphone_j = doublemetaphone(filtered_words[j])[0]
            
            # Calculate the edit distance between Double Metaphone codes
            dist = sum(Levenshtein.distance(mi, mj) for mi, mj in zip(metaphone_i, metaphone_j))
            phonetic_distance_matrix[i, j] = dist

# Display the phonetic distance matrix
for i in range(len(filtered_words)):
    for j in range(len(filtered_words)):
        print(f"{filtered_words[i]} <-> {filtered_words[j]}: {phonetic_distance_matrix[i, j]}")