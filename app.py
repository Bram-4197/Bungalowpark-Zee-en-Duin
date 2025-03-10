import os
from flask import Flask, flash, redirect, render_template, url_for
from forms import BungalowForm, NaamFormulier
from models import db, Bungalow



UPLOAD_FOLDER = 'static/uploads'
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db.init_app(app)

@app.before_request
def create_tables():
    db.create_all()

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
    bungalows = Bungalow.query.all()
    return render_template('bungalows.html', bungalows=bungalows)

@app.route("/bungalow/<naam>")
def bungalow(naam):
    return render_template('bungalow.html',  naam=naam)

@app.route('/welkom/<naam>')
def welkom(naam):
    return render_template('welkom.html', naam=naam)

@app.route('/bungalow/add', methods=['GET', 'POST'])
def add_bungalow():
    form = BungalowForm()
    if form.validate_on_submit():
        file = form.fileLocation.data
        filename = file.filename
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        new_bungalow = Bungalow(
            title=form.title.data, 
            aantalPersonen=form.aantalPersonen.data, 
            prijs=form.prijs.data, 
            fileLocation=filepath
        )
        db.session.add(new_bungalow)
        db.session.commit()
        flash('Bungalow added successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('add_bungalow.html', form=form)

@app.route('/bungalow/edit/<int:bungalow_id>', methods=['GET', 'POST'])
def edit_bungalow(bungalow_id):
    bungalow = Bungalow.query.get_or_404(bungalow_id)
    form = BungalowForm(obj=bungalow)
    if form.validate_on_submit():
        bungalow.title = form.title.data
        bungalow.aantalPersonen = form.aantalPersonen.data
        bungalow.prijs = form.prijs.data
        bungalow.fileLocation = form.fileLocation.data
        db.session.commit()
        flash('bungalow updated successfully!', 'success')
        return redirect(url_for('index'))
    return render_template('edit_bungalow.html', form=form, bungalow=bungalow)

@app.route('/bungalow/delete/<int:bungalow_id>')
def delete_bungalow(bungalow):
    bungalow = Bungalow.query.get_or_404(bungalow)
    db.session.delete(bungalow)
    db.session.commit()
    flash('Task deleted successfully!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
