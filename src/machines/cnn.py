import numpy as np
import keras
import keras.layers as layers
from sklearn.metrics import classification_report
import pickle
from sklearn.preprocessing import LabelEncoder
from keras.layers import Dropout


def pickle_image_generator(input_path, bs, lb, mode="train", aug=None):
    with open(input_path, 'rb') as handle:
        b = pickle.load(handle)
        np.random.shuffle(b)
        it = iter(b)
        while True:
            # initialize our batches of images and labels
            features = []
            labels = []
            # keep looping until we reach our batch size
            while len(features) < bs:
                # attempt to read the next line of the CSV file
                try:
                    curr_dict = it.__next__()
                except StopIteration:
                    it = iter(b)
                    if mode == "eval":
                        break

                label = curr_dict['videolabel']

                arr = np.zeros(1500 * 1500, dtype="uint8")
                for key, value in curr_dict.items():
                    if 'label' not in str(key):
                        arr[key] = value

                arr = arr.reshape((1500, 1500))
                # update our corresponding batches lists
                features.append(arr.reshape(1500, 1500, 1))
                labels.append(label)
            labels = lb.transform(np.array(labels))
            yield (np.array(features), labels)


def cnn():
    num_clasess = 1
    labels = ['video', 'novideo']
    # initialize the paths to our training and testing CSV files
    TRAIN_PICKLE = "/home/cyberlab/Desktop/QOE/src/tools/train.pickle"
    TEST_PICKLE = "/home/cyberlab/Desktop/QOE/src/tools/test.pickle"
    testLabels = []

    # initialize the number of epochs to train for and batch size
    NUM_EPOCHS = 75
    BS = 32

    # initialize the total number of training and testing image
    NUM_TRAIN_IMAGES = 0
    NUM_TEST_IMAGES = 0

    # open the training CSV file, then initialize the unique set of class
    # labels in the dataset along with the testing labels
    with open(TRAIN_PICKLE, 'rb') as handle:
        b = pickle.load(handle)
        NUM_TRAIN_IMAGES = len(b)

    with open(TEST_PICKLE, 'rb') as handle:
        b = pickle.load(handle)
        NUM_TEST_IMAGES = len(b)
        for curr_dict in b:
            testLabels.append(curr_dict['videolabel'])

    lb = LabelEncoder()
    lb.fit(labels)
    testLabels = lb.transform(testLabels)
    # initialize both the training and testing image generators
    trainGen = pickle_image_generator(TRAIN_PICKLE, BS, lb,
                                      mode="train", aug=None)
    testGen = pickle_image_generator(TEST_PICKLE, BS, lb,
                                     mode="train", aug=None)

    model = keras.Sequential()

    model.add(layers.Conv2D(filters=10, kernel_size=(10, 10), strides=5,
                            activation='relu', input_shape=(1500, 1500, 1)))
    model.add(layers.MaxPooling2D())
    model.add(Dropout(0.1))
    model.add(layers.Conv2D(filters=20, kernel_size=(10, 10), strides=5,
                            activation='relu'))
    model.add(layers.MaxPooling2D())
    model.add(Dropout(0.1))
    model.add(layers.Flatten())
    model.add(layers.Dense(units=64, activation='relu'))
    model.add(layers.Dense(units=64, activation='relu'))
    model.add(layers.Dense(units=num_clasess, activation='sigmoid'))

    model.compile(loss='binary_crossentropy',
                  optimizer=keras.optimizers.Adam(),
                  metrics=['accuracy'])

    H = model.fit_generator(
        trainGen,
        steps_per_epoch=NUM_TRAIN_IMAGES // BS,
        validation_data=testGen,
        validation_steps=NUM_TEST_IMAGES // BS,
        epochs=NUM_EPOCHS)

    # re-initialize our testing data generator, this time for evaluating
    testGen = pickle_image_generator(TEST_PICKLE, BS, lb,
                                     mode="eval", aug=None)

    # make predictions on the testing images, finding the index of the
    # label with the corresponding largest predicted probability
    predIdxs = model.predict_generator(testGen,
                                       steps=(NUM_TEST_IMAGES // BS) + 1)
    # show a nicely formatted classification report
    print("[INFO] evaluating network...")
    print(classification_report(testLabels, (predIdxs > 0.5),
                                target_names=lb.classes_))

cnn()
