# -*-coding:utf-8-*-

from module.gameFeature import GameFeature
from module.featureDigitalize import FeatureDigitalize
from module.dataTraining import DataTraining

def main():
    # trainFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller").Create()
    trainFeature = GameFeature("localhost", "root", "5566", "steam", "steam_spy").Create()
    # print(trainFeature)
    # count = 0
    # for name in trainFeature.keys():
    #     print (trainFeature[name])
    #     count += 1
    # print(count)
    trainData = FeatureDigitalize(trainFeature).Digitalize()
    # testFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller_2017").Create()
    # testData = FeatureDigitalize(testFeature).Digitalize()
    coef, intercept, std, amin, amax, result = DataTraining(trainData, trainData).TrainAndTest()
    # coef, intercept, std, amin, amax, result = DataTraining(trainData, trainData).Predict()

    
    print(coef)
    print(intercept)
    print('\n')
    print(std)
    print(amin)
    print(amax)
    print(result)

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

#sql clear table: TRUNCATE TABLE table_name ex.TRUNCATE TABLE steam_spy
