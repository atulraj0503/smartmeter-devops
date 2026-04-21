from flask import Flask, render_template, request

app = Flask(__name__)

meters = {
    "1001": {"units": 245, "bill": 1470, "status": "Online"},
    "1002": {"units": 120, "bill": 720, "status": "Offline"},
    "1003": {"units": 310, "bill": 1860, "status": "Online"}
}

@app.route("/", methods=["GET", "POST"])
def home():
    data = None
    if request.method == "POST":
        meter_id = request.form["meter_id"]
        data = meters.get(meter_id)
    return render_template("index.html", data=data)

@app.route("/admin")
def admin():
    total = len(meters)
    offline = sum(1 for m in meters.values() if m["status"] == "Offline")
    revenue = sum(m["bill"] for m in meters.values())
    return render_template("admin.html", total=total, offline=offline, revenue=revenue)

if __name__ == "__main__":
    app.run(debug=True)