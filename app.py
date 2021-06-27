import numpy as np 
from flask import Flask , request , render_template
import pickle 

app = Flask(__name__)
model = pickle.load(open('model.pkl' , 'rb'))

@app.route('/')
def home():
    return  render_template("index.html")

@app.route("/predict" , methods = ['POST'])

def predict():
    float_features = [float(x) for x in request.form.values()]
    final_features = [np.array(float_features)]
    prediction = model.predict(final_features)
    

    output = round(prediction[0] , 2)
    dict1  = {1 :"Building windows float processed" , 2 :"Building windows non float processed" , 3 :"Vehicle windows float processed" , 4 :"Vehicle windows non float processed" , 5: "Containers" , 6 :"Tableware" , 7 :"Headlamps" }
    return render_template('index.html', prediction_text='The type of glass is {} '.format(dict1[output]))
 
                           
if __name__ == '__main__':
    app.run(debug=True)