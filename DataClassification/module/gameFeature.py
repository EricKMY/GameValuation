# -*-coding:utf-8-*-
import pymysql

class GameFeature():
    def __init__(self, host, user, passwd, schema, table):
        self.host = host
        self.user = user
        self.passwd = passwd
        self.schema = schema
        self.table = table

    def Create(self):
        schema = pymysql.connect(host = self.host, user = self.user, passwd = self.passwd, db = self.schema)
        cursor = schema.cursor()
        cursor.execute("SELECT * FROM " + self.table)
        results = cursor.fetchall()
        gameDic = {}

        for record in results:
            name = record[0].strip()
            sell = self.CreateSell(record[2])
            price = self.CreatePrice(record[3])
            date = self.CreateDate(record[4])
            tag = self.CreateTag(record[5])
            language = self.CreateLanguage(record[6])
            introduction = self.CreateIntroduction(record[9])
            about = self.CreateAbout(record[10])
            view = self.CreateYoutube(record[11])

            gameDic[name] = {'sell':sell, 'price':price, 'date':date, 'tag':tag, 'language':language, 'introduction':introduction, 'about':about, 'view':view}

        schema.close()
        return gameDic

    def CreateSell(self, rawMeat):
        sellDic = {}
        sell = rawMeat.split('\xa0..\xa0')
        sellDic['min'] = int(sell[0].replace(',', '').replace(': ', ''))
        sellDic['max'] = int(sell[1].replace(',', ''))

        return sellDic

    def CreatePrice(self, rawMeat):
        price = rawMeat.strip()
        price = float(price.replace('$', ''))

        # if price.find('Free') == -1:
        #     priceList = price.split('$')
        #     priceList.pop(0)
        #     priceList = [double(element.replace(',', '')) for element in priceList]  #string 12,000 -> int 12000
        #     price = min(priceList)
        # else:
        #     price = 0

        return price

    def CreateDate(self, rawMeat):
        date = {}
        yearList = ['2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018']
        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for year in yearList:
            if rawMeat.find(year) != -1:
                date['year'] = int(year)
                break

        count = 0
        for month in monthList:
            count += 1
            if rawMeat.find(month) != -1:
                date['month'] = count

        return date

    def CreateTag(self, rawMeat):
        tag = rawMeat.replace('Summary!!Atmospheric!!At!!Crafting!!Cr!!Experimental!!Ex!!Female Protagonist!!FP!!Kickstarter!!KS!!Open World!!OW!!Remake!!Re!!Space Sim!!SS!!Stealth!!St!!Warhammer 40K!!WH!!Zombies!!Zb!!', '')
        tagList = tag.split('!!')
        return tagList

    def CreateLanguage(self, rawMeat):
        language = rawMeat.replace('English!!EN!!Russian!!RU!!German!!DE!!Spanish!!SP!!Chinese!!CH!!French!!FR!!Polish!!PL!!Turkish!!TR!!Swedish!!SW!!', '')
        # languageList = language.split('!!')
        # print(languageList)
        return language

    def CreateSysReq(self, rawMeat):
        sysReqDic = {}
        sysReqList = rawMeat.strip().split("!!")
        sysDic = {'OS:':'os', 'Processor:':'processor', 'Memory:':'memory', 'Graphics:':'graphics', 'DirectX:':'directX', 'Network:':'network', 'Storage:':'storage', 'Sound Card:':'soundCard'}

        for sysReq in sysReqList:
            for key, value in sysDic.items():
                if sysReq == key:
                    sysReqDic[value] = sysReqList[sysReqList.index(sysReq)+1].strip()
                    break

        return sysReqDic

    def CreateIntroduction(self, rawMeat):
        introduction = rawMeat.strip()
        return introduction

    def CreateAbout(self, rawMeat):
        aboutList = []
        tempList = rawMeat.splitlines()
        for element in tempList:
            aboutList.append(element.strip())
        return aboutList

    def CreateYoutube(self, rawMeat):
        if (rawMeat == ''):
            view = 0
        else:
            viewList = rawMeat.strip().split(" ")
            view = int(viewList[1].replace(',', '').replace('\xa0views', ''))
        return view
