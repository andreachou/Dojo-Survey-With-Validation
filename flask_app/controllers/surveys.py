from server import app
from flask import render_template, session, request, redirect
from flask_app.models.survey import Dojo


@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process():
    # session['name'] = request.form['name']
    # session['location'] = request.form['location']
    # session['language'] = request.form['language']
    # session['comments'] = request.form['comments']

    # validation
    if not Dojo.validate_dojo(request.form):
        return redirect("/")
    Dojo.save(request.form)
    return redirect("/result")

@app.route('/result')
def display_result():
    return render_template("result.html", dojo=Dojo.get_last_one())