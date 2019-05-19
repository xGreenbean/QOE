import numpy as np
import pandas as pd
from Configs import conf

"""
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 

"""


def draw_features():
    frames = []
    for device in conf.Devices:
        for ott in conf.Otts:
            for i in range(conf.numbers_of_id):
                df = pd.read_csv(
                    "C:\\Users\\Saimon\\Desktop\\dataset\\" + device + "_" + ott + "\\Id_" + str(
                        i + 1) + "\\" + device + "_" + ott + "_"+conf.feature_type+"_features_" + str(
                        i + 1) + ".csv")
                frames.append(df)
    print("Done Reading")
    result = pd.concat(frames)
    return result


def run_rfr():
    # Read in data and display first 5 rows
    features = draw_features()

#   only for video/no video, for app remove
    features = features.replace({"Label":{0: 2, 1: 3}})
    # One-hot encode the data using pandas get_dummies
    features = features.sample(frac=1)
    features = pd.get_dummies(features)

    # Labels are the values we want to predict
    labels = np.array(features['Label'])
    # Remove the labels from the features
    # axis 1 refers to the columns
    features= features.drop('Label', axis = 1)

    # Saving feature names for later use
    feature_list = list(features.columns)
    # Convert to numpy array
    features = np.array(features)

    # Using Skicit-learn to split data into training and testing sets
    from sklearn.model_selection import train_test_split
    # Split the data into training and testing sets
    train_features, test_features, train_labels, test_labels = train_test_split(features, labels, test_size = 0.25, random_state = 41)

    from sklearn.ensemble import RandomForestRegressor
    # Instantiate model with 1000 decision trees
    # 0.2 1493 52 47 = 98.75
    # 0.3 1233 42 49 98.13
    rf = RandomForestRegressor(n_estimators = 1256, random_state = 42)
    # Train the model on training data
    rf.fit(train_features, train_labels)
    predictions = rf.predict(test_features)
    # Calculate the absolute errors
    errors = abs(predictions - test_labels)
    # Print out the mean absolute error (mae)
    print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')
    mape = 100 * (errors / (test_labels))
    # Calculate and display accuracy
    accuracy = 100 - np.mean(mape)
    print('Accuracy:', round(accuracy, 2), '%.')

run_rfr()