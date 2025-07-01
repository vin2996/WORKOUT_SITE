from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/presentation')
def presentation():
    return render_template('presentation.html')

@app.route('/nutrition')
def nutrition():
    return render_template('nutrition.html') 

if __name__ == '__main__':
    app.run(debug=True)
