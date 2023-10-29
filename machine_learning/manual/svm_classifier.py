from sklearn import datasets
from sklearn.metrics import precision_recall_fscore_support
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC


def main():
    # Step 1: Load IRIS dataset
    # https://scikit-learn.org/stable/auto_examples/datasets/plot_iris_dataset.html
    iris = datasets.load_iris()
    X = iris.data[:, :2]
    y = iris.target
    print(X.shape)
    print(y.shape)

    # Step 2: Split dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # Step 3: Train SVM Classifier
    svm_classifier = SVC(kernel='linear', C=1.0)
    svm_classifier.fit(X=X_train, y=y_train)

    # Step 4: Prediction using trained SVM classifier
    y_pred = svm_classifier.predict(X=X_test)

    # Step 5: Performance metrics
    p, r, f, s = precision_recall_fscore_support(y_true=y_test, y_pred=y_pred, average="macro")
    print(f"Precision: {p}  Recall: {r}  F1-Score: {f}  Support: {s}")


if __name__ == "__main__":
    main()

# EOF
