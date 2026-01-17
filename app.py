from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/") 
#Route to Home page 
def home():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #Later: Authentication Logic
        email = request.form["email"]
        password = request.form["password"]

    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True)