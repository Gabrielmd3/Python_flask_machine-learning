from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
  return render_template("index.html")

@app.route("/classificador2")
def classificador2():
  return render_template("classificador2.html")

@app.route("/classificador3")
def classificador3():
  return render_template("classificador3.html")

@app.route("/classificador4")
def classificador4():
  return render_template("classificador4.html")


if __name__ == "__main__":
  app.run(debug=True)
