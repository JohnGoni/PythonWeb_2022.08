import os
#from unittest import result
from flask import Flask, render_template, request
import pandas as pd

carcent_list = pd.read_csv("C:/Workspace/01.PythonWeb/00.Project_1/00.Project_1/static/광주__�동�ݨ정비업��_csv")

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')


@app.route('/function', methods=['GET','POST'])
def input():
    if request.method == 'POST':
        val = request.form['주소']
        f_image = request.files['image']
        fname= f_image.filename
        filename= os.path.join(app.static_folder,'upload/')+fname
        f_image.save(filename)
        return render_template('output.html', result=val, fname=fname)
    else:
        return render_template('input.html')


@app.route('/center_list', methods=['GET','POST'])
def center_list():
    car_list=carcent_list.to_dict('list')
    manu_list = ['장소', '도로명주소', '위도', '경도']
    car_dic = {}
    for j in range(len(car_list['장소'])):
        a = []
        for i in manu_list:
            a.append(car_list[i][j])
        car_dic[j] = a

    carcenter=car_dic

    if request.method=='POST':

        return render_template('map.html', result=carcenter)
        
    else:
        return render_template('carcenter_list.html', result=carcenter)
        

        





@app.route('/oil', methods=['GET','POST'])
def expend_list():
    return render_template('oil.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
