# -*-coding:utf-8-*-

import numpy as np
from sklearn.linear_model import LinearRegression

class DataTraining():
    def __init__(self, trainData, testData):
        self.trainData = trainData
        self.testData = testData

    def TrainAndTest(self):
        trainData = self.trainData
        testData = self.testData

        train_X, train_Y = self.CreateArray(trainData)
        test_X, test_Y = self.CreateArray(testData)

        module = LinearRegression()
        module.fit(train_X, train_Y)
        module.predict(test_X)

        result = (test_Y * 2 - module.predict(test_X)) / test_Y

        return (module.coef_, module.intercept_, result)

    def CreateArray(self, data):
        data_x = []
        data_y = []

        for name in data.keys():
            data_y.append(data[name]['sellPerMonth'])
            data_x.append([data[name]['price'], data[name]['language'], data[name]['sysReqMin'], data[name]['sysReqRec']])

        return np.array(data_x), np.array(data_y)
