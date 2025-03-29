import joblib
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

# Load models
scaler = joblib.load("models/scaler.pkl")
label_encoders = joblib.load("models/encoder.pkl")
svm_model = joblib.load("models/svm_model.pkl")
lr_model = joblib.load("models/lr_model.pkl")

# Feature names
feature_names = [
    "age", "job", "marital", "education", "default", "housing", "loan", "contact",
    "month", "day_of_week", "duration", "campaign", "pdays", "previous",
    "poutcome", "emp_var_rate", "cons_price_idx", "cons_conf_idx", "euribor3m", "nr_employed"
]

# Categorical columns
categorical_columns = ["job", "marital", "education", "default", "housing", "loan",
                       "contact", "month", "day_of_week", "poutcome"]


@app.route("/", methods=["GET", "POST"])
def main():
    if request.method == "POST":
        try:
            # Extract form data
            data = request.form.to_dict()

            # Convert numeric features
            for feature in feature_names:
                if feature not in categorical_columns:
                    data[feature] = float(data.get(feature, 0))

            # Convert to DataFrame
            df = pd.DataFrame([data])

            # Apply label encoding for categorical features
            for col in categorical_columns:
                if col in df.columns and col in label_encoders:
                    df[col] = label_encoders[col].transform(df[col])
                else:
                    df[col] = 0

            # Ensure correct feature order
            df = df[feature_names]

            # Scale numeric features
            df_scaled = scaler.transform(df)

            # Get model choice from form
            model_choice = request.form.get("model_choice", "svm")

            # Make prediction with selected model
            if model_choice == "svm":
                prediction = svm_model.predict(df_scaled)
            elif model_choice == "lr":
                prediction = lr_model.predict(df_scaled)

            # Render result
            result = "Yes" if prediction[0] == 1 else "No"
            return render_template("index.html", result=result)

        except Exception as e:
            return f"Error: {str(e)}", 400

    return render_template("index.html", result=None)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
