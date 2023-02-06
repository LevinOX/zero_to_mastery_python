from flask import Flask, render_template, url_for  # , redirect

app = Flask(__name__)


@app.route("/")
def hello_world():
    print(url_for('static', filename='bear.ico'))
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
