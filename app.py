# Importing the Natural Language Toolkit (nltk) and WordNet from nltk.corpus
import nltk
from nltk.corpus import wordnet as wn
nltk.download('wordnet')  # Downloading the WordNet data

# Initializing a sample tag cloud as a dictionary
# The keys are words and the values are their respective counts
tag_cloud = {'happy': 10, 'joyful': 5, 'sad': 3, 'unhappy': 2, 'merry': 7, 'glad': 8}

# Function to find synonyms of a word using WordNet
def find_synonyms(word):
    synonyms = set()  # Initializing an empty set for synonyms
    for syn in wn.synsets(word):  # Looping through all synsets of the word
        for lemma in syn.lemmas():  # Looping through lemmas in each synset
            synonyms.add(lemma.name())  # Adding the lemma name to the synonyms set
    return synonyms  # Returning the set of synonyms

# Mapping each word in the tag cloud to its most frequent synonym
word_mapping = {}  # Initializing an empty dictionary for word mapping
for word in tag_cloud.keys():  # Looping through each word in the tag cloud
    synonyms = find_synonyms(word)  # Getting synonyms for the word
    # Finding the most frequent synonym based on the tag cloud, or a default value of 0
    most_frequent_synonym = max(synonyms, key=lambda x: tag_cloud.get(x, 0))
    word_mapping[word] = most_frequent_synonym  # Mapping the word to its most frequent synonym

# Aggregating counts based on the mapping
new_tag_cloud = {}  # Initializing an empty dictionary for the new tag cloud
for word, count in tag_cloud.items():  # Looping through items in the original tag cloud
    mapped_word = word_mapping[word]  # Getting the mapped word for each word
    if mapped_word in new_tag_cloud:
        new_tag_cloud[mapped_word] += count  # Incrementing count if the word is already in the new tag cloud
    else:
        new_tag_cloud[mapped_word] = count  # Adding the word with its count if not already present

# Printing the new tag cloud
print(new_tag_cloud)
