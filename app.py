from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/food')
def food():
    return render_template('food.html')

@app.route('/education')
def education():
    return render_template('education.html')

@app.route('/mental_health')
def mental_health():
    return render_template('mental_health.html')

@app.route('/security')
def security():
    return render_template('security.html')

if __name__ == '__main__':
    app.run(debug=True)
