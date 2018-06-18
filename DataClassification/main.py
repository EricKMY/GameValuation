# -*-coding:utf-8-*-

from module.gameFeature import GameFeature
from module.featureDigitalize import FeatureDigitalize
from module.dataTraining import DataTraining

def main():
    gameFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller")
    featureDigit = FeatureDigitalize(gameFeature.Create())
    # result = DataTraining(featureDigit.Digitalize())
    # result = gameFeature.Create()
    # for name in result.keys():
    #     print (result[name]['sysReqMin']['memory'])
    #     print ("\n")
    print(featureDigit.Digitalize())

print(main())
