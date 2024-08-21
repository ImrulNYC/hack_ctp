from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# A simple in-memory list to store subscribers (this is just for demonstration)
subscribers = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    if email not in subscribers:
        subscribers.append(email)
        # Here you would add code to send a confirmation email
        return f"Thank you for subscribing, {email}!"
    return "You are already subscribed!"

@app.route('/unsubscribe/<email>')
def unsubscribe(email):
    if email in subscribers:
        subscribers.remove(email)
        # Here you would add code to send an unsubscribe confirmation email
        return f"You have unsubscribed, {email}."
    return "Email not found."

if __name__ == '__main__':
    app.run(debug=True)
