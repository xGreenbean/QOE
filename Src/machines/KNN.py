import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

"""
K nearest neighbors algorithm for guessing app and video/non video per session
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_knn_quality(test_size, num_of_neighbors):
    features = pd.read_csv('C:\\QOE\\Src\\generators\\test_breaker_filter3000_0.03_250.csv')

    features = features.drop(['filter', 'source_file', 'Unnamed: 0'], axis=1)
    features = features.sample(frac=1)
    features['label'] = features['label'].astype(str)
    features = pd.get_dummies(features)

    # Labels are the values we want to predict

    labels = np.array(features[['label_1', 'label_2', 'label_3', 'label_4']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_1', 'label_2', 'label_3', 'label_4'], axis=1)
    features = np.array(features)
    train_features, test_features, train_labels, test_labels= train_test_split(features, labels, test_size=test_size)
    scaler = StandardScaler()
    scaler.fit(train_features)
    train_features = scaler.transform(train_features)
    test_features = scaler.transform(test_features)
    classifier = KNeighborsClassifier(n_neighbors=num_of_neighbors)
    classifier.fit(train_features, train_labels)
    predictions = classifier.predict(test_features)

    print("Train Accuracy:", metrics.accuracy_score(train_labels, classifier.predict(train_features)))
    print("Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))


def run_knn_video(test_size, num_of_neighbors):
    features = pd.read_csv('C:\\QOE\\Src\\bins_breaker.csv')
    print("video ", (features['label'] == 'video').sum(), "unknown ",
          (features['label'] != 'video').sum())

    features = features.drop(['sni', 'filter', 'source_file', 'Unnamed: 0'], axis=1)
    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    labels = np.array(features[['label_unknown', 'label_video']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_unknown', 'label_video'], axis=1)
    cols = features.columns
    features = np.array(features)
    train_features, test_features, train_labels, test_labels= train_test_split(features, labels, test_size=test_size)
    scaler = StandardScaler()
    scaler.fit(train_features)
    train_features = scaler.transform(train_features)
    test_features = scaler.transform(test_features)
    classifier = KNeighborsClassifier(n_neighbors=num_of_neighbors)
    classifier.fit(train_features, train_labels)
    predictions = classifier.predict(test_features)

    print("Train Accuracy:", metrics.accuracy_score(train_labels, classifier.predict(train_features)))
    print("Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))



def run_knn_app(test_size, num_of_neighbors):
    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies
    features = pd.read_csv('C:\\QOE\\Src\\bins_breaker.csv')

    print(features.groupby('label').count())

    features = features.drop(['sni', 'filter', 'source_file', 'Unnamed: 0'], axis=1)
    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    labels = np.array(features[['label_unknown', 'label_Netflix', 'label_FaceBook',
                                'label_YouTube', 'label_Instagram', 'label_OtherOTT']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_unknown', 'label_Netflix', 'label_FaceBook',
                              'label_YouTube', 'label_Instagram', 'label_OtherOTT'], axis=1)
    cols = features.columns
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=test_size)
    scaler = StandardScaler()
    scaler.fit(train_features)
    train_features = scaler.transform(train_features)
    test_features = scaler.transform(test_features)
    classifier = KNeighborsClassifier(n_neighbors=num_of_neighbors)
    classifier.fit(train_features, train_labels)
    # Train the model on training data
    classifier.fit(train_features, train_labels)
    predictions = classifier.predict(test_features)
    # Calculate the absolute errors
    errors = abs(predictions - test_labels)

    print("Train Accuracy:", metrics.accuracy_score(train_labels, classifier.predict(train_features)))
    print("Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))


if __name__ == '__main__':
    run_knn_quality(0.3, 1)