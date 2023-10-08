from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def inicio():
    return render_template('inicio.html')

@app.route('/acerca-de')
def acerca_de():
    return render_template('acerca_de.html')

if __name__ == '__main__':
    app.run(debug=True)