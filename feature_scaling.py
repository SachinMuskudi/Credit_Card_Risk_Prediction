import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
import logging
from logging_code import setup_logging
logger = setup_logging('feature_scaling')
import sys
import os
from sklearn.preprocessing import StandardScaler #Z_Score
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
from All_Models import common
import pickle

def fs(X_train,y_train,X_test,y_test):
    try:
        logger.info(f"Training data independent size : {X_train.shape}")
        logger.info(f"Training data dependent size : {y_train.shape}")
        logger.info(f"Testing data independent size : {X_test.shape}")
        logger.info(f"Testing data dependent size : {y_test.shape}")
        logger.info(f"before : {X_train.head(1)}")

        sc = StandardScaler()
        sc.fit(X_train)
        X_train_sc = sc.transform(X_train)
        X_test_sc = sc.transform(X_test)

        with open('standard_scalar.pkl','wb') as f:
            pickle.dump(sc,f)

        logger.info(f'{X_train_sc}')
        common(X_train_sc,y_train,X_test_sc,y_test)
        reg = LogisticRegression(C= 0.01, class_weight = None, max_iter = 100, penalty = 'l1', solver = 'saga')
        reg.fit(X_train_sc,y_train) #training completed
        logger.info(f"Test Accuracy : {accuracy_score(y_test, reg.predict(X_test_sc))}")
        logger.info(f"Test Confusion Matrix : {confusion_matrix(y_test, reg.predict(X_test_sc))}")
        logger.info(f"Classification report : {classification_report(y_test, reg.predict(X_test_sc))}")

        with open('Model.pkl','wb') as f:
            pickle.dump(reg,f)


    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")