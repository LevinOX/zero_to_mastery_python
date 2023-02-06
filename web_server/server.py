from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/<string:username>/<int:post_id>")
def hello_world(username=None, post_id=None):
    print(url_for('static', filename='bear.ico'))
    return render_template('index.html', name=username, post_id=post_id)


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/blog")
def blog():
    return "<p>These are my thoughts on blogs.</p>"


@app.route("/blog/2020/dog")
def blog2():
    return "<p>My dog.</p>"


# @app.route("/favicon.ico")
# def blog2():
#     return "<p>My dog.</p>"

# $ flask --app server --debug run
