# importing os for setting path
import os

working_dir = 'E:\\Great Learning\\DL\\Capstone\\Data\\'

os.chdir(working_dir)

# Suppress warnings
import warnings; warnings.filterwarnings('ignore')

import fasttext
def fasttextmodelload():
    fasttxtmodel = fasttext.load_model('ft_model_Potential.bin')
    return fasttxtmodel


def fasttxtpotentialacclvl_predict(x):
    model = fasttextmodelload()
    pred = model.predict(x)
    return pred


#test
prediction = fasttxtpotentialacclvl_predict("The collaborator reports that he was working in the UstulaciÃ³n and realized that the cyclone duct was obstructed and opened the door to try to unclog the same and the material detached and projected towards the employee causing small burn in the right heel.")

import json

jsonObj = json.dumps(prediction[0])
print(jsonObj)

from flask import Flask, request, json, render_template, jsonify

app = Flask(__name__)  # ,static_url_path='/'


# @app.route('/hello')
# def index():
#    return render_template('index.html',name='John')  #{'hello': 'world'}


@app.route('/get_p_acc_lvl', methods=['GET'])
def get_potential_accident_level():
    query_parameters = request.args

    acc_desc = query_parameters.get('description')

    prediction = fasttxtpotentialacclvl_predict(acc_desc)  # ft.predict('acc_desc')
    # prediction = "Employee was sitting in the resting area at level 326 (raise bore), when he suffered sudden illness, falling and suffering excoriation on the face."

    print(acc_desc)

    # pred = json.dumps(prediction[0])
    # print(pred)
    pred = str(prediction[0])

    if pred == "('__label__3',)":
        pred = "Potential accident level: 3"
    elif pred == "('__label__1',)":
        pred = "Potential accident level: 1"
    elif pred == "('__label__2',)":
        pred = "Potential accident level: 2"
    elif pred == "('__label__4',)":
        pred = "Potential accident level: 4"
    elif pred == "('__label__5',)":
        pred = "Potential accident level: 5"

    return jsonify(pred)


if __name__ == '__main__':
    app.run()