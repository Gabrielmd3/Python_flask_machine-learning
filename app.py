from flask import Flask, render_template, request
import ml

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
  if request.method == "POST":
    req = request.form
    parametro1 = (req["parametro1"])
    rs = (req["random_state"])
    parametro2 = (req["parametro2"])
    classificador = req["dropdownClassifier"]
    accuracy, precision, recall, f1 = ml.machine_learning(classificador, parametro1, parametro2, rs)
    e = True
    return render_template("index.html", e=e, precision=precision,
                            recall=recall, accuracy=accuracy, f1=f1, img="displayimg.png",)
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)
