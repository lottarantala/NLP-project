import pandas as pd

#ambiguous_terms = pd.read_csv("MSHCorpus/MSHCorpus/benchmark_mesh.txt", sep="\t")
with open("MSHCorpus/MSHCorpus/benchmark_mesh.txt", 'r') as file:
    ambiguous_terms = []

    # Iterate over the lines of the file
    for line in file:
        # Remove the newline character at the end of the line
        line = line.strip()
        values = line.split("\t")
        # Append the line to the list
        ambiguous_terms.append(values)

# Print the list of lines 
print(ambiguous_terms)