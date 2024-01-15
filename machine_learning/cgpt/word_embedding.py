from gensim.models import Word2Vec
from nltk.tokenize import word_tokenize  # You may need to install nltk: pip install nltk

# Example sentences (you can replace them with your own dataset)
sentences = [
    "Word embeddings are dense vector representations of words.",
    "They capture semantic information about words.",
    "Word2Vec is a popular technique for generating word embeddings."
]

# Tokenize the sentences
tokenized_sentences = [word_tokenize(sentence.lower()) for sentence in sentences]

# Train Word2Vec model
model = Word2Vec(sentences=tokenized_sentences,
                 vector_size=100, window=5,
                 min_count=1, workers=4)

# Save the model (optional)
# model.save("word2vec_model")

# Get the embedding for a specific word (e.g., 'word')
embedding = model.wv['word']

print("Word embedding for 'word':", embedding)
