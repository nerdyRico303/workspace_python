import numpy as np
import data_prep # external file
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from sklearn.naive_bayes import GaussianNB
from sklearn.decomposition import PCA


    ## Section 1: file initialization ##

#initializing path (note: Path need to be change to your current system file)
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

# dimension = 20 # You can manually set the number of dimensions
# pca = PCA(n_components = dimension)
# X = pca.fit_transform(X)

#-----------------------------------------------------------------------------------------#


    ## Section 2: Building the Machine Learning Model ##

# splitting the combined data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
# Embedding the Naive-Bayes model in the variable "model"
model = GaussianNB()


    ## Section 3: Training and Testing ##

# training
model.fit(X_train, y_train)
# testing
model_test = model.predict(X_test)
accuracy = accuracy_score(y_test, model_test)


    ## Section 4: Evaluation ##

print(f"Accuracy: {accuracy * 100:.2f}%")
print("Classification Report:")
print(classification_report(y_test, model_test))


