
# Stellar Classification Using Machine Learning


This project involves the classification of astronomical objects such as stars, galaxies, and quasars based on their spectral characteristics using the Sloan Digital Sky Survey DR17 dataset. Various machine learning models were trained and evaluated, including Random Forest, K-Nearest Neighbors, and Decision Tree, to determine the best model for accurate classification.

## Dataset

The dataset used for this project is the Stellar Classification Dataset - SDSS17, available on Kaggle. The dataset consists of 100,000 observations, each described by 17 feature columns and 1 target column (class), which indicates whether the object is a star, galaxy, or quasar.
https://www.kaggle.com/datasets/fedesoriano/stellar-classification-dataset-sdss17

### Dataset Attributes

* obj_ID: Object Identifier, the unique value that identifies the object in the image catalog used by the CAS.
* alpha: Right Ascension angle (at J2000 epoch).
* delta: Declination angle (at J2000 epoch).
* u: Ultraviolet filter in the photometric system.
* g: Green filter in the photometric system.
* r: Red filter in the photometric system.
* i: Near Infrared filter in the photometric system.
* z: Infrared filter in the photometric system.
* run_ID: Run Number used to identify the specific scan.
* rereun_ID: Rerun Number to specify how the image was processed.
* cam_col: Camera column to identify the scanline within the run.
* field_ID: Field number to identify each field.
* spec_obj_ID: Unique ID used for optical spectroscopic objects (two different observations with the same spec_obj_ID must share the same output class).
* class: Object class (galaxy, star, or quasar).
* redshift: Redshift value based on the increase in wavelength.
* plate: Plate ID, identifies each plate in SDSS.
* MJD: Modified Julian Date, used to indicate when a given piece of SDSS data was taken.
* fiber_ID: Fiber ID that identifies the fiber that pointed the  light at the focal plane in each observatio

# Project Structure

## Data Preprocessing:

* The dataset was loaded and inspected for any missing values.
* The target variable was set to the class column, and features were prepared for model training.

## Model Training:

### Random Forest:
 A RandomForestClassifier with 100 estimators and a random state of 42 was used.
Accuracy: 0.98
Classification Report:
               precision    recall  f1-score   support

      GALAXY       0.98      0.99      0.98     17845
         QSO       0.97      0.93      0.95      5700
        STAR       0.99      1.00      1.00      6455




accuracy                           0.98     30000

macro avg       0.98      0.97      0.98     30000
weighted avg       0.98      0.98      0.98     30000

Confusion Matrix:
 [[17601   188    56]
 [  398  5301     1]
 [    2     0  6453]]
### K-Nearest Neighbors (KNN): 
KNeighborsClassifier with 5 neighbors was employed.

Accuracy: 0.70
Classification Report:
               precision    recall  f1-score   support

      GALAXY       0.74      0.89      0.81     17845
         QSO       0.50      0.39      0.44      5700
        STAR       0.76      0.47      0.58      6455

    accuracy                           0.70     30000
   macro avg       0.66      0.58      0.61     30000
weighted avg       0.70      0.70      0.69     30000

Confusion Matrix:
 [[15887  1402   556]
 [ 3097  2221   382]
 [ 2598   853  3004]]

### Decision Tree: 
 DecisionTreeClassifier with a random state of 42 was used.



Accuracy: 0.96
Classification Report:
               precision    recall  f1-score   support

      GALAXY       0.97      0.97      0.97     17845
         QSO       0.91      0.91      0.91      5700
        STAR       1.00      1.00      1.00      6455

    accuracy                           0.96     30000
   macro avg       0.96      0.96      0.96     30000
weighted avg       0.96      0.96      0.96     30000

Confusion Matrix:
 [[17299   518    28]
 [  503  5197     0]
 [   23     0  6432]]


## Model Evaluation:
![bar graph](https://github.com/NIRANJANA-03/STELLAR-CLASSIFICATION/blob/main/model%20training/evaluation%20of%20different%20model.png)
## Model Deployment:

The Random Forest model, which provided the best accuracy, was saved using joblib and a GUI was created using Tkinter for real-time classification of astronomical objects based on user input

![bar graph](https://github.com/NIRANJANA-03/STELLAR-CLASSIFICATION/blob/main/model%20training/deployment.png)
