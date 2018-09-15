# -*-coding:utf-8-*-

from module.gameFeature import GameFeature
from module.featureDigitalize import FeatureDigitalize
from module.dataTraining import DataTraining

def main():
    trainFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller").Create()
    trainData = FeatureDigitalize(trainFeature).Digitalize()
    # testFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller_2017").Create()
    # testData = FeatureDigitalize(testFeature).Digitalize()
    # result1, result2, result3 = DataTraining(trainData, testData).TrainAndTest()
    #
    # print(result1)
    # print(result2)
    # print('\n')
    # print(result3)

    a = b = 0

    for dic in trainFeature:
        print(dic)
        a += 1

    for dic in trainData:
        print(dic)
        b += 1

    print(a,b)

print(main())
