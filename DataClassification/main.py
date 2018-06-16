# -*-coding:utf-8-*-

from module.gameFeature import GameFeature
from module.featureDigitalize import FeatureDigitalize
def main():

    gameFeature = GameFeature("localhost", "root", "5566", "steam", "top_seller")
    # print(gameFeature.Create())
    feature = FeatureDigitalize(gameFeature.Create())
    print(feature.Digitalize())


print(main())
