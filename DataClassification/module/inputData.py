import pymysql



def data():
    db = pymysql.connect(host="localhost", user="root", passwd="5566", db="steam")
    cursor = db.cursor()

    cursor.execute("SELECT * FROM top_seller")

    results = cursor.fetchall()
    dataDic = {}
    nameList = []
    for record in results:
        name = record[0].strip()
        #col1 = col1.encode("utf8").decode("cp950", "ignore")
        price = record[2].strip()
        language = CreateLanguage(record[4])#record[4].splitlines()
        date = record[5]
        sysReqMin = record[6].strip()
        sysReqRec = record[7].strip()

        nameList.append(name)

        if price.find("NT$") == -1:
            price = 0
        else:
            price = price.replace('NT$ ', '')
            price = price.replace(',', '')
            price = int(price)

        # del language[0]
        # languageList = []
        # for element in language:
        #     element = element.strip()
        #     languageList.append(element)

        dateList = date.split(', ')
        month = dateList[0].split(' ')[-1]
        monthList = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        for i in range(0, 12):
            if month == monthList[i]:
                month = i + 1
        year = int(dateList[1])
        releasedMonth = (2018 - year) * 12 + (6 - month) + 1

        sysReqMinList = sysReqMin.split('!!')
        sysReqMinDic = {}
        reqList = ['OS:', 'Processor:', 'Memory:', 'Graphics:', 'DirectX:', 'Network:', 'Storage:', 'Sound Card:']
        os = processor = memory = graphics = directX = network = storage = soundCard = False
        booleanList = [os, processor, memory, graphics, directX, network, storage, soundCard]
        keyList = ['os', 'processor', 'memory', 'graphics', 'directX', 'network', 'storage', 'soundCard']
        for req in sysReqMinList:
            for i in range(len(booleanList)):
                if booleanList[i] == True:
                    sysReqMinDic[keyList[i]] = req.strip()
                    booleanList[i] = False
                if req == reqList[i]:
                    booleanList[i] = True
        if 'graphics' in sysReqMinDic.keys():
            print(sysReqMinDic['graphics'])
        sysReqRecList = sysReqRec.split('!!')
        sysReqRecDic = {}
        for req in sysReqRecList:
            for i in range(0, len(booleanList)):
                if booleanList[i] == True:
                    sysReqRecDic[keyList[i]] = req.strip()
                    booleanList[i] = False
                if req == reqList[i]:
                    booleanList[i] = True

        dataDic[name] = {'price':price, 'language':language, 'releasedMonth':releasedMonth, 'sysReqMin':sysReqMinDic, 'sysReqRec':sysReqRecDic}
    db.close()
    #print (dataDic)
    return [dataDic, nameList]

def CreateLanguage(rawMeat):
    languageList = rawMeat.splitlines()
    language = []
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

def feature(data):
    dataDic = data[0]
    nameList = data[1]
    featureDic = sysReqMinDic = sysReqRecDic = {}
    for name in nameList:
        price = dataDic[name]['price']
        languageList = dataDic[name]['language']
        sysReqMinDic = dataDic[name]['sysReqMin']
        sysReqRecDic = dataDic[name]['sysReqRec']
        languageCount = len(languageList)
        languagePopulation = countLanguagePopulation(languageList)
        if 'memory' in sysReqMinDic.keys():
            memory = getMemoryWeight(sysReqMinDic['memory'])
        else:
            memory = 0
        # print (memory)
        featureDic[name] = {'languageCount':languageCount, 'languagePopulation':languagePopulation}
    print (featureDic)

def countLanguagePopulation(languageList):
    population = 0
    billion = 10**9
    million = 10**6
    languagePopulationDic = {'English':1.12*billion, 'Chinese':1.1*billion, 'Spanish':512.9*million,
    'French':284.9*million, 'Russian':264.3*million, 'Portuguese':236.5*million,
    'Portuguese-Brazil':236.5*million , 'German':132*million, 'Japanese':128.3*million,
    'Turkish':78.9*million, 'Korean':77.2*million, 'Italian':67.8*million,
    'Thai':60.5*million, 'Polish':40.265*million, 'Ukrainian':32.948*million, 'Dutch':23.025*million, 'Finnish':5.789*million}
    tc = False
    for language in languageList:
        if language in languagePopulationDic.keys():
            population += languagePopulationDic[language]
        # if language == 'Traditional Chinese':
        #     population += 1.1*billion
        #     tc = True
        # if language == 'Simplified Chinese' and tc == False:
        #     population += 1.1*billion
        # FOR TESTING
        # if (language not in languageList) and (language != 'Traditional Chinese') and (language != 'Simplified Chinese'):
        #     print(language)
    return population

def getProcessorWeight(processor):
    return processor

def getMemoryWeight(memory):
    if memory.find('2'):
        return 0
    else:
        return 1

def getGraphicsWeight(graphics):
    return graphics

def getSysReqWeight(sysReqDic):
    processorWeight = getProcessorWeight(sysReqDic['processor'])
    memoryWeight = getMemoryWeight(sysReqDic['memory'])
    graphicsWeight = getGraphicsWeight(sysReqDic['graphics'])

print(feature(data()))
