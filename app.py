from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # Needed for flash messages

# Route for the registration page
@app.route("/", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        confirm_password = request.form["confirm_password"]

        # Basic validation
        if not name or not email or not password or not confirm_password:
            flash("All fields are required!")
            return redirect(url_for("register"))
        if password != confirm_password:
            flash("Passwords do not match!")
            return redirect(url_for("register"))

        # Optionally, save to a file or database
        with open("users.txt", "a") as f:
            f.write(f"Name: {name}, Email: {email}\n")

        flash("Registration successful!")
        return redirect(url_for("register"))

    return render_template("register.html")

if __name__ == "__main__":
    app.run(debug=True)

