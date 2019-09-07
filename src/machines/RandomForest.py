import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier,RandomForestRegressor
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

    features = pd.read_csv('C:\\QOE\\Src\\test_quality_peaks_up_down_all.csv')
    features = features[pd.notnull(features['up_duration'])]

    network = ["up_packet_count", "up_min_packet_size", "up_max_packet_size",
                          "up_mean_packet_size", "up_std_packet_size", "up_size_var", "up_max_time_delta",
                          "up_std_time_delta",
                          "up_min_time_delta", "up_var_time_delta", "up_mean_time_delta", "up_duration",
                          "up_packets_size", "up_upstream_mean_ttl",
                          "up_size_histogram",
                          "d_packet_count", "d_min_packet_size", "d_max_packet_size",
                          "d_mean_packet_size", "d_std_packet_size", "d_size_var", "d_max_time_delta",
                          "d_std_time_delta",
                          "d_min_time_delta", "d_var_time_delta", "d_mean_time_delta", "duration", "d_packets_size",
                          "d_upstream_mean_ttl",
                          "d_size_histogram",
               "packet_count", "min_packet_size", "max_packet_size",
               "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
               "min_time_delta", "var_time_delta", "mean_time_delta", "duration", "packets_size",
               "upstream_mean_ttl",
               "size_histogram"]

    transport = ["up_tran_len_sum", "up_tran_len_max", "up_tran_len_min",
                          "up_tran_len_mean", "up_tran_len_std", "up_tran_len_var",
                          "up_tran_time_relative_sum", "up_tran_time_relative_max", "up_tran_time_relative_min",
                          "up_tran_time_relative_mean", "up_tran_time_relative_std", "up_tran_time_relative_var",
                          "up_tran_time_delta_sum", "up_tran_time_delta_max", "up_tran_time_delta_min",
                          "up_tran_time_delta_mean", "up_tran_time_delta_std", "up_tran_time_delta_var",
            "d_tran_len_sum", "d_tran_len_max", "d_tran_len_min", "d_tran_len_mean",
            "d_tran_len_std", "d_tran_len_var",
            "d_tran_time_relative_sum", "d_tran_time_relative_max", "d_tran_time_relative_min",
            "d_tran_time_relative_mean", "d_tran_time_relative_std", "d_tran_time_relative_var",
            "d_tran_time_delta_sum", "d_tran_time_delta_max", "d_tran_time_delta_min",
            "d_tran_time_delta_mean", "d_tran_time_delta_std", "d_tran_time_delta_var",
            "tran_len_sum", "tran_len_max", "tran_len_min", "tran_len_mean",
            "tran_len_std", "tran_len_var",
            "tran_time_relative_sum", "tran_time_relative_max", "tran_time_relative_min",
            "tran_time_relative_mean", "tran_time_relative_std", "tran_time_relative_var",
            "tran_time_delta_sum", "tran_time_delta_max", "tran_time_delta_min",
            "tran_time_delta_mean", "tran_time_delta_std", "tran_time_delta_var"]


    ia = ["d_max_packet_size","d_upstream_mean_ttl",
    "d_tran_len_max"]

    features = features.drop(ia, axis=1)

    features = features.drop(['filter', 'source_file', 'Unnamed: 0'], axis=1)

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
    print("video bin3 peak without first")
    features = pd.read_csv('C:\\QOE\\Src\\sess_os_all.csv')
    print("video ", (features['label'] == 'video').sum(),"unknown ",
          (features['label'] != 'video').sum())

    features = features.drop(['sni','filter','source_file', 'Unnamed: 0'], axis=1)
    features = features[pd.notnull(features['f_size_var'])]

    #features = features.drop(header_first, axis=1)
    #features = features.drop(conf.header_peak, axis=1)

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
    features = pd.read_csv('C:\\QOE\\Src\\app_bin5_break_new_agg_0.03.csv')
    print("app_bin3_peak_new_0.05")
    features = features[pd.notnull(features['f_size_var'])]
    print(features.groupby('label').count())
    features = features.drop(['sni','filter','source_file', 'Unnamed: 0'], axis=1)

    header_first = ["f_packet_count", "f_min_packet_size", "f_max_packet_size",
                    "f_mean_packet_size", "f_std_packet_size", "f_size_var", "f_max_time_delta",
                    "f_std_time_delta", "f_min_time_delta", "f_mean_time_delta", "f_duration", "f_packets_size",
                    "f_upstream_mean_ttl",
                    "f_size_histogram"]
    #features = features.drop(conf.header_break, axis=1)
    features = features.drop(header_first, axis=1)

    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    #, 'label_Instagram'
    labels = np.array(features[['label_unknown','label_Netflix', 'label_FaceBook',
                                'label_YouTube', 'label_OtherOTT']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_unknown','label_Netflix', 'label_FaceBook',
                                'label_YouTube', 'label_OtherOTT'], axis=1)
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


