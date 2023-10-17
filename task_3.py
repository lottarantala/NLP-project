from pywsd import simple_lesk, original_lesk, adapted_lesk, cosine_lesk, similarity_by_path
import nltk

sample_sentence = 'I have been prescribed two important drugs today during my visit to clinic'
target_word = 'drug'

# Lesk definitions
print("Lesk definitions:\n")
# Original Lesk
origLesk = original_lesk(sample_sentence, target_word)
print(f"Original Lesk definition: {origLesk.definition()}")

# Adapted Lesk
adaptedLesk = adapted_lesk(sample_sentence, target_word, hyperhypo=True)
print(f"Adapted Lesk definition (extended with hypernyms and hyponyms): {adaptedLesk.definition()}")

# Simple Lesk
simpleLesk = simple_lesk(sample_sentence, target_word, hyperhypo=True)
print(f"Simple Lesk definition (extended with hypernyms and hyponyms): {simpleLesk.definition()}")

# Cosine Lesk
cosLesk = cosine_lesk(sample_sentence, target_word, hyperhypo=True)
cosLesk2 = cosine_lesk(sample_sentence, target_word, hyperhypo=False)
print(f"Cosine Lesk definition: {cosLesk.definition()}")

