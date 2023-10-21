# Importing the Keras libraries and packages
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense, Dropout
import os


sz = 128
# Step 1 - Building the CNN

# Initializing the CNN
classifier = Sequential()

# First convolution layer and pooling
classifier.add(Convolution2D(64, (3, 3), input_shape=(sz, sz, 1), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Second convolution layer and pooling
classifier.add(Convolution2D(64, (3, 3), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# third convolution layer and pooling
classifier.add(Convolution2D(64, (3, 3), activation="relu"))
classifier.add(MaxPooling2D(pool_size=(2, 2)))

# If needed.....
# fourth convolution layer and pooling
#classifier.add(Convolution2D(32, (3, 3), activation='relu'))
#classifier.add(MaxPooling2D(pool_size=(2, 2)))

# Flattening the layers
classifier.add(Flatten())

# Adding a fully connected layer

# classifier.add(Dense(units=128, activation='relu'))
# classifier.add(Dropout(0.5))

classifier.add(Dense(units=128, activation="relu"))
classifier.add(Dropout(0.5))

#classifier.add(Dense(units=36, activation="relu"))
#classifier.add(Dropout(0.5))

# softmax for more than 2 outputs neuron
classifier.add(Dense(units=36, activation="softmax"))

# Compiling the CNN
classifier.compile(
    optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"]
)  # categorical_crossentropy for more than 2


# Step 2 - Preparing the train/test data and training the model
classifier.summary()

train_datagen = ImageDataGenerator(
    rescale=1.0 / 255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True
)

test_datagen = ImageDataGenerator(rescale=1.0 / 255)

training_set = train_datagen.flow_from_directory(
    "myProcessdata/train",
    target_size=(sz, sz),
    batch_size=1,
    color_mode="grayscale",
    class_mode="categorical",
)

test_set = test_datagen.flow_from_directory(
    "myProcessData/test",
    target_size=(sz, sz),
    batch_size=1,
    color_mode="grayscale",
    class_mode="categorical",
)
classifier.fit(
    training_set,
    steps_per_epoch=5040,  # No of images in training set
    epochs=5,
    validation_data=test_set,
    validation_steps=2160,
)  # No of images in test set


# Saving the model
model_json = classifier.to_json()
with open("model_az.json", "w") as json_file:
    json_file.write(model_json)
print("Model Saved")
classifier.save_weights("model_az.h5")
print("Model saved")
