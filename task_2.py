import pandas as pd
from nltk.corpus import wordnet
from task_1 import get_semantic
import re
import os

directory = "MSHCorpus/MSHCorpus/"

def find_file(word, directory):
    for file in os.listdir(directory):
        if file.startswith(word):
            #print(file)
            return file

def load_arff_file(filename, directory):
    data = []
    with open(directory + "/" + filename, "r") as f:
        for line in f:
            line = line.replace('\n', '')
            line = re.split(r',(?=")', line)
            line = line[-1].rsplit(',', 1)
            #print(line)
            data.append(line)
    names = ['citation string', 'class']
    data = data[7:]
    df = pd.DataFrame(data, columns=names)
    return df

def find_senses(word):
    file = find_file(word, directory)
    data = load_arff_file(file, directory)
    #We are computing the sense from the first abstract of the dataset
    sentence = data["citation string"][0]
    print("Sentence:")
    print(sentence)
    sense = get_semantic(sentence, word)
    return sense

# selected 10 regular terms and 10 acronyms randomly
regular_terms = ['Cell', 'Nurse', 'Exercises', 'Borrelia', 'Digestive',
                 'Crack', 'Coffee', 'Tolerance', 'Malaria', 'Radiation']
acronyms = ['IP', 'HR', 'HIV', 'EGG', 'PEP', 'AA', 'Epi', 'TNT', 'PR', 'US']

#printing the results
print("Regular terms:\n")
for word in regular_terms:
    print("Word: ", word)
    print("Synsets:")
    synsets = wordnet.synsets(word)
    for syn in synsets:
        print(syn.definition())
    print("Sense:" ,find_senses(word))
    print("\n")
print("#############################################################")
print("Acronyms:")
for word in acronyms:
    print("Word: ", word)
    print("Synsets:")
    synsets = wordnet.synsets(word)
    for syn in synsets:
        print(syn.definition())
    print("Sense:" ,find_senses(word))
    print("\n")