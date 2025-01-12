from flask import Flask, render_template, request, redirect
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000"

# Pagina principală
@app.route("/")
def index():
    # Preluăm datele de la backend
    response = requests.get(f"{API_URL}/data")
    if response.status_code == 200:
        data = response.json()
    else:
        data = []
    return render_template("index.html", data=data)

# Simulează datele pentru un pacient
@app.route("/simulate", methods=["POST"])
def simulate():
    patient_id = request.form.get("patient_id")
    if patient_id:
        response = requests.get(f"{API_URL}/sensor/{patient_id}/data")
        if response.status_code == 200:
            return redirect("/")
    return "Eroare la simulare", 400

if __name__ == "__main__":
    app.run(debug=True)
