# -*-coding:utf-8-*-

import numpy as np
from sklearn.linear_model import LinearRegression

class DataTraining():
    def __init__(self, trainData, testData):
        self.trainData = trainData
        self.testData = testData

    def Train(self):
        trainData = self.trainData
        train_X, train_Y, train_YMin, train_YMax = self.CreateArray(trainData)
        module = LinearRegression()
        module.fit(train_X, train_Y)
        return (module.coef_, module.intercept_)

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
                resultList.append((test_YMin[i] - predictList[i]) / test_YMin[i])
            else:
                resultList.append(0)

        # result = (test_Y - module.predict(test_X)) / test_Y
        # matchMin = (module.predict(test_X) > test_YMin)
        # matchMax = (module.predict(test_X) < test_YMax)
        # match = matchMin.astype(int) *  matchMax.astype(int)
        # reg = LinearRegression().fit(test_Y, module.coef_)
        result =  np.array(resultList)
        std = np.std(result, ddof = 1)
        amin = np.amin(result)
        amax = np.amax(result)

        return (module.coef_, module.intercept_, std, amin, amax, resultList)

    # def Predict(self):
    #     pass

    def CreateArray(self, data):
        data_x = []
        data_y = []
        data_yMin = []
        data_yMax = []

        for name in data.keys():
            data_y.append(data[name]['sell'])
            data_yMin.append(data[name]['sellMin'])
            data_yMax.append(data[name]['sellMax'])
            data_x.append([data[name]['price'], data[name]['language'], data[name]['tag']])

        return np.array(data_x), np.array(data_y), data_yMin, data_yMax
