# -*-coding:utf-8-*-

from module.gameFeature import GameFeature
from module.featureDigitalize import FeatureDigitalize
from module.dataTraining import DataTraining

def main():
    trainFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller")
    # testFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller_2017")
    trainData = FeatureDigitalize(trainFeature.Create())
    # testData = FeatureDigitalize(testFeature.Create())
    # result = DataTraining(featureDigit.Digitalize())
    result = trainFeature.Create()
    for name in result.keys():
        print (result[name]['date'])
        print ("\n")
    # print(DataTraining.Training(trainingData))

print(main())
