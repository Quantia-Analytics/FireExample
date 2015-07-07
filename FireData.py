# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 17:12:12 2015

@author: Steve Elston

This file contains the Python code for preparing the fire
data for charting and analysis.
"""

def standardize(df):
    return  df.sub(df.mean(1), axis = 0).div(df.std(1), axis = 0)
    
def azureml_main(frame1):
    import pandas as pd
    import numpy as np
    Azure = False

## If not running in MAML read the data from a csv file.
    if(Azure == False):
        frame1 = pd.read_csv("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\forestfires.csv")
 
## Ensure the numeric columns are of type float.  
    floatCols = ["X", "Y", "FFMC", "DMC", "DC", "ISI", \
    "temp", "RH", "wind", "rain", "area"] 
    frame1[floatCols] = frame1[floatCols].astype(float)   

## Add a new column with the log of the area    
    logCols = ["rainLog", "areaLog"]
    frame1[logCols] = frame1[["rain", "area"]].apply(lambda x: np.log2(x + 1))
    
    temp = frame1["rain"]
## If not in MAML standardize the floating point columns and output to a csv file.        
    if(Azure == False):
        floatCols.extend(logCols)
        frame1[floatCols] = frame1[floatCols].apply(standardize)
        frame1.to_csv("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\forestfireslog.csv")
    
    return frame1
    
azureml_main([1,2])