from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/index.html')
def game():
    return render_template('index.html')

@app.route('/menu.html')
def menu_redirect():
    return render_template('menu.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
