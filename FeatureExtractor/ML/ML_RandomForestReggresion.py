import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pandas as pd
from ML.DrawFeatures import draw_features
from Configs import conf
"""
Random Forest regression algorithm each row of feature based on full session,flow up and down
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_rfr(test_size, num_trees, rs_test_train, rs_regressor):
    # Read in data and display first 5 rows
    features = draw_features()

    #   only for video/no video, for app remove
    if conf.feature_type == "video":
        features = features.replace({"Label": {0: 2, 1: 3}})
    # One-hot encode the data using pandas get_dummies
    features = features.sample(frac=1)
    features = pd.get_dummies(features)

    # Labels are the values we want to predict
    labels = np.array(features['Label'])
    # Remove the labels from the features
    # axis 1 refers to the columns
    features = features.drop('Label', axis=1)
    # Convert to numpy array
    features = np.array(features)
    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size=test_size,
                                                                                random_state=rs_test_train)
    # Instantiate model with 1000 decision trees
    # 0.2 1493 52 47 = 98.75
    # 0.3 1233 42 49 98.13
    rf = RandomForestRegressor(n_estimators=num_trees, random_state=rs_regressor)
    # Train the model on training data
    rf.fit(train_features, train_labels)
    predictions = rf.predict(test_features)
    # Calculate the absolute errors
    errors = abs(predictions - test_labels)
    # Print out the mean absolute error (mae)
    print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    mape = 100 * (errors / test_labels)
    # Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')


if __name__ == '__main__':
    run_rfr(0.25, 1256, 41, 42)
