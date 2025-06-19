import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.metrics import accuracy_score
from sklearn.decomposition import PCA
import sys
import os
import data_prep 


### With PCA ###


sys.path.append(r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data')
os.chdir(r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata')

    ## Section 1: Load image data ##
train_noncovid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_NonCOVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\NonCOVID\trainCT_NonCOVID.txt', 0)
test_noncovid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_NonCOVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\NonCOVID\testCT_NonCOVID.txt', 0)
val_noncovid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_NonCOVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\NonCOVID\valCT_NonCOVID.txt', 0)
train_covid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_COVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\COVID\trainCT_COVID.txt', 1)
test_covid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_COVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\COVID\testCT_COVID.txt', 1)
val_covid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_COVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\COVID\valCT_COVID.txt', 1)
train_noncovid_full = np.append(train_noncovid, test_noncovid, axis=0)
train_noncovid_full = np.append(train_noncovid_full, val_noncovid, axis=0)  # 397 Non-COVID samples in total
train_covid_full = np.append(train_covid, test_covid, axis=0)
train_covid_full = np.append(train_covid_full, val_covid, axis=0)  # 349 COVID samples in total
X = np.append(train_noncovid_full, train_covid_full, axis=0)
X = X / 255.0  # normalization

# Labeling each variable (noncov = 0; cov = 1)
y_noncovid = np.zeros(len(train_noncovid_full))
y_covid = np.ones(len(train_covid_full))
y = np.append(y_noncovid, y_covid)

    ## Section 2: Apply PCA ##
# We use n =20
pca = PCA(n_components=20)
X_pca = pca.fit_transform(X)

    ## Section 3: Split Data ##
# splitting the combined data into training and test sets
X_train_pca, X_test_pca, y_train, y_test = train_test_split(X_pca, y, test_size=0.5, random_state=42)

    ## Section 4: KNN Classifier ##
# Initialize the KNN classifier with 5 neighbors
knn_pca = KNeighborsClassifier(n_neighbors=5)
knn_pca.fit(X_train_pca, y_train)

    ## Section 5: Printing the results ##
# For train data 
y_train_pred_pca = knn_pca.predict(X_train_pca)
train_accuracy_pca = accuracy_score(y_train, y_train_pred_pca)
print(f"KNN Training Accuracy with PCA: {train_accuracy_pca * 100:.2f}%")

# For test data 
y_test_pred_pca = knn_pca.predict(X_test_pca)
test_accuracy_pca = accuracy_score(y_test, y_test_pred_pca)
print(f"KNN Test Accuracy with PCA: {test_accuracy_pca * 100:.2f}%")



### Without PCA ###


sys.path.append(r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data')
os.chdir(r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata')

    ## Section 1: Load image data ##
train_noncovid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_NonCOVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\NonCOVID\trainCT_NonCOVID.txt', 0)
test_noncovid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_NonCOVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\NonCOVID\testCT_NonCOVID.txt', 0)
val_noncovid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_NonCOVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\NonCOVID\valCT_NonCOVID.txt', 0)
train_covid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_COVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\COVID\trainCT_COVID.txt', 1)
test_covid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_COVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\COVID\testCT_COVID.txt', 1)
val_covid = data_prep.pic_loader(
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\CT_COVID',
    r'C:\Users\ASUS\Documents\Michelle\Avery\Year 3\DTS201\data\courseworkdata\Data-split\COVID\valCT_COVID.txt', 1)
train_noncovid_full = np.append(train_noncovid, test_noncovid, axis=0)
train_noncovid_full = np.append(train_noncovid_full, val_noncovid, axis=0)  # 397 Non-COVID samples in total
train_covid_full = np.append(train_covid, test_covid, axis=0)
train_covid_full = np.append(train_covid_full, val_covid, axis=0)  # 349 COVID samples in total
X = np.append(train_noncovid_full, train_covid_full, axis=0)
X = X / 255.0  # normalization

# Labeling each variable (noncov = 0; cov = 1)
y_noncovid = np.zeros(len(train_noncovid_full))
y_covid = np.ones(len(train_covid_full))

y = np.append(y_noncovid, y_covid)

#splitting the combined data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)

    ## Section 2: KNN Classifier ##
# Initialize the KNN classifier with 5 neighbors
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)

    ## Section 3: Printing the results ##
    
# For train data
y_train_pred = knn.predict(X_train)
train_accuracy = accuracy_score(y_train, y_train_pred)
print(f"KNN Training Accuracy: {train_accuracy * 100:.2f}%")

# For test data
y_test_pred = knn.predict(X_test)
test_accuracy = accuracy_score(y_test, y_test_pred)
print(f"\nKNN Test Accuracy: {test_accuracy * 100:.2f}%")