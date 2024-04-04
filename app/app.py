from flask import Flask, render_template, request
import tensorflow as tf
import keras
import os
import numpy as np
import pandas as pd
from collections import Counter 

app = Flask(__name__, template_folder='templates')


# Load your pre-trained model
model_path = os.path.join(os.getcwd(), 'C:/COMP313-002-Winter2024-Team6---Credit-Card-Fraud-Detection/app/optimal_model_ann.h5')
model = keras.models.load_model(model_path)
#"C:/COMP313-002-Winter2024-Team6---Credit-Card-Fraud-Detection/app/optimal_model_ann.h5"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/loading')
def loading():
    return render_template('loading.html')

@app.route('/upload', methods=['POST'])
def predict():
    # if request.method == 'POST':
    #     file = request.files['file']
    #     df = pd.read_csv(file)
    #     predictions = model.predict(df) 

    #     fraud_count = 0
    #     non_fraud_count = 0
    #     for prediction in predictions:
    #         if prediction > 0.5:
    #             fraud_count += 1
    #         else:
    #             non_fraud_count += 1
    pred_string = f"{fraud_count} instances of fraud detected. "
    # return render_template('home.html', prediction=pred_string)
    return jsonify({"prediction": pred_string})


@app.route('/prediction')
def prediction():
    prediction = request.args.get('prediction', '')
    return render_template('result.html', prediction=prediction)       

if __name__ == '__main__':
    app.run(debug=True)