def run_rfr_rg_delay(test_size, num_trees, rs_test_train, rs_regressor):
    # Read in data and display first 5 rows
    features = pd.read_csv('C:\\QOE\\Src\\test_delay_Peak.csv')
    # features = features[pd.notnull(features['up_duration'])]

    header_net_tran = ["packet_count", "min_packet_size", "max_packet_size",
                       "mean_packet_size", "std_packet_size", "size_var", "max_time_delta", "std_time_delta",
                       "min_time_delta", "var_time_delta", "mean_time_delta", "duration", "packets_size",
                       "upstream_mean_ttl",
                       "size_histogram", "tran_len_sum", "tran_len_max", "tran_len_min", "tran_len_mean",
                       "tran_len_std", "tran_len_var",
                       "tran_time_relative_sum", "tran_time_relative_max", "tran_time_relative_min",
                       "tran_time_relative_mean", "tran_time_relative_std", "tran_time_relative_var",
                       "tran_time_delta_sum", "tran_time_delta_max", "tran_time_delta_min",
                       "tran_time_delta_mean", "tran_time_delta_std", "tran_time_delta_var"]

    ia = ['up_upstream_mean_ttl',
          'd_max_packet_size',
          'd_tran_len_max',
          'd_upstream_mean_ttl', 'tran_len_max', 'max_packet_size']

    features = features.drop(['filter', 'source_file', 'Unnamed: 0'], axis=1)

    # One-hot encode the data using pandas get_dummies
    features = features.sample(frac=1)
    features = pd.get_dummies(features)

    labels = np.array(features['label'])
    # Remove the labels from the features
    # axis 1 refers to the columns
    features= features.drop('label', axis = 1)

    features = np.array(features)

    from sklearn.ensemble import RandomForestRegressor
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


def run_rfr_delay(test_size, num_trees, rs_test_train, rs_regressor, classifier_features=[], classifier_labels=[]):

    #   only for video/no video, for app remove
    # One-hot encode the data using pandas get_dummies

    features = pd.read_csv('C:\\QOE\\Src\\test_delay_Breaker_classifier.csv')
    #features = features[pd.notnull(features['up_duration'])]


    ia = ['up_upstream_mean_ttl',
    'd_max_packet_size',
    'd_tran_len_max',
    'd_upstream_mean_ttl', 'tran_len_max', 'max_packet_size']

    features = features.drop(['filter', 'source_file', 'Unnamed: 0'], axis=1)
    #features = features.drop(ia, axis=1)
    features = features.sample(frac=1)
    features['label'] = features['label'].astype(str)
    features = pd.get_dummies(features)


    # Labels are the values we want to predict

    labels = np.array(features[['label_1', 'label_2', 'label_3', 'label_4', 'label_5']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_1', 'label_2', 'label_3', 'label_4', 'label_5'], axis=1)

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




if __name__ == '__main__':
    # 1156 41 42
    #579
    #quality 1289 ,41,42 (0.3, 2139, 41, 42) (1539, 41, 42)
    run_rfr_quality(0.3, 1156, 41, 42)

    # all: 56 network:58 tran:55
    # breaker all: 62 network:61 tran:64
    # peaks :all: 66 network:64 tran:65
