# Cyber Data Analytics - Lab 1 
###### TU Delft 2017/2018 -- Author: Johanna Korte

For the visualization task, please run [visualization_task.py](visualization_task.py)  
For the imbalance and classification task, please run [Main.py](Main.py) with the desired parameters

## Files

[Main.py](Main.py) - Run classifiers and Smote on data with given parameters  
[preprocess.py](preprocess.py) - Preprocesses the data such that it can be used by the classifiers  
[crossvalidation.py](crossvalidation.py) - Coordinates k-fold crossvalidation  
[SMOTE.py](SMOTE.py) - Applies Synthetic Minority Over-sampling Technique if specified in main  
[classifiers.py](classifiers.py) - Contains the code for training all classifiers  
[ROC.py](ROC.py) - Given the prediction on test data, form ROC curves and print statistics  
[visualization_task.py](visualization_task.py) - Given the data, return the visualization as described in the visualization task of the report