import pywsd
import os
import pandas as pd
import re

directory = "MSHCorpus/MSHCorpus/"
# selected 10 regular terms and 10 acronyms randomly
regular_terms = ['Cell', 'Nurse', 'Exercises', 'Borrelia', 'Digestive',
                 'Crack', 'Coffee', 'Tolerance', 'Malaria', 'Radiation']
acronyms = ['IP', 'HR', 'HIV', 'EGG', 'PEP', 'AA', 'Epi', 'TNT', 'PR', 'US']

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

for target_word in regular_terms + acronyms:

    file = find_file(target_word, directory)
    data = load_arff_file(file, directory)
    #We are computing the sense from the first abstract of the dataset
    sample_sentence = data["citation string"][0]
    # Lesk definitions
    print(f"\nLesk definitions for {target_word} :\n")
    # Original Lesk
    origLesk = pywsd.original_lesk(sample_sentence, target_word)
    print(f"Original Lesk definition: {origLesk.definition()}")

    # Adapted Lesk
    adaptedLesk = pywsd.adapted_lesk(sample_sentence, target_word, hyperhypo=True)
    print(f"Adapted Lesk definition (extended with hypernyms and hyponyms): {adaptedLesk.definition()}")

    # Simple Lesk
    simpleLesk = pywsd.simple_lesk(sample_sentence, target_word, hyperhypo=True)
    print(f"Simple Lesk definition (extended with hypernyms and hyponyms): {simpleLesk.definition()}")

    # Cosine Lesk
    cosLesk = pywsd.cosine_lesk(sample_sentence, target_word, hyperhypo=True)
    print(f"Cosine Lesk definition: {cosLesk.definition()}")