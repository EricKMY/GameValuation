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

        train_name ,train_X, train_Y, train_YMin, train_YMax = self.CreateArray(trainData)
        test_name,test_X, test_Y, test_YMin, test_YMax = self.CreateArray(testData)

        module = LinearRegression()
        module.fit(train_X, train_Y)
        predictArray = module.predict(test_X)
        predictArray[predictArray < 0] = 0
        predictList = predictArray.tolist()
        
        resultList = []
        smoothList = []
        extermHighList = []

        for i in range(len(predictList)):
            if predictList[i] > test_YMax[i]:          
                if (predictList[i] - test_YMax[i]) / test_YMax[i] < 5:
                    resultList.append((predictList[i] - test_YMax[i]) / test_YMax[i])
                    smoothList.append(test_name[i])
                else:
                    extermHighList.append(test_name[i])
            elif predictList[i] < test_YMin[i]:
                if (predictList[i] - test_YMin[i]) / test_YMin[i] >= -1:
                    resultList.append((predictList[i] - test_YMin[i]) / test_YMin[i])
                    smoothList.append(test_name[i])
            else:
                resultList.append(0)
                smoothList.append(test_name[i])

        result =  np.array(resultList)
        std = np.std(result, ddof = 1)
        avg = np.mean(result)#np.percentile(result, [25, 50, 75])
        amin = np.amin(result)
        amax = np.amax(result)
        # plt.boxplot(result)
        plt.hist(result)
        # plt.show()

        return (module.coef_, module.intercept_, avg, len(resultList), len(extermHighList), resultList)

    def TrainAndPredict(self):
        trainData = self.trainData
        targetData = self.testData

        train_name,train_X, train_Y, train_YMin, train_YMax = self.CreateArray(trainData)
        target_name, target_X, target_Y, target_YMin, target_YMax = self.CreateArray(targetData)

        module = LinearRegression()
        module.fit(train_X, train_Y)
        # target_Y = module.predict(target_X)

        target_X = np.float32(target_X)
        return int(module.predict(target_X))
        

    def CreateArray(self, data):
        data_name = []
        data_x = []
        data_y = []
        data_yMin = []
        data_yMax = []

        for name in data.keys():
            data_name.append(data[name])
            data_y.append(data[name]['sell'])
            data_yMin.append(data[name]['sellMin'])
            data_yMax.append(data[name]['sellMax'])
            data_x.append([data[name]['price'], data[name]['Mlanguage'], data[name]['tag'], data[name]['introduction'], data[name]['about'], data[name]['Kview']])
        return data_name, np.array(data_x), np.array(data_y), data_yMin, data_yMax
