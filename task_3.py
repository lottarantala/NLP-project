import pywsd
import nltk

sample_sentence = 'I have been prescribed two important drugs today during my visit to clinic'
target_word = 'drug'

# Lesk definitions
print("\nLesk definitions:\n")
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


# Similarity
print("\nSimilarities:\n")

print(f"Path similarity between cosine lesk and original lesk: {pywsd.similarity_by_path(cosLesk, origLesk)}")
print(f"Path similarity between cosine lesk and adapted lesk: {pywsd.similarity_by_path(cosLesk, adaptedLesk)}")
print(f"Path similarity between cosine lesk and simple lesk: {pywsd.similarity_by_path(cosLesk, simpleLesk)}\n")

print(f"Infocontent similarity between cosine lesk and original lesk: {pywsd.similarity_by_infocontent(cosLesk, origLesk, 'res')}")
print(f"Infocontent similarity between cosine lesk and adapted lesk: {pywsd.similarity_by_infocontent(cosLesk, adaptedLesk, 'res')}")
print(f"Infocontent similarity between cosine lesk and simple lesk: {pywsd.similarity_by_infocontent(cosLesk, simpleLesk, 'res')}\n")


# Highest lemma count
highest_lemmacount = pywsd.max_lemma_count(target_word)
print(f"Highest lemma count for the word 'drug': {highest_lemmacount}")