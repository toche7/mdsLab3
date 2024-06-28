def homework(): 
    import pandas as pd
    import numpy as np  
    import matplotlib.pyplot as plt

    exDf = pd.read_csv("https://raw.githubusercontent.com/toche7/DataSets/main/yieldvsTemp.txt")
    exDf

    # create model 1 for linear regression
    from sklearn.linear_model import LinearRegression
 


    # create model 2 for linear regression wih polynomial features
    from sklearn.preprocessing import PolynomialFeatures
 
    # return the value of the score for model 1 and model 2
    scoreModel1 = None
    scoreModel2 = None
    return scoreModel1, scoreModel2


if __name__ == '__main__':
    print(homework())
