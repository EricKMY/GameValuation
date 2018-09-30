# -*-coding:utf-8-*-

import numpy as np
from sklearn.linear_model import LinearRegression

class DataTraining():
    def __init__(self, trainData, testData):
        self.trainData = trainData
        self.testData = testData

    def Train(self):
        trainData = self.trainData
        train_X, train_Y = self.CreateArray(trainData)
        module = LinearRegression()
        module.fit(train_X, train_Y)
        return (module.coef_, module.intercept_)

    def TrainAndTest(self):
        trainData = self.trainData
        testData = self.testData

        train_X, train_Y = self.CreateArray(trainData)
        test_X, test_Y = self.CreateArray(testData)

        module = LinearRegression()
        module.fit(train_X, train_Y)
        module.predict(test_X)

        result = (test_Y - module.predict(test_X)) / test_Y
        # reg = LinearRegression().fit(test_Y, module.coef_)
        aa = np.std(result, ddof = 1)

        return (module.coef_, module.intercept_, aa)

    def CreateArray(self, data):
        data_x = []
        data_y = []

        for name in data.keys():
            data_y.append(data[name]['sell'])
            data_x.append([data[name]['price'], data[name]['language'], data[name]['tag']])

        return np.array(data_x), np.array(data_y)
