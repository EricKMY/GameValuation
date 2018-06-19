# -*-coding:utf-8-*-

import numpy as np
from sklearn.linear_model import LinearRegression

class DataTraining():
    def __init__(self):
        pass

    def Training(self, trainingData):
        x = []
        y = []

        for name in trainingData.keys():
            y.append(trainingData[name]['sellPerMonth'])
            x.append([trainingData[name]['price'], trainingData[name]['language'], trainingData[name]['sysReqMin'], trainingData[name]['sysReqRec']])

        X = np.array(x)
        Y = np.array(y)
        lm = LinearRegression()
        lm.fit(X, Y)

        return (lm.coef_, lm.intercept_ )

    def Testing(self, testingData):
        pass

    # def fname(arg):
    #     pass
