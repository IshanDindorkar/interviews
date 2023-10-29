from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Create a toy dataset of text documents and corresponding labels
documents = ["I love this product",
             "This is terrible",
             "Great customer service",
             "Waste of money"]
labels = [1, 0, 1, 0]  # 1 for positive sentiment, 0 for negative sentiment

# Vectorize the text data using the bag-of-words approach
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
print(X.toarray())

# Split the data into a training set and a testing set
X_train, X_test, y_train, y_test = train_test_split(X, labels, test_size=0.25, random_state=42)

# Create and train the Multinomial Naive Bayes classifier
nb_classifier = MultinomialNB()
nb_classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = nb_classifier.predict(X_test)

# Calculate the accuracy of the classifier
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
