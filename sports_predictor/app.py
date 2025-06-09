from flask import Flask, render_template, request
import random

app = Flask(__name__)

SPORTS = ['Soccer', 'Baseball', 'Basketball']

@app.route('/')
def index():
    return render_template('index.html', sports=SPORTS)

@app.route('/predict', methods=['POST'])
def predict():
    sport = request.form.get('sport')
    team1 = request.form.get('team1')
    team2 = request.form.get('team2')
    prediction = random.choice([team1, team2])
    return render_template('prediction.html', sport=sport, team1=team1, team2=team2, prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
