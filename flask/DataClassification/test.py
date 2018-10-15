# -*-coding:utf-8-*-

from module.gameFeature import GameFeature
from module.featureDigitalize import FeatureDigitalize
from module.dataTraining import DataTraining

def main():
    trainFeature = GameFeature("localhost", "root", "5566", "steam", "steam_spy").Create()
    trainData = FeatureDigitalize(trainFeature).Digitalize()
    # count = 0
    # for name in trainData.keys():
    #     print (trainData[name])
    #     count += 1
    # print(count)
    
    testFeature = GameFeature("localhost", "root", "5566", "steam", "steam_spy_2017").Create()
    testData = FeatureDigitalize(testFeature).Digitalize()
    coef, intercept, std, amin, amax, result = DataTraining(trainData, testData).TrainAndTest()
    # coef, intercept, std, amin, amax, result = DataTraining(trainData, trainData).Predict()

    
    print(coef)
    print(intercept)
    print('\n')
    print(std)
    print(amin)
    print(amax)
    # print(result)

    # a = b = 0
    # 
    # for dic in trainFeature:
    #     print(dic)
    #     a += 1
    # 
    # for name in trainData.keys():
    #     print(trainData[name])
    #     b += 1
    
    # print(a,b)
    # trainResult1, trainResult2 = DataTraining(trainData, trainData).Train()
    # print(trainResult1, trainResult2)

print(main())

