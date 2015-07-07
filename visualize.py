# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 20:34:47 2015

@author: Steve Elston

This code creates visualizations of the forest fire data set.
"""
def trimOutliers(df):
    

def azureml_main(frame1):
    import pandas as pd
    import matplotlib
    matplotlib.use("agg")
    matplotlib.style.use('ggplot')
    from pandas.tools.plotting import scatter_matrix
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import matplotlib.pyplot as plt
    Azure = False

## If not running in MAML read the data from a csv file.
    if(Azure == False):
        frame1 = pd.read_csv("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\forestfireslog.csv")

    fig1 = plt.figure(1, figsize = (10,6))
    ax = fig1.gca()
    
    plotCols = ["FFMC", "DMC", "DC", "ISI", \
    "temp", "RH", "wind", "rain", "areaLog"]
#    print(plotCols)
#    print(pd.DataFrame.head(frame1[plotCols]))
    scatter_matrix(frame1[plotCols], ax = ax, alpha = 0.5)
    fig1.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig1.png")
    
    fig2 = plt.figure(2, figsize = (10,6))
    ax = fig2.gca()
#    ptSize = frame1["area"].tolist()
#    print(ptSize)
    plt.plot(frame1["X"], frame1["Y"], 'bo', alpha = 0.2)
    fig2.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig2.png")
    
    fig3 = plt.figure(3, figsize = (10,6))
    ax = fig3.add_subplot(111, projection='3d')
    ax.scatter(frame1["X"], frame1["Y"], frame1["areaLog"], c = 'r')
    fig3.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig3.png")
    
    return frame1
    
    
 
azureml_main([1,2])   
    
        
    