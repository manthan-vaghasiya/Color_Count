from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
import os 
import data

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jhasdgfhbdj654321sdkjfjdsbn'
bootstrap = Bootstrap5(app)

@app.route('/', methods=['GET', 'POST'])
def home():
    file_path = os.path.join(path, 'kkkk.jpg')
    hex_data, perc_data = data.main(file_path)
    if request.method == 'POST':
        file = request.files['myFile']
        if file:
            file_path = os.path.join(path, file.filename)
            file.save(file_path)
            hex_data, perc_data = data.main(file_path)
            return render_template('index.html', hex_data=hex_data, perc_data=perc_data, file_path=file_path)
    return render_template('index.html', hex_data=hex_data, perc_data=perc_data, file_path=file_path)

if __name__ == '__main__':
    path = 'static/img'
    if not os.path.exists(path):
        os.makedirs(path)
    app.run(debug=True)