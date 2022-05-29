from flask import Flask, request, render_template
import pickle
model = pickle.load(open('linear_model2.pkl', 'rb'))

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/prediction', methods=['POST'])
def prediction():
    output = 0
    params = []
    fields = []
    if request.method == 'POST':
        price = float(request.form['price'])
        kms = int(request.form['kms'])
        ow = int(request.form['owner'])

        fuel = request.form['fuel']
        if fuel == 'Petrol':
            Fuel_Type_Petrol = 1
            Fuel_Type_Diesel = 0
        elif fuel == 'Diesel':
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 1
        else:
            Fuel_Type_Petrol = 0
            Fuel_Type_Diesel = 0

        seller = request.form['seller']
        if seller == 'Individual':
            Seller_Type_Individual = 1
        else:
            Seller_Type_Individual = 0

        trans = request.form['trans']
        if trans == 'Manual':
            Transmission_Manual = 1
        else:
            Transmission_Manual = 0

        age = int(request.form['age'])

        output = model.predict([[price, kms, ow, Fuel_Type_Diesel, Fuel_Type_Petrol,
                               Seller_Type_Individual, Transmission_Manual, age]])
    return render_template('result.html', number="You can sell your car for {output} Lakhs".format(output=round(output[0], 2)))


if __name__ == '__main__':
    app.run(debug=True)
