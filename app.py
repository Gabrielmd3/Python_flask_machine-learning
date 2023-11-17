from flask import Flask, render_template, request
import ml

app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
  if request.method == "POST":
    req = request.form
    classificador = req["dropdownClassifier"]
    parametro1 = (req["parametro1"])
    parametro2 = (req["parametro2"])
    rs = (req["random_state"])
    accuracy, precision, recall, f1 = ml.machine_learning(classificador, parametro1, parametro2, rs)
    exibir_imagem = True
    return render_template("index.html", img="displayimg.png", exibir_imagem=exibir_imagem, accuracy=accuracy, precision=precision,
                            recall=recall, f1=f1)
  return render_template("index.html")

if __name__ == "__main__":
  app.run(debug=True)
