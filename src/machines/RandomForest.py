import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

from configs import conf
"""
Random Forest regression algorithm each row of feature based on full session,flow up and down
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_rfr_video(test_size, num_trees, rs_test_train, rs_regressor):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies
<<<<<<< HEAD:Src/machines/RandomForest.py
    features = pd.read_csv('C:\\QOE\\Src\\bins_breaker.csv')

=======
    features = pd.read_csv('/home/ehud/Desktop/QOE/src/bins_breaker.csv')
    for index,row in features.iterrows():
        print(row)
>>>>>>> 2666c4218e22d9a8c75f2e89a8db89ee6d4a0f79:src/machines/RandomForest.py
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

def run_rfr_app(test_size, num_trees, rs_test_train, rs_regressor):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies
    features = pd.read_csv('/home/ehud/Desktop/QOE/src/generators/bins.csv')

<<<<<<< HEAD:Src/machines/RandomForest.py
    print(features.groupby('label').count()
)
=======
    print(features.groupby('label').count())
>>>>>>> 2666c4218e22d9a8c75f2e89a8db89ee6d4a0f79:src/machines/RandomForest.py

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
    run_rfr_video(0.30, 1256, 41, 42)