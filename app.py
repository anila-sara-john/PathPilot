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

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]

        return render_template(
            "message.html",
            title="Registration Successful",
            message=f"Thank you {name}, your account has been created."
        )

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)
