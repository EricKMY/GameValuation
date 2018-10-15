# -*-coding:utf-8-*-

class FeatureDigitalize():
    def __init__(self, gameFeature):
        self.gameFeature = gameFeature

    def Digitalize(self):
        feature = self.gameFeature
        digDic = {}
        for name in feature.keys():
            sell = self.DigitalizeSell(feature[name]['sell']['min'], feature[name]['sell']['max'])
            sellMin = feature[name]['sell']['min']
            sellMax = feature[name]['sell']['max']
            price = feature[name]['price']
            Mlanguage = self.DigitalizeLanguage(feature[name]['language'])
            tag = feature[name]['tag']
            introduction = len(feature[name]['introduction'])
            about = len(feature[name]['about'])
            Kview = feature[name]['view'] / 1000
            digDic[name] = {'sell' :sell, 'sellMin' :sellMin, 'sellMax' :sellMax, 'price' :price, 'Mlanguage' :Mlanguage, 'tag' : tag, 'introduction' : introduction, 'about' : about, 'Kview' : Kview}
            # sysReqMin = self.DigitalizeSysReq(feature[name]['sysReqMin'])
            # sysReqRec = self.DigitalizeSysReq(feature[name]['sysReqRec'])
            # sellPerMonth = self.DigitalizeSell(feature[name]['date'], feature[name]['sell'])
            # digDic[name] = {'sellPerMonth':sellPerMonth, 'price':price, 'language':language, 'sysReqMin':sysReqMin, 'sysReqRec':sysReqRec}

        return digDic

    def DigitalizeSell(self, min, max):
        # releasedMonth = (2018 - date['year']) * 12 + (6 - date['month']) + 1
        # if releasedMonth == 0:
        #     releasedMonth = 1
        # return (totalSell / releasedMonth)
        return ((min + max) / 2)
        # return max

    def DigitalizeLanguage(self, languageList):
        BILLION = 10**9
        MILLION = 10**6
        # WORLD_POPULATION = 7.62 * BILLION
        totalPopulation = 0
        languagePopulationDic = {'English':1.12*BILLION, 'Chinese':1.1*BILLION, 'Spanish':512.9*MILLION,
        'French':284.9*MILLION, 'Russian':264.3*MILLION, 'Portuguese':236.5*MILLION,
        'Portuguese-Brazil':236.5*MILLION , 'German':132*MILLION, 'Japanese':128.3*MILLION,
        'Turkish':78.9*MILLION, 'Korean':77.2*MILLION, 'Italian':67.8*MILLION,
        'Thai':60.5*MILLION, 'Polish':40.265*MILLION, 'Ukrainian':32.948*MILLION, 'Dutch':23.025*MILLION, 'Finnish':5.789*MILLION}

        # for language in languageList:
        #     if language in languagePopulationDic.keys():
        #         population += languagePopulationDic[language]
        for language, population in languagePopulationDic.items():
            if languageList.find(language) != -1:
                totalPopulation += population

        return totalPopulation / MILLION
    
    def DigitalizeTag(self, tagList):
        return len(tagList)

    # def DigitalizeSysReq(self, sysReqList):
    #     CPU = GPU = RAM = 0

    #     for sysName in sysReqList:
    #         if sysName == 'processor':
    #             CPU = self.ScoreCPU(sysReqList[sysName]) * 4
    #         if sysName == 'graphics':
    #             GPU = self.ScoreGPU(sysReqList[sysName]) * 2
    #         if sysName == 'memory':
    #             RAM = self.ScoreRAM(sysReqList[sysName]) * 1

    #     return (CPU + GPU + RAM + 1) / 8

    # def ScoreCPU(self, cpu):
    #     if cpu.find('i5') or cpu.find('i7'):
    #         return 1
    #     else:
    #         return 0

    # def ScoreGPU(self, gpu):
    #     if gpu.find('512 MB VRAM'):
    #         return 1
    #     else:
    #         return 0

    # def ScoreRAM(self, ram):
    #     ramList = ram.strip()
    #     RAM = int(ramList[0])

    #     if RAM > 4:
    #         return 1
    #     else:
    #         return 0
