from flask import Flask, render_template
# from flask_vite import Vite
from flask_inertia import Inertia
from react import render

app = Flask(__name__, static_folder='static', static_url_path='/static')
# vite = Vite(app)

INERTIA_TEMPLATE = 'index.html'
inertia = Inertia(app)

@app.route("/")
def home():
    return render('Index', {
        'name' : 'Marjon'
    })

@app.route("/anotherPage")
def another():
    return render('AnotherPage', {})


@app.route("/static_page")
def staticPage():
    return app.send_static_file("index.html")
