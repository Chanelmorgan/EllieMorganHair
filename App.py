from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'chanelmorgan01@gmail.com'
app.config['MAIL_PASSWORD'] = 'nduzrdzaqykuslkf'  # Use the App Password here
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_DEFAULT_SENDER'] = 'chanelmorgan01@gmail.com'
app.config['SECRET_KEY'] = os.urandom(24)  # Random secret key for session management

mail = Mail(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(subject='New Contact Form Submission',
                      recipients=['chanelmorgan01@gmail.com'],
                      body=f'Name: {name}\nEmail: {email}\nMessage: {message}',
                      reply_to=email)

        try:
            mail.send(msg)
            flash('Thank you for your message! We will get back to you soon.', 'success')
        except Exception as e:
            flash(f'An error occurred while sending your message: {str(e)}', 'danger')
        return redirect(url_for('contact'))

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)