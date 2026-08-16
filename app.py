from flask import Flask, render_template, request
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app = Flask(
    __name__,
    template_folder=os.path.join(BASE_DIR, "templates")
)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cards")
def cards():
    return render_template("cards.html")

@app.route("/schemes")
def schemes():
    return render_template("schemes.html")

@app.route("/helpline")
def helpline():
    return render_template("helpline.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")

        print("New Message:", name, email, message)
        return render_template("contact.html")

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
