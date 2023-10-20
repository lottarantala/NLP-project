import pandas as pd
from nltk.corpus import wordnet
from task_1 import get_semantic
import re
import os

directory = "MSHCorpus/MSHCorpus/"

##TURHAA?
# Read the ambiguous terms to a list:

with open("MSHCorpus/MSHCorpus/benchmark_mesh.txt", 'r') as file:
    ambiguous_terms = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line.strip()
        values = line.split("\t")
        # Append the line to the list
        ambiguous_terms.append(values)

# Print the list of ambiguous words and their CUIs.
# print(ambiguous_terms)
# print(len(ambiguous_terms))
##TURHA LOPPUU
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
    print(sentence)
    sense = get_semantic(sentence, word)
    return sense

# selected 10 regular terms and 10 acronyms randomly
regular_terms = ['Respiration', 'Nursing', 'Glycoside', 'Borrelia', 'Crown',
                 'Crack', 'Ganglion', 'Lactation', 'Synapsis', 'veterinary']
acronyms = ['PVC', 'HR', 'HIV', 'EGG', 'PEP', 'AA', 'EMS', 'TNT', 'PR', 'US']


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