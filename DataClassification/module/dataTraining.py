# -*-coding:utf-8-*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

class DataTraining():
    def __init__(self, trainData, testData):
        self.trainData = trainData
        self.testData = testData

    def TrainAndTest(self):
        trainData = self.trainData
        testData = self.testData

        train_X, train_Y, train_YMin, train_YMax = self.CreateArray(trainData)
        test_X, test_Y, test_YMin, test_YMax = self.CreateArray(testData)

        module = LinearRegression()
        module.fit(train_X, train_Y)
        predictArray = module.predict(test_X)
        predictArray[predictArray < 0] = 0
        predictList = predictArray.tolist()
        
        resultList = []

        for i in range(len(predictList)):
            if predictList[i] > test_YMax[i]:
                resultList.append((predictList[i] - test_YMax[i]) / test_YMax[i])
            elif predictList[i] < test_YMin[i]:
                resultList.append((predictList[i] - test_YMin[i]) / test_YMin[i])
            else:
                resultList.append(0)

        result =  np.array(resultList)
        std = np.std(result, ddof = 1)
        avg = np.histogram(result)
        amin = np.amin(result)
        amax = np.amax(result)
        plt.boxplot(result)
        plt.show()

        return (module.coef_, module.intercept_, avg, amin, amax, resultList)

    def TrainAndPredict(self):
        trainData = self.trainData
        targetData = self.testData

        train_X, train_Y, train_YMin, train_YMax = self.CreateArray(trainData)
        target_X, target_Y, target_YMin, target_YMax = self.CreateArray(targetData)

        module = LinearRegression()
        module.fit(train_X, train_Y)
        target_Y = module.predict(target_X)

        return target_Y
        

    def CreateArray(self, data):
        data_x = []
        data_y = []
        data_yMin = []
        data_yMax = []

        for name in data.keys():
            data_y.append(data[name]['sell'])
            data_yMin.append(data[name]['sellMin'])
            data_yMax.append(data[name]['sellMax'])
            data_x.append([data[name]['price'], data[name]['Mlanguage'], data[name]['tag'], data[name]['introduction'], data[name]['about'], data[name]['Kview']])

        return np.array(data_x), np.array(data_y), data_yMin, data_yMax
