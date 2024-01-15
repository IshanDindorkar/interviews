"""
Topic Modeling using LDA
"""

# Install gensim if not already installed
# pip install gensim

from gensim import corpora
from gensim.models import LdaModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Sample documents
documents = [
    "Natural language processing is a subfield of artificial intelligence.",
    "Topic modeling is useful for discovering hidden topics in a collection of documents.",
    "Latent Dirichlet Allocation is a popular algorithm for topic modeling.",
    "Python is a programming language widely used in data science and machine learning.",
    "Text mining involves extracting useful information from unstructured text data."
]

# Preprocess the documents
stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()


def preprocess_text(text):
    # Text Normalization
    tokens = word_tokenize(text)
    tokens = [token.lower() for token in tokens if token.isalpha()]
    tokens = [token for token in tokens if token not in stop_words]
    tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return tokens


processed_documents = [preprocess_text(doc) for doc in documents]

# Create a dictionary and corpus
dictionary = corpora.Dictionary(processed_documents)
corpus = [dictionary.doc2bow(doc) for doc in processed_documents]

# Train the LDA model
lda_model = LdaModel(corpus, num_topics=2, id2word=dictionary, passes=10, random_state=42)

# Print the topics
for topic_id, topic_words in lda_model.print_topics():
    print(f'Topic {topic_id + 1}: {topic_words}')

# Get the topic distribution for a document
new_document = "Artificial intelligence and machine learning are transforming industries."
new_document_tokens = preprocess_text(new_document)
new_document_bow = dictionary.doc2bow(new_document_tokens)
topic_distribution = lda_model.get_document_topics(new_document_bow)

print(f'Topic Distribution for New Document: {topic_distribution}')
