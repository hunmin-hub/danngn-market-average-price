from flask import Flask, render_template, request
import main as proc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/search',methods=['POST'])
def search():
    product = request.form['input']
    button_count = request.form['choices-single-defaul']
    middle_price = proc.scrapping_market(product, int(button_count))
    if middle_price == int(-1):
        return render_template("warning.html")
    else:
        return render_template("search.html", searchingBy=product, searchingCt=button_count, searchingPrice=middle_price)
app.run(host="127.0.0.1")