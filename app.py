from flask import Flask, render_template
import os

from flask import request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy




app = Flask(__name__)

# Set up the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), unique=True, nullable=False)
    image_url = db.Column(db.Text, nullable=True)  # Image URL field
    content = db.Column(db.Text, nullable=False)  # Content field

@app.route('/', methods=['GET', 'POST'])
def index():
    posts = Post.query.all()  # Query all posts from the database
    return render_template('index.html', posts=posts)

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

@app.route('/post', methods=['POST', 'GET'])
def post():
    if request.method == 'POST':
        title = request.form.get('post-title')
        image_url = request.form.get('post-image')
        content = request.form.get('post-content')

        if title and content:
            new_post = Post(title=title, image_url=image_url, content=content)
            db.session.add(new_post)
            db.session.commit()
            return redirect(url_for('post_success'))  # Redirect to a success page or view

    # Handle GET request
    posts = Post.query.all()
    posts_list = [
        {
            'title': post.title,
            'image_url': post.image_url,
            'content': post.content
        }
        for post in posts
    ]
    return render_template('post.html', posts=posts_list)

@app.route('/postsuccess')
def post_success():
    return render_template('post_success.html')





if __name__ == '__main__':    
    with app.app_context():
        db.create_all()  # Create database tables
    app.run(debug=True)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)


