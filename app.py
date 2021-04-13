
import keras
import numpy as np
from flask import Flask, request, jsonify, render_template
from sklearn.preprocessing import StandardScaler
from DataTransformation import scaler
app = Flask(__name__, template_folder='template')
model = keras.models.load_model('C:/Users/acer/Desktop/Web App/model/model.h5')

# Bind home function to URL
@app.route('/')
def home():
    return render_template('HeartDiseaseClassifier.html')

# Bind predict function to URL
@app.route('/predict', methods =['POST'])
def predict():
    
    # Put all form entries values in a list 
    features = [float(i) for i in request.form.values()]
    # Convert features to array
    array_features = np.array(features).reshape(1,13)
    array_features = scaler(array_features)

    

    # Predict features
    prediction = model.predict(array_features)
    categories = [0,1]
    prediction = categories[np.argmax(prediction)]
    
    output = prediction
    
    # Check the output values and retrive the result with html tag based on the value
    if output == 1:
        return render_template('HeartDiseaseClassifier.html', 
                               result = 'The patient is not likely to have heart disease!')
    else:
        return render_template('HeartDiseaseClassifier.html', 
                               result = 'The patient is likely to have heart disease!')

if __name__ == '__main__':
#Run the application
    app.run()

