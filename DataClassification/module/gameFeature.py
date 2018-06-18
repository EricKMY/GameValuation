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
        nameList = []

        for record in results:
            name = record[0].strip()
            price = self.CreatePrice(record[2])
            language = self.CreateLanguage(record[4])
            date = self.CreateDate(record[5])
            sysReqMin = self.CreateSysReq(record[6])
            sysReqRec = self.CreateSysReq(record[7])
            totalSell = 500000000
            gameDic[name] = {'price':price, 'language':language, 'date':date, 'sysReqMin':sysReqMin, 'sysReqRec':sysReqRec, 'totalSell':totalSell}
        schema.close()
        return gameDic

    def CreatePrice(self, rawMeat):
        price = rawMeat.strip()

        if price.find("NT$") == -1:
            price = 0
        else:
            price = price.replace('NT$ ', '')
            price = price.replace(',', '')
            price = int(price)

        return price

    def CreateLanguage(self, rawMeat):
        language = []
        languageList = rawMeat.splitlines()
        chineseExist = False
        del languageList[0]

        for element in languageList:
            element = element.strip()
            if element == 'Traditional Chinese' or element == 'Simplified Chinese':
                chineseExist = True
            else:
                language.append(element)

        if chineseExist:
            language.append('Chinese')

        return language

    def CreateDate(self, rawMeat):
        date = {}
        dateList = rawMeat.split(', ')
        date['day'] = int(dateList[0].split(' ')[0])
        month = dateList[0].split(' ')[-1]
        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        for i in range(len(monthList)):
            if month == monthList[i]:
                month = i + 1

        date['month'] = month
        date['year']  = int(dateList[1])

        return date

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
