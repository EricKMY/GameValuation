from flask import Flask, request, render_template

# from DataClassification.module.gameFeature import GameFeature
# from DataClassification.module.featureDigitalize import FeatureDigitalize
# from DataClassification.module.dataTraining import DataTraining

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('start.html')
    
@app.route('/a', methods=['GET', 'POST'])
def page_a():
    sold = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        about = request.form.get('short_introduction', '')
        introduction = request.form.get('introduction', '')
        tag = request.form.get('tag', '')
        language = request.form.get('language', '')
        price = request.form.get('price', '')
        view = request.form.get('view', '')

        targetList = [name, price, tag, language, introduction, about]
        #放進運算的function
        # trainFeature = GameFeature("localhost", "root", "5566", "steam", "steam_spy").Create()
        # trainData = FeatureDigitalize(trainFeature).Digitalize()
        # targetData = FeatureDigitalize(targetList).Digitalize()
        # coef, intercept, std, amin, amax, result = DataTraining(trainData, targetData).TrainAndTest()
        #sold = 結果
    return render_template('a.html', sold=sold)

if __name__ == '__main__':
    app.debug = True
    app.run()