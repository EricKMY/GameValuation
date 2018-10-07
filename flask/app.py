from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('start.html')
    
@app.route('/a', methods=['GET', 'POST'])
def page_a():
    sold = ''
    if request.method == 'POST':
        name = request.form.get('name', '')
        short_introduction = request.form.get('short_introduction', '')
        introduction = request.form.get('introduction', '')
        tag = request.form.get('tag', '')
        language = request.form.get('language', '')
        price = request.form.get('price', '')
        other = request.form.get('other', '')
        #放進運算的function
        #sold = 結果
    return render_template('a.html', sold=sold)

if __name__ == '__main__':
    app.debug = True
    app.run()