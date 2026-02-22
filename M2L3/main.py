from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/anasayfa')
def index2():
    return render_template('index.html')

@app.route('/hava')
def weather():
    return render_template('havadurumu.html')

if __name__ == "__main__":
    app.run(debug=True)