import pandas as pd

#Read the ambiguous terms to a list:

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
print(ambiguous_terms)
#print(len(ambiguous_terms))

#selecting 10 regular terms and 10 acronyms randomly
regular_terms = ['Milk', 'Nursing', 'Glycoside', 'Borrelia', 'Crown', 'Crack', 'Ganglion', 'Lactation', 'Synapsis', 'veterinary' ]
acronyms = ['PVC', 'OCD', 'HIV', 'EGG', 'cRNA', 'AA', 'EM', 'MAF', 'PR', 'SPR']

