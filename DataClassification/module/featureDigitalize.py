# -*-coding:utf-8-*-

class FeatureDigitalize():
    def __init__(self, gameFeature):
        self.gameFeature = gameFeature

    def Digitalize(self):
        feature = self.gameFeature
        digDic = {}
        for name in feature.keys():
            price = feature[name]['price']
            language = self.DigitalizeLanguage(feature[name]['language'])
            sysReqMin = self.DigitalizeSysReq(feature[name]['sysReqMin'])
            sysReqRec = self.DigitalizeSysReq(feature[name]['sysReqRec'])
            sellPerMonth = self.DigitalizeSell(feature[name]['date'], feature[name]['totalSell'])
            digDic[name] = {'price':price, 'language':language, 'sysReqMin':sysReqMin, 'sysReqRec':sysReqRec, 'sellPerMonth':sellPerMonth}

        return digDic

    def DigitalizeLanguage(self, languageList):
        population = 0
        billion = 10**9
        million = 10**6
        languagePopulationDic = {'English':1.12*billion, 'Chinese':1.1*billion, 'Spanish':512.9*million,
        'French':284.9*million, 'Russian':264.3*million, 'Portuguese':236.5*million,
        'Portuguese-Brazil':236.5*million , 'German':132*million, 'Japanese':128.3*million,
        'Turkish':78.9*million, 'Korean':77.2*million, 'Italian':67.8*million,
        'Thai':60.5*million, 'Polish':40.265*million, 'Ukrainian':32.948*million, 'Dutch':23.025*million, 'Finnish':5.789*million}

        for language in languageList:
            if language in languagePopulationDic.keys():
                population += languagePopulationDic[language]

        return population

    def DigitalizeSysReq(self, sysReqList):
        return 5

    def DigitalizeSell(self, date, totalSell):
        releasedMonth = (2018 - date['year']) * 12 + (6 - date['month']) + 1
        return (totalSell / releasedMonth)
