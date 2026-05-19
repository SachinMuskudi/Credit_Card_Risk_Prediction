import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys
import seaborn as sns
import logging
from logging_code import setup_logging
logger = setup_logging('filter_methods')
import warnings
warnings.filterwarnings('ignore')
from sklearn.feature_selection import VarianceThreshold
from scipy.stats import pearsonr

def fm(X_train_num,X_test_num,y_train,y_test):
    try:
        logger.info(f'Before Train Colum: {X_train_num.shape} \n{X_train_num.columns}')
        logger.info(f'Before Test Colum: {X_test_num.shape} \n{X_test_num.columns}')

        #feature selection
        reg = VarianceThreshold(threshold=0.01)
        reg.fit(X_train_num)
        logger.info(f'Number of Good Columns: {sum(reg.get_support())} : {X_train_num.columns[reg.get_support()]}')
        logger.info(f'Number of Bad Columns: {sum(~reg.get_support())} : {X_train_num.columns[~reg.get_support()]}')

        X_train_num = X_train_num.drop(['NPA Status_trim', 'NumberOfTime30-59DaysPastDueNotWorse_trim',
                                        'NumberOfTimes90DaysLate_trim',
                                        'NumberOfTime60-89DaysPastDueNotWorse_trim'], axis=1)
        X_test_num = X_test_num.drop(['NPA Status_trim', 'NumberOfTime30-59DaysPastDueNotWorse_trim',
                                      'NumberOfTimes90DaysLate_trim',
                                      'NumberOfTime60-89DaysPastDueNotWorse_trim'], axis=1)

        logger.info(f'After Train Colum: {X_train_num.shape} \n{X_train_num.columns}')
        logger.info(f'After Test Colum: {X_test_num.shape} \n{X_test_num.columns}')

        logger.info('======================== Hypothesis Testing ===============================')
        c = []
        for i in X_train_num.columns:
            results = pearsonr(X_train_num[i], y_train)
            c.append(results)
        t = np.array(c)
        p_value = pd.Series(t[:, 1], index=X_train_num.columns)
        # p = 0
        # f = []
        # for i in p_value:
        #     if i < 0.05:
        #         f.append(X_train_num.columns[p])
        #     p = p + 1
        # print(X_train_num.columns)
        # print(f)
        X_train_num = X_train_num.drop(['DebtRatio_trim'], axis=1)
        X_test_num = X_test_num.drop(['DebtRatio_trim'], axis=1)
        logger.info(f'After Train Colum: {X_train_num.shape} \n{X_train_num.columns}')
        logger.info(f'After Test Colum: {X_test_num.shape} \n{X_test_num.columns}')

        return X_train_num,X_test_num

    except Exception as e:
        er_type, er_msg, er_line = sys.exc_info()
        logger.info(f"Error in line no : {er_line.tb_lineno} due to : {er_msg}")