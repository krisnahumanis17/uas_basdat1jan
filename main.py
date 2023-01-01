from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
@app.route("/product")
def shop():
    return render_template("shop.html")

@app.route("/cart")
def cart():
    return render_template("cart.html")