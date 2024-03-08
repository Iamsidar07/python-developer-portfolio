import smtplib

from flask import Flask, render_template, request, redirect, url_for, flash
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ["SECRET_KEY"]
EMAIL = os.environ["EMAIL"]
PASSWORD = os.environ["PASSWORD"]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        print("hello")
        msg = f"""
        Name: {request.form.get('name')}
        Email: {request.form.get('email')}
        Message: {request.form.get('message')}
"""
        send_email(message=msg, subject=request.form.get("subject"))
        flash(message="Message has been sent successfully!")
        return redirect(url_for("contact"))
    return render_template("contact.html")


def send_email(message, subject):
    with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL, PASSWORD)
        connection.sendmail(
            from_addr=EMAIL, to_addrs=EMAIL, msg=f"{subject}:\n\n{message}"
        )


if __name__ == "__main__":
    app.run(debug=True)
