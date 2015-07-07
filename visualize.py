# -*- coding: utf-8 -*-
"""
Created on Sun Jul 05 20:34:47 2015

@author: Steve Elston

This code creates visualizations of the forest fire data set.
"""
def trimOutliers(df, trimList, limLst):
    i = 0
    for x in trimList:
        print(x, i, limLst[i][0], limLst[i][1])
        filt = ((df[x] > limLst[i][0]) & (df[x] < limLst[i][1]))
        df = df[filt]
        i += 1
    return df


def azureml_main(frame1):
    import matplotlib
    matplotlib.use("agg")
    matplotlib.style.use('ggplot')
    import pandas as pd
    from pandas.tools.plotting import scatter_matrix
    from mpl_toolkits.mplot3d import Axes3D
    import numpy as np
    import matplotlib.pyplot as plt
    Azure = False

## If not running in MAML read the data from a csv file.
    if(Azure == False):
        frame1 = pd.read_csv("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\forestfireslog.csv")

    
    fig2 = plt.figure(2, figsize = (10,6))
    ax = fig2.gca()
    plt.plot(frame1["X"], frame1["Y"], 'bo', alpha = 0.2)
    fig2.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig2.png")
    
    fig1 = plt.figure(1, figsize = (10,6))
    ax = fig1.gca()
    
    plotCols = ["FFMC", "DMC", "DC", "ISI", \
    "temp", "RH", "wind", "rain", "areaLog"]
#    print(pd.DataFrame.head(frame1[plotCols]))
    scatter_matrix(frame1[plotCols], ax = ax, alpha = 0.5)
    fig1.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig1.png")
    
    print(frame1.shape)
    trmCols = ["FFMC", "ISI", "rain"]
    trmLst = [[-3.0, 10.0], [-10.0, 4.0], [-10.0, 3.0]]
    frame2 = trimOutliers(frame1, trmCols, trmLst)    
    print(frame1.shape)
    
    fig4 = plt.figure(4, figsize = (10,6))
    ax = fig4.gca()
    scatter_matrix(frame2[plotCols], ax = ax, alpha = 0.5)
    fig4.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig4.png")
    
    fig5 = plt.figure(5, figsize = (12,8))
    ax = fig5.add_subplot(221, projection='3d')
    ax.scatter(frame2["X"], frame2["Y"], frame2["areaLog"], c = 'r')
    ax = fig5.add_subplot(222, projection='3d')
    ax.scatter(frame1["X"], frame1["Y"], frame1["areaLog"], c = 'r')
    fig5.savefig("C:\\Users\\Steve\\Documents\\AzureML\\Data Sets\\Forest_Fire\\fig5.png")
    
    return frame1
    
    
 
azureml_main([1,2])   
    
        
    