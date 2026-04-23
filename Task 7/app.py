from flask import Flask, jsonify, request, send_from_directory, redirect
import datetime
import base64
import random

app = Flask(__name__)

@app.route("/")
def index():
    return send_from_directory("static", "index.html")
@app.route("/hello/<name>")
def hello(name):
    return jsonify({"msg" : f"Hello {name}!"})
@app.route("/time")
def time():
    now = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return jsonify({"time" : f"The time is:  {now} "})


@app.route("/mot")
def mot():
    ms= ["Keep going and it doesnt matter where you are right now.", "Some days a smile is enough.","Today is beautiful like you.","Youre doing amazing!"]
    mb = random.choice(ms)
    return jsonify({"dday": f"For todays quote: {mb}"})


@app.route("/base64/encode", methods=["POST"])
def encode():
    data =request.json.get("data")
    encoded = base64.b64decode(data.encode()).decode()
    return jsonify({"data":encoded})

@app.route("/base64/encode", methods=["POST"])
def decode():
    data =request.json.get("data")
    decoded=base64.b64decode(data).decode()
    return jsonify({"data":decoded})


@app.route("/cat/<int:status_code>")
def cat(status_code):
    return redirect(f"https://http.cat/{status_code}", code=302)

@app.route("/cat/402")
def cat1():
    return redirect("https://http.cat/402", code=302)

if __name__ == "__main__":
    app.run(debug=True)


