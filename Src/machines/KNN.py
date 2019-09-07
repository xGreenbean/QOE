import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
from sklearn.neighbors import KNeighborsClassifier
from configs import conf
"""
K nearest neighbors algorithm for guessing app and video/non video per session
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_knn_quality(test_size, num_of_neighbors):
    features = pd.read_csv('C:\\QOE\\Src\\test_quality_breaker_up_down_all.csv')
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

    features = features.drop(['filter', 'source_file', 'Unnamed: 0'], axis=1)
    #features = features.drop(transport, axis=1)
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
    features = pd.read_csv('C:\\QOE\\Src\\video_bin3_break.csv')
    print("video ",(features['label'] == 'video').sum(),"unknown ",
          (features['label'] != 'video').sum())

    features = features.drop(['sni','filter','source_file', 'Unnamed: 0'], axis=1)
    features = features[pd.notnull(features['f_size_var'])]
    header_first = ["f_packet_count", "f_min_packet_size", "f_max_packet_size",
                    "f_mean_packet_size", "f_std_packet_size", "f_size_var", "f_max_time_delta",
                    "f_std_time_delta", "f_min_time_delta", "f_mean_time_delta"]
    features = features.drop(header_first, axis=1)
    #features = features.drop(conf.header_peak, axis=1)

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
    features = pd.read_csv('C:\\QOE\\Src\\app_bin5_break_new_agg_0.03.csv')
    features = features[pd.notnull(features['f_size_var'])]
    print(features.groupby('label').count())

    features = features.drop(['sni', 'filter', 'source_file', 'Unnamed: 0'], axis=1)

    header_peak = ["p_max_element_size", "p_min_element_size", "p_mean_element_size", "p_max_silence_time",
                   "p_min_silence_time", "p_mean_silence_time", "p_std_silence_time",
                   "p_element_count", "p_max_element_length",
                   "p_min_element_length", "p_std_element_length", "p_mean_element_length"]

    header_break = ["b_max_element_size", "b_min_element_size", "b_mean_element_size",
                    "b_std_element_size", "b_max_silence_time",
                    "b_min_silence_time", "b_mean_silence_time", "b_std_silence_time",
                    "b_element_count", "b_max_element_length",
                    "b_min_element_length", "b_std_element_length", "b_mean_element_length"]

    #features = features.drop(header_break, axis=1)
    #features = features.drop(header_peak, axis=1)

    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    header_first = ["f_packet_count", "f_min_packet_size", "f_max_packet_size",
                    "f_mean_packet_size", "f_std_packet_size", "f_size_var", "f_max_time_delta",
                    "f_std_time_delta", "f_min_time_delta", "f_mean_time_delta", "f_duration", "f_packets_size",
                    "f_upstream_mean_ttl",
                    "f_size_histogram"]

    features = features.drop(header_first, axis=1)

    labels = np.array(features[['label_unknown', 'label_Netflix', 'label_FaceBook',
                                'label_YouTube', 'label_OtherOTT']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_unknown', 'label_Netflix', 'label_FaceBook',
                              'label_YouTube', 'label_OtherOTT'], axis=1)
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


def run_knn_os(test_size, num_of_neighbors):
    features = pd.read_csv('C:\\QOE\\Src\\sess_os_all.csv')
    print("iphone ",(features['label'] == 1).sum(),"android ",
          (features['label'] != 1).sum())
    features['label'] = features['label'].astype(str)
    features = features.drop(['sni','filter','source_file', 'Unnamed: 0'], axis=1)
    #features = features[pd.notnull(features['f_size_var'])]

    features = features.sample(frac=1)
    features = pd.get_dummies(features)
    # Labels are the values we want to predict

    labels = np.array(features[['label_1', 'label_2']])
    # Remove the labels from the features
    # axis 1 refers to the columns
    # Convert to numpy array
    features = features.drop(['label_1','label_2'], axis=1)
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

if __name__ == '__main__':
    run_knn_quality(0.3, 3)

    # Big Packet 55 net:53 tran:52
    # Peaks 64 net:63 tran: 63
    # Breaker 63 net:57 tran: 58