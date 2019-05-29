import pandas as pd
import numpy as np
from ML.DrawFeatures import draw_features
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

"""
K nearest neighbors algorithm for guessing app and video/non video per session
Works for both app predicting and video/non video classifying 
Need upgrade this in this section 
"""


def run_knn(test_size, num_of_neighbors):
    dataset = draw_features()
    dataset = pd.get_dummies(dataset)
    y = np.array(dataset['Label'])
    x = dataset.drop('Label', axis=1)
    x = np.array(x)
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=test_size)
    scaler = StandardScaler()
    scaler.fit(x_train)
    x_train = scaler.transform(x_train)
    x_test = scaler.transform(x_test)
    classifier = KNeighborsClassifier(n_neighbors=num_of_neighbors)
    classifier.fit(x_train, y_train)
    y_pred = classifier.predict(x_test)
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))


if __name__ == '__main__':
    run_knn(0.3, 1)
