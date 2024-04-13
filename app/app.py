from flask import Flask, render_template, request, jsonify
import tensorflow as tf
import keras
import os
import numpy as np
import pandas as pd
from collections import Counter 
import boto3

app = Flask(__name__, template_folder='templates')

model_path = os.path.join(os.getcwd(), 'C:/Users/rammy/OneDrive/Documents/CentennialCollege/4th Semester/Software Project/final project/COMP313-002-Winter2024-Team6---Credit-Card-Fraud-Detection/app/optimal_model_ann.h5')
model = keras.models.load_model(model_path)
#"C:/COMP313-002-Winter2024-Team6---Credit-Card-Fraud-Detection/app/optimal_model_ann.h5"

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/loading')
def loading():
    return render_template('load.html')

@app.route('/upload', methods=['POST'])
def predict():
    #Comment from line 27 to 53 to avoid calling the AWS cuket. Substitute the pred_string with a static value
    # Initialize a Boto3 S3 client
    s3 = boto3.client('s3')
    bucket_name = 'contentcen301275725.aws.ai'
    object_key = 'fraud_data_b.csv'
    

    # Generate an HTTP GET request to retrieve the file
    try:
        response = s3.get_object(Bucket=bucket_name, Key=object_key)
    except s3.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        print(f"Failed to download file: {error_code}")
        return None

    # Load the CSV file into a DataFrame
    df = pd.read_csv(response['Body'])
      
    if df is not None:
        predictions = model.predict(df) 
        fraud_count = 0
        non_fraud_count = 0
        for prediction in predictions:
            if prediction > 0.5:
                fraud_count += 1
            else:
                non_fraud_count += 1

    pred_string = f"{fraud_count} instances of fraud detected. "
    # return render_template('home.html', prediction=pred_string)
    return jsonify({"prediction": pred_string})


@app.route('/prediction')
def prediction():
    prediction = request.args.get('prediction', '')
    return render_template('result.html', prediction=prediction)       

if __name__ == '__main__':
    app.run(debug=True)
