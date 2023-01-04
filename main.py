import sys
import subprocess
from time import sleep
from flask import Flask, render_template

# Initiate All Startegies In Separate Processes Running In Parallel
subprocess.Popen([sys.executable, "Strategy1.py", ">>", "Strategy1.log"])
subprocess.Popen([sys.executable, "Strategy2.py", ">>", "Strategy2.log"])
subprocess.Popen([sys.executable, "Strategy3.py", ">>", "Strategy3.log"])
subprocess.Popen([sys.executable, "Strategy4.py", ">>", "Strategy4.log"])
subprocess.Popen([sys.executable, "Strategy5.py", ">>", "Strategy5.log"])

app = Flask(__name__)


@app.route("/<strategy>")
def index(strategy):
    return render_template("index.html", strategy=strategy)


@app.route("/stream/<strategy>")
def stream(strategy):
    def generate():
        with open(f"{strategy}.log") as f:
            while True:
                yield f.read()
                sleep(1)

    return app.response_class(generate(), mimetype="text/plain")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    """
    Visit http://127.0.0.1:5000/Strategy1 to view Strategy1 logs streaming
    Visit http://127.0.0.1:5000/Strategy2 to view Strategy2 logs streaming
    Visit http://127.0.0.1:5000/Strategy3 to view Strategy3 logs streaming
    Visit http://127.0.0.1:5000/Strategy4 to view Strategy4 logs streaming
    Visit http://127.0.0.1:5000/Strategy5 to view Strategy5 logs streaming
    """
