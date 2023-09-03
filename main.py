
# Find a live correction of this exercise here : https://www.youtube.com/watch?v=G_1apUGUF38
import pickle
from flask import Flask, render_template, request
import requests
app = Flask(__name__)
model = pickle.load(open("model.sav", "rb"))
@app.route('/', methods=['GET'])
def california_index():
	return render_template("index.html")
@app.route('/predict/', methods=['POST'])
def result():
	if request.method == 'POST':
		MedInc = float(request.form['MedInc'])
		HouseAge = float(request.form['HouseAge'])
		AveRooms = float(request.form['AveRooms'])
		AveBedrms = float(request.form['AveBedrms'])
		Population = float(request.form['Population'])
		AveOccup = float(request.form['AveOccup'])
		Latitude = float(request.form['Latitude'])
		Longitude = float(request.form['Longitude'])	
	reg = model.predict([[MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude]])
	return render_template("prediction.html", price=reg)
if __name__ == '__main__':
    app.debug = True
    app.run(
        host='0.0.0.0',
        port=5000,
        debug=True)
