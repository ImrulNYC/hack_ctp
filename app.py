from flask import Flask, render_template
import os

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
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
