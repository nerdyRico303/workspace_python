import numpy as np
import matplotlib.pyplot as plt
import data_prep # external file
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from tensorflow.keras.models import Sequential # we are building MLP using Sequences of NN's
from tensorflow.keras.layers import Dense
from sklearn.decomposition import PCA


    ## Section 1: file initialization ##

# initializing path (note: Path need to be change to your current system file)
dimension = 250*250
train_noncovid = data_prep.pic_loader('C:/Users/Enric/Desktop/coursework/courseworkdata/CT_NonCOVID',
                                         'C:/Users/Enric/Desktop/coursework/courseworkdata/Data-split/NonCOVID/trainCT_NonCOVID.txt', 0)
test_noncovid = data_prep.pic_loader('C:/Users/Enric/Desktop/coursework/courseworkdata/CT_NonCOVID',
                                        'C:/Users/Enric/Desktop/coursework/courseworkdata/Data-split/NonCOVID/testCT_NonCOVID.txt', 0)
val_noncovid = data_prep.pic_loader('C:/Users/Enric/Desktop/coursework/courseworkdata/CT_NonCOVID',
                                       'C:/Users/Enric/Desktop/coursework/courseworkdata/Data-split/NonCOVID/valCT_NonCOVID.txt', 0)
train_covid = data_prep.pic_loader('C:/Users/Enric/Desktop/coursework/courseworkdata/CT_COVID',
                                      'C:/Users/Enric/Desktop/coursework/courseworkdata/Data-split/COVID/trainCT_COVID.txt', 1)
test_covid = data_prep.pic_loader('C:/Users/Enric/Desktop/coursework/courseworkdata/CT_COVID',
                                     'C:/Users/Enric/Desktop/coursework/courseworkdata/Data-split/COVID/testCT_COVID.txt', 1)
val_covid = data_prep.pic_loader('C:/Users/Enric/Desktop/coursework/courseworkdata/CT_COVID',
                                    'C:/Users/Enric/Desktop/coursework/courseworkdata/Data-split/COVID/valCT_COVID.txt', 1)
train_noncovid_full = np.append(train_noncovid, test_noncovid, axis=0)
train_noncovid_full = np.append(train_noncovid_full, val_noncovid, axis=0)  # 397 Non-COVID samples in total
train_covid_full = np.append(train_covid, test_covid, axis=0)
train_covid_full = np.append(train_covid_full, val_covid, axis=0)  # 349 COVID samples in total
X = np.append(train_noncovid_full, train_covid_full, axis=0)
X = X / 255 # normalization (change to range 0<x<1)

# labeling each variable (noncov = 0; cov = 1)
y_noncovid = np.zeros(len(train_noncovid_full))
y_covid = np.ones(len(train_covid_full))

y = np.append(y_noncovid, y_covid)


    ## Section 1.5: Applying PCA ##

#---------- ATTENTION: Toggle the section below using (Ctrl + '/') to apply pca ----------#

dimension = 20 # You can manually set the number of dimensions
pca = PCA(n_components = dimension)
X = pca.fit_transform(X)

#-----------------------------------------------------------------------------------------#


    ## Section 2: Building the Machine Learning Model ##

# splitting the combined data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

# MLP model ("Multi-Layer Perceptron" by my understanding is combining multiple layer type of classification)
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(dimension,)))  # Input layer
model.add(Dense(256, activation='relu'))  # Hidden layer 1
model.add(Dense(128, activation='relu'))  # Hidden layer 2
model.add(Dense(64, activation='relu'))   # Hidden layer 3
model.add(Dense(1, activation='sigmoid')) # Output layer (for binary classification)

# model Compiler
model.compile(optimizer='adam', 
              loss='binary_crossentropy', 
              metrics=['accuracy'])


    ## Section 3: Training and Testing ##

# training
history = model.fit(X_train, y_train, epochs=25, batch_size=32, validation_split=0.2)
# testing
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"Test Accuracy: {test_acc:.4f}")
y_pred = (model.predict(X_test) > 0.5).astype("int32")


    ## Section 4: Result Representation ##

# print classification report and accuracy
# print("Classification Report:\n", classification_report(y_test, y_pred))

# # (Graphical Purposes) Plot training accuracy and loss history
# plt.plot(history.history['accuracy'], label='Training Accuracy')
# plt.plot(history.history['val_accuracy'], label='Validation Accuracy')
# plt.title('Training and Validation Accuracy')
# plt.legend()
# plt.show()

# plt.plot(history.history['loss'], label='Training Loss')
# plt.plot(history.history['val_loss'], label='Validation Loss')
# plt.title('Training and Validation Loss')
# plt.legend()
# plt.show()