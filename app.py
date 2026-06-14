from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    result = ""

    if request.method == 'POST':

        distance = float(request.form['distance'])
        electricity = float(request.form['electricity'])

        carbon_score = (distance * 0.21) + (electricity * 0.5)

        result = f"Estimated Carbon Score: {carbon_score:.2f} kg CO2"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)