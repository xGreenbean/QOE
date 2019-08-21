import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import datetime
import matplotlib.pyplot as plt

from configs import conf
"""
Random Forest regression algorithm each row of feature based on full session,flow up and down
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_rfr_quality(test_size, num_trees, rs_test_train, rs_regressor, classifier_features=[], classifier_labels=[]):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies

    features = pd.read_csv('C:\\QOE\\Src\\generators\\test2_peaks_bins3_filter3000.csv')

    features = features.drop(['filter', 'source_file'], axis=1)
    features = features.sample(frac=1)
    features['label'] = features['label'].astype(str)
    features = pd.get_dummies(features)


    # Labels are the values we want to predict

    labels = np.array(features[['label_1', 'label_2', 'label_3', 'label_4']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_1', 'label_2','label_3', 'label_4'], axis=1)

    cols = features.columns
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=test_size,
                                                                                random_state=rs_test_train)
    rf = RandomForestClassifier(n_estimators=num_trees, random_state=rs_regressor)

    # Train the model on training data
    rf.fit(train_features, train_labels)
    if len(classifier_features) != 0:
        test_features = classifier_features
        test_labels = classifier_labels

    start_test = datetime.datetime.now()
    predictions = rf.predict(test_features)
    print("Done testing in", datetime.datetime.now() - start_test, "seconds")
    # Calculate the absolute errors

    print("Train Accuracy:", metrics.accuracy_score(train_labels, rf.predict(train_features)))
    print("Test Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))

    feature_importances = pd.DataFrame(rf.feature_importances_,
                                       index=cols,
                                       columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)
    return predictions


def run_rfr_video(test_size, num_trees, rs_test_train, rs_regressor, classifier_features=[], classifier_labels=[]):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies

    features = pd.read_csv('C:\\QOE\\Src\\sess_breaker_t3.csv')
    print("video ",(features['label'] == 'video').sum(),"unknown ",
          (features['label'] != 'video').sum())

    features = features.drop(['sni','filter','source_file', 'Unnamed: 0'], axis=1)
    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    labels = np.array(features[['label_unknown','label_video']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_unknown','label_video'], axis=1)
    cols = features.columns
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=test_size,
                                                                                random_state=rs_test_train)
    rf = RandomForestClassifier(n_estimators=num_trees, random_state=rs_regressor)

    # Train the model on training data
    rf.fit(train_features, train_labels)
    if len(classifier_features) != 0:
        test_features = classifier_features
        test_labels = classifier_labels

    predictions = rf.predict(test_features)
    # Calculate the absolute errors
    errors = abs(predictions - test_labels)


    print("Train Accuracy:", metrics.accuracy_score(train_labels, rf.predict(train_features)))
    print("Test Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))

    feature_importances = pd.DataFrame(rf.feature_importances_,
                                       index=cols,
                                       columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)
    return predictions


def run_rfr_app(test_size, num_trees, rs_test_train, rs_regressor):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies
    features = pd.read_csv('/home/ehud/Desktop/QOE/src/generators/bins.csv')

    print(features.groupby('label').count())
    features = features.drop(['sni','filter','source_file', 'Unnamed: 0'], axis=1)
    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    labels = np.array(features[['label_unknown','label_Netflix', 'label_FaceBook',
                                'label_YouTube', 'label_Instagram', 'label_OtherOTT']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_unknown','label_Netflix', 'label_FaceBook',
                                'label_YouTube', 'label_Instagram', 'label_OtherOTT'], axis=1)
    cols = features.columns
    features = np.array(features)

    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=test_size,
                                                                                random_state=rs_test_train)
    rf = RandomForestClassifier(n_estimators=num_trees, random_state=rs_regressor)

    # Train the model on training data
    rf.fit(train_features, train_labels)
    predictions = rf.predict(test_features)
    # Calculate the absolute errors
    errors = abs(predictions - test_labels)

    print("Train Accuracy:", metrics.accuracy_score(train_labels, rf.predict(train_features)))
    print("Accuracy:", metrics.accuracy_score(predictions, test_labels))
    print(" Confusion matrix\n", confusion_matrix(test_labels.argmax(axis=1), predictions.argmax(axis=1)))

    feature_importances = pd.DataFrame(rf.feature_importances_,
                                       index=cols,
                                       columns=['importance']).sort_values('importance', ascending=False)
    print(feature_importances)


if __name__ == '__main__':
    # 1156 41 42
    run_rfr_quality(0.30, 1156, 49,53)