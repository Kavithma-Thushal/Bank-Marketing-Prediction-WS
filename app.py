import warnings
import joblib
import numpy as np
from flask import Flask, render_template, request

# Ignore warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

# Load the models
scaler = joblib.load("models/scaler.pkl")
label_encoders = joblib.load("models/encoder.pkl")
model = joblib.load("models/svm_model.pkl")


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        age = float(request.form["age"])
        job = request.form["job"]
        marital = request.form["marital"]
        education = request.form["education"]
        default = request.form["default"]
        housing = request.form["housing"]
        loan = request.form["loan"]
        contact = request.form["contact"]
        month = request.form["month"]
        day_of_week = request.form["day_of_week"]
        # poutcome = request.form["poutcome"]
        # duration = float(request.form["duration"])
        # campaign = float(request.form["campaign"])
        # pdays = float(request.form["pdays"])
        # previous = float(request.form["previous"])
        # emp_var_rate = float(request.form["emp_var_rate"])
        # cons_price_idx = float(request.form["cons_price_idx"])
        # cons_conf_idx = float(request.form["cons_conf_idx"])
        # euribor3m = float(request.form["euribor3m"])
        # nr_employed = float(request.form["nr_employed"])

        # Preprocess the categorical input data using label encoders
        job = label_encoders['job'].transform([job])[0]
        marital = label_encoders['marital'].transform([marital])[0]
        education = label_encoders['education'].transform([education])[0]
        default = label_encoders['default'].transform([default])[0]
        housing = label_encoders['housing'].transform([housing])[0]
        loan = label_encoders['loan'].transform([loan])[0]
        contact = label_encoders['contact'].transform([contact])[0]
        month = label_encoders['month'].transform([month])[0]
        day_of_week = label_encoders['day_of_week'].transform([day_of_week])[0]
        # poutcome = label_encoders['poutcome'].transform([poutcome])[0]

        # Create an array for prediction input
        input_data = np.array([[age, job, marital, education, default, housing, loan, contact, month,
                                day_of_week]])

        # Scale the input data using scaler
        input_data_scaled = scaler.transform(input_data)

        # Make prediction
        prediction = model.predict(input_data_scaled)

        # Render result
        result = "Yes" if prediction[0] == 1 else "No"
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
