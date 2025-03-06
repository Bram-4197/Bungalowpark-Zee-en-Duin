from flask import Flask, redirect, render_template, url_for
from forms import NaamFormulier

app = Flask(__name__)



app.secret_key = "test"



@app.route('/')
def index():
    return render_template('index.html')


@app.route("/ons")
def ons():
    return render_template("over-ons.html")

@app.route('/formulier', methods=['GET', 'POST'])
def formulier():
    form = NaamFormulier()
    if form.validate_on_submit():
        naam = form.naam.data
        return redirect(url_for('welkom', naam=naam))
    return render_template('formulier.html', form=form)

@app.route("/bungalows")
def bungalows():
    return render_template('bungalows.html')

@app.route("/bungalow/<naam>")
def bungalow(naam):
    return render_template('bungalow.html',  naam=naam)

@app.route('/welkom/<naam>')
def welkom(naam):
    return render_template('welkom.html', naam=naam)

if __name__ == '__main__':
    app.run(debug=True)
