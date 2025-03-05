from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        # Dummy check
        if username == "farmer" and password == "market":
            flash("Login Successful!", "success")
            return redirect(url_for("home"))
        else:
            flash("Invalid Credentials", "danger")
    return render_template("login.html")

@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        flash("Signup Successful! Please login.", "success")
        return redirect(url_for("login"))
    return render_template("signup.html")

if __name__ == "__main__":
    app.run(debug=True)
