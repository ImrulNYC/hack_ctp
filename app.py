from flask import Flask, render_template
import os

from flask import request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///subscribers.db'
db = SQLAlchemy(app)
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            new_subscriber = Subscriber(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            return jsonify({'status': 'success', 'message': 'Thank you for subscribing!'})
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
@app.route('/subscribe', methods=['GET', 'POST'])
def subscribe():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            new_subscriber = Subscriber(email=email)
            db.session.add(new_subscriber)
            db.session.commit()
            return redirect(url_for('success'))
    return render_template('index.html')

@app.route('/success')
def success():
    return render_template('success.html')






if __name__ == '__main__':    
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


