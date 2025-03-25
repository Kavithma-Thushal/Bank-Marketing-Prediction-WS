import joblib
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# Load the model
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
        duration = float(request.form["duration"])
        campaign = float(request.form["campaign"])
        pdays = float(request.form["pdays"])
        previous = float(request.form["previous"])
        poutcome = request.form["poutcome"]
        emp_var_rate = float(request.form["emp_var_rate"])
        cons_price_idx = float(request.form["cons_price_idx"])
        cons_conf_idx = float(request.form["cons_conf_idx"])
        euribor3m = float(request.form["euribor3m"])
        nr_employed = float(request.form["nr_employed"])

        # Create an array for prediction input
        input_data = np.array([[age, job, marital, education, default, housing, loan, contact, month,
                                day_of_week, duration, campaign, pdays, previous, poutcome, emp_var_rate,
                                cons_price_idx, cons_conf_idx, euribor3m, nr_employed]])

        # Make prediction
        prediction = model.predict(input_data)

        # Render result
        result = "Yes" if prediction[0] == 1 else "No"
        return render_template("index.html", result=result)

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
