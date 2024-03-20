from flask import Flask, render_template, request
import tensorflow as tf
import keras
import os
import numpy as np
import pandas as pd
from collections import Counter 

app = Flask(__name__, template_folder='templates')

# Load your pre-trained model
model_path = os.path.join(os.getcwd(), 'C:/Users/rammy/OneDrive/Documents/CentennialCollege/4th Semester/Software Project/Project/app/optimal_model_ann.h5')
model = keras.models.load_model(model_path)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        df = pd.read_csv(file)
        predictions = model.predict(df) 

        fraud_count = 0
        non_fraud_count = 0
        for prediction in predictions:
            if prediction > 0.5:
                fraud_count += 1
            else:
                non_fraud_count += 1
        pred_string = f"{fraud_count} instances of fraud detected. "
        return render_template('index.html', prediction=pred_string)


        

if __name__ == '__main__':
    app.run(debug=True)
