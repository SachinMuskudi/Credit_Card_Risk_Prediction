'''
In this file I am going to call all related functions for data cleaning and model
development
'''
# importing needed libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")
import os
import logging
from logging_code import setup_logging
logger = setup_logging("main")
import sys
from sklearn.model_selection import train_test_split
from Random_Sample_Imputation import handling_missing_values
from var_out import vt_outliers
from filter_methods import fm
from Categorical_to_num import c_t_n
from imblearn.over_sampling import SMOTE
from feature_scaling import fs

class CREDIT:
    #initializing constructor with variables and functions
    def __init__(self,path):
        try:
            self.path = path
            self.df = pd.read_csv(self.path) # loading the data into varibale
            logger.info(f"Total data_size : {self.df.shape}")
            self.df = self.df.drop([150000,150001],axis=0)
            self.df = self.df.drop(['MonthlyIncome.1'],axis=1)
            logger.info(f'Null Values: \n : {self.df.isnull().sum()}')
            self.X = self.df.iloc[:,:-1] #independent
            self.y = self.df.iloc[:,-1] #dependent
            self.X_train,self.X_test,self.y_train,self.y_test = train_test_split(self.X,self.y,test_size=0.2,random_state=42)
            self.y_train = self.y_train.map({'Good': 1, 'Bad': 0}).astype(int)
            self.y_test = self.y_test.map({'Good': 1, 'Bad': 0}).astype(int)
            logger.info(f'Train Data Size: {len(self.X_train)} : {len(self.y_train)} \n Total train Data: {self.X_train.shape}')
            logger.info(f'Test Data Size : {len(self.X_test)} : {len(self.y_test)} \n: total test data : {self.X_test.shape}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")

    def missing_values(self):
        try:
            logger.info(f'Before Handling Null Values , X_train Columns and shape {self.X_train.shape} \n{self.X_train.columns} : \n{self.X_train.isnull().sum()}')
            logger.info(f'Before Handling Null values X_test columns and shape {self.X_test.shape} \n{self.X_test.columns} : \n{self.X_test.isnull().sum()}')

            #converting object datatype to numerical data
            self.X_train['NumberOfDependents'] = pd.to_numeric(self.X_train['NumberOfDependents'])
            self.X_test['NumberOfDependents'] = pd.to_numeric(self.X_test['NumberOfDependents'])

            #calling a function from Random_Sample_Imputation file
            self.X_train, self.X_test = handling_missing_values(self.X_train, self.X_test)
            logger.info(f'After Handling Null Values , X_train Columns and shape {self.X_train.shape} \n{self.X_train.columns} : \n{self.X_train.isnull().sum()}')
            logger.info(f'After Handling Null values X_test columns and shape {self.X_test.shape} \n{self.X_test.columns} : \n{self.X_test.isnull().sum()}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")

    def data_separation(self):
        try:
            #separation of number columns from X_train and X_test
            self.X_train_num_cols = self.X_train.select_dtypes(exclude='object')
            self.X_test_num_cols = self.X_test.select_dtypes(exclude='object')

            # separation of categorical columns from X_train and X_test
            self.X_train_cat_cols = self.X_train.select_dtypes(include='object')
            self.X_test_cat_cols = self.X_test.select_dtypes(include='object')

            logger.info(f'{self.X_train_num_cols.columns} : {self.X_train_num_cols.shape}')
            logger.info(f'{self.X_test_num_cols.columns} : {self.X_test_num_cols.shape}')
            logger.info('===============================================================')
            logger.info(f'{self.X_train_cat_cols.columns} : {self.X_train_cat_cols.shape}')
            logger.info(f'{self.X_test_cat_cols.columns} : {self.X_test_cat_cols.shape}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")
    def variable_transformation(self):
        try:
            logger.info(f'Before Train Column Name: \n{self.X_train_num_cols.columns} : {self.X_train_num_cols.shape}')
            logger.info(f'Before Test Column Name: \n{self.X_test_num_cols.columns} : {self.X_test_num_cols.shape}')

            self.X_train_num_cols,self.X_test_num_cols = vt_outliers(self.X_train_num_cols,self.X_test_num_cols)

            logger.info(f'After Train Column Name: \n{self.X_train_num_cols.columns} : {self.X_train_num_cols.shape}')
            logger.info(f'After Test Column Name: \n{self.X_test_num_cols.columns} : {self.X_test_num_cols.shape}')
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")

    def feature_selection(self):
        try:
            self.X_train_num_cols,self.X_test_num_cols = fm(self.X_train_num_cols,self.X_test_num_cols,self.y_train,self.y_test)
        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")

    def cat_to_num(self):
        try:
            self.X_train_cat_cols,self.X_test_cat_cols = c_t_n(self.X_train_cat_cols,self.X_test_cat_cols)

            #combine data
            self.X_train_cat_cols.reset_index(drop=True,inplace=True)
            self.X_train_num_cols.reset_index(drop=True,inplace=True)
            self.X_test_cat_cols.reset_index(drop=True,inplace=True)
            self.X_test_num_cols.reset_index(drop=True,inplace=True)

            self.training_data = pd.concat([self.X_train_num_cols,self.X_train_cat_cols],axis=1)
            self.testing_data = pd.concat([self.X_test_num_cols,self.X_test_cat_cols],axis=1)

            logger.info('====================================================')
            logger.info(f'Final Training Data : {self.training_data.shape} \n{self.training_data.columns}')
            logger.info(f'{self.training_data.isnull().sum()}')

            logger.info(f'Final Testing Data : {self.testing_data.shape} \n{self.testing_data.columns}')
            logger.info(f'{self.testing_data.isnull().sum()}')

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")

    def data_balancing(self):
        try:
            logger.info(f'Number of Rows for Good Columns {1}: {sum(self.y_train == 1)}')
            logger.info(f'Number of Rows for Bad Columns {0}: {sum(self.y_train == 0)}')
            logger.info(f'Training data size: {self.training_data.shape}')

            sm = SMOTE(random_state=42)

            self.training_data_bal,self.y_train_bal = sm.fit_resample(self.training_data,self.y_train)

            logger.info(f"Number of Rows for Good Customer {1} : {sum(self.y_train_bal == 1)}")
            logger.info(f"Number of Rows for Bad Customer {0} : {sum(self.y_train_bal == 0)}")
            logger.info(f"Training data size : {self.training_data_bal.shape}")

            fs(self.training_data_bal,self.y_train_bal,self.testing_data,self.y_test)

        except Exception as e:
            er_type, er_msg, er_line = sys.exc_info()
            logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")





if __name__ == "__main__":
    try:
        obj = CREDIT('creditcard.csv')
        obj.missing_values()
        obj.data_separation()
        obj.variable_transformation()
        obj.feature_selection()
        obj.cat_to_num()
        obj.data_balancing()
    except Exception as e:
        er_type,er_msg,er_line = sys.eXc_info()
        logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")