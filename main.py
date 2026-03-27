from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def json():
    marks={
        "Rohan":55,
        "Tasnim":50,
        "Reshmita":60,
        "Vipul":77,
        "Raj":60
    }
    values=[1,marks,55]
    return jsonify(values)


app.run(debug=True)