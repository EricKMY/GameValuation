from flask import Flask, request, render_template
from DataClassification.module.gameFeature import GameFeature
from DataClassification.module.featureDigitalize import FeatureDigitalize
from DataClassification.module.dataTraining import DataTraining

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('start.html')
    
@app.route('/a', methods=['GET', 'POST'])
def page_a():
    sold = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        about = request.form.get('about', '')
        introduction = request.form.get('introduction', '')
        tag = request.form.get('tag', '')
        language = request.form.get('language', '')
        price = request.form.get('price', '')
        other = request.form.get('other', '')
        
        # tag = self.CreateTag(tag)
        # language = self.CreateLanguage(language)
        targetList = [name, about, introduction, tag, language, price, other]

        #放進運算的function
        trainFeature = GameFeature("localhost", "root", "5566", "steam", "steam_spy").Create()
        trainData = FeatureDigitalize(trainFeature).Digitalize()
        coef, intercept, std, amin, amax, result = DataTraining(trainData, trainData).TrainAndTest()
        #sold = 結果
    return render_template('a.html', sold=sold)

if __name__ == '__main__':
    app.debug = True
    app.run()

# def __init__(self, rawMeat):
#     self.rawMeat = rawMeat

# def CreateTag(self):
#     tagList = rawMeat.split(',')
#     return tagList

# def CreateLanguage(self):
#     languageList = rawMeat.split(',')
#     return languageList