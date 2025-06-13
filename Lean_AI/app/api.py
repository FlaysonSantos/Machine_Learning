
from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('modelo/modelo.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    features = np.array([[
        data['volume'],
        data['tempo_ciclo'],
        data['refugo_pct']
    ]])
    prediction = model.predict(features)
    result = 'Anomalia' if prediction[0] == -1 else 'Normal'
    return jsonify({'resultado': result})

if __name__ == '__main__':
    app.run(debug=True)
