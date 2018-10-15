class TargetFeature():
    def __init__(self, targetList):
        self.targetList = targetList

    def Create(self):
        targetDic = {}

        name = self.targetList[0]
        sell = self.CreateSell()
        price = self.targetList[1]
        date = self.CreateDate()
        tag = self.targetList[2]
        language = str(self.targetList[3])
        introduction = self.CreateIntroduction(self.targetList[4])
        about = self.CreateAbout(self.targetList[5])
        view = int(self.targetList[6])

        targetDic[name] = {'sell':sell, 'price':price, 'date':date, 'tag':tag, 'language':language, 'introduction':introduction, 'about':about, 'view' : view}
        
        return targetDic

    def CreateSell(self):
        sellDic = {}
        sellDic['min'] = 0
        sellDic['max'] = 0
        return sellDic

    def CreatePrice(self, rawMeat):
        price = rawMeat.strip()
        return price

    def CreateDate(self):
        date = {}
        date['year'] = 2018
        date['month'] = 10
        return date

    def CreateTag(self, rawMeat):
        tagList = rawMeat.split(',')
        return tagList

    def CreateLanguage(self, rawMeat):
        languageList = rawMeat.split(',')
        return languageList

    def CreateIntroduction(self, rawMeat):
        introduction = rawMeat.strip()
        return introduction

    def CreateAbout(self, rawMeat):
        aboutList = []
        tempList = rawMeat.splitlines()
        for element in tempList:
            aboutList.append(element.strip())
        return aboutList
    
    def CreateView(self, rawMeat):
        view = rawMeat.strip()
        return int(view)
