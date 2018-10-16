from flask import Flask, request, render_template

from DataClassification.module.gameFeature import GameFeature
from DataClassification.module.targetFeature import TargetFeature
from DataClassification.module.featureDigitalize import FeatureDigitalize
from DataClassification.module.dataTraining import DataTraining

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('start.html')
    
@app.route('/a', methods=['GET', 'POST'])
def page_a():
    sold = ''
    name = ''
    about = ''
    introduction = ''
    tag = ''
    language = []
    price = ''
    view = ''

    if request.method == 'POST':
        name = request.form.get('name', '')
        about = request.form.get('about', '')
        introduction = request.form.get('introduction', '')
        tag = request.form.get('tag', '')
        language = request.form.getlist('language')
        price = request.form.get('price', '')
        view = request.form.get('view', '')

        targetList = [name, price, tag, language, introduction, about, view]
        #放進運算的function
        trainFeature = GameFeature("localhost", "root", "5566", "steam", "steam_spy").Create()
        targetFeature = TargetFeature(targetList).Create()
        trainData = FeatureDigitalize(trainFeature).Digitalize()
        targetData = FeatureDigitalize(targetFeature).Digitalize()
        sold = DataTraining(trainData, targetData).TrainAndPredict()
        # sold = targetList
    return render_template('a.html', sold=sold, name=name, about=about, introduction=introduction, tag=tag, language=language, price=price, view=view)

if __name__ == '__main__':
    app.debug = True
    app.run()