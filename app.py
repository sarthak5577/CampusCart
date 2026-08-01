from flask import Flask, render_template, request
import sqlite3


app = Flask(__name__)


@app.route("/")
def home():

    return render_template("index.html")



@app.route("/login")
def login():

    return render_template("login.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]
        college = request.form["college"]
        year = request.form["year"]
        branch = request.form["branch"]


        connection = sqlite3.connect("campuscart.db")

        cursor = connection.cursor()


        cursor.execute("""
        INSERT INTO users
        (name, email, password, college, year, branch)

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (name, email, password, college, year, branch))


        connection.commit()

        connection.close()


        return "Registration Successful"



    return render_template("register.html")



if __name__ == "__main__":

    app.run(debug=True)