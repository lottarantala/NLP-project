import nltk
from nltk.wsd import lesk 
from nltk.tokenize import word_tokenize 
import time

def get_semantic(seq, key_word): 
	
	# Tokenization of the sequence 
	temp = word_tokenize(seq) 
	
	# Retrieving the definition 
	# of the tokens 
	temp = lesk(temp, key_word) 
	return temp.definition() 

keyword = 'drug'
seq1 = 'I have been prescribed two important drugs today during my visit to clinic'


# Start timer
start_time = time.time()

print(get_semantic(seq1, keyword)) 

# End timer
end_time = time.time()

# Calculate elapsed time
elapsed_time = end_time - start_time
print("Elapsed time: ", elapsed_time) 