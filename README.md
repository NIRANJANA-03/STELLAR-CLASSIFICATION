#Stellar Classification Using Machine Learning

This project involves the classification of astronomical objects such as stars, galaxies, and quasars based on their spectral characteristics using the Sloan Digital Sky Survey DR17 dataset. Various machine learning models were trained and evaluated, including Random Forest, K-Nearest Neighbors, and Decision Tree, to determine the best model for accurate classification.
Dataset

The dataset used for this project is the Stellar Classification Dataset - SDSS17, available on Kaggle. The dataset consists of 100,000 observations, each described by 17 feature columns and 1 target column (class), which indicates whether the object is a star, galaxy, or quasar.
Dataset Attributes

* obj_ID: Object Identifier, the unique value that identifies the object in the image catalog used by the CAS.
    alpha: Right Ascension angle (at J2000 epoch).
    delta: Declination angle (at J2000 epoch).
    u: Ultraviolet filter in the photometric system.
    g: Green filter in the photometric system.
    r: Red filter in the photometric system.
    i: Near Infrared filter in the photometric system.
    z: Infrared filter in the photometric system.
    run_ID: Run Number used to identify the specific scan.
    rereun_ID: Rerun Number to specify how the image was processed.
    cam_col: Camera column to identify the scanline within the run.
    field_ID: Field number to identify each field.
    spec_obj_ID: Unique ID used for optical spectroscopic objects (two different observations with the same spec_obj_ID must share the same output class).
    class: Object class (galaxy, star, or quasar).
    redshift: Redshift value based on the increase in wavelength.
    plate: Plate ID, identifies each plate in SDSS.
    MJD: Modified Julian Date, used to indicate when a given piece of SDSS data was taken.
    fiber_ID: Fiber ID that identifies the fiber that pointed the light at the focal plane in each observation.

Project Structure

The project is structured into several key components:
Data Preprocessing

    The dataset was loaded and inspected for any missing values.
    The target variable was set to the class column, and features were prepared for model training.

Model Training

Three machine learning models were trained and evaluated:

    Random Forest: A RandomForestClassifier with 100 estimators and a random state of 42 was used.
    K-Nearest Neighbors (KNN): KNeighborsClassifier with 5 neighbors was employed.
    Decision Tree: DecisionTreeClassifier with a random state of 42 was used.

The models were trained using a 70-30 train-test split.
Model Evaluation

    Models were evaluated based on accuracy, precision, and F1-Score.
    A comparison of the models' performance was plotted to visualize the results.

Model Deployment

The Random Forest model, which provided the best accuracy, was saved using joblib. A GUI was created using Tkinter for real-time classification of astronomical objects based on user input.
