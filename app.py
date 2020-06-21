from flask import Flask, render_template, request
from flask_cors import CORS,cross_origin
import pickle

app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
    return render_template('index.html')

@app.route('/prediction', methods = ['GET','POST'])
@cross_origin()
def predict():
    if request.method == 'POST':
        try:

            greScroe = float(request.form['greScore'])
            toeflScore = float(request.form['toeflScore'])
            univRating = float(request.form['univRating'])
            sop = float(request.form['sop'])
            lor = float(request.form['lor'])
            cgpa = float(request.form['cgpa'])
            is_research = request.form['research']
            research = [1 if is_research == 'yes' else 0][0]

            # Read Pickle File 
            filename = 'linear_model.pickle'
            loaded_model = pickle.load(open(filename, 'rb')) # loading the model file from the storage

            prediction=loaded_model.predict([[greScroe,toeflScore,univRating,sop,lor,cgpa,research]])
            
            # showing the prediction results in a UI
            return render_template('result.html',prediction=round(100*prediction[0]))
            
        except:
            'Error'
    else:
        return 'Nothing'

if __name__ == '__main__':
    app.run(debug = True)