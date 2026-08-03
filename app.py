from flask import Flask, render_template, request, session, redirect
import sqlite3

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)

app.secret_key = "campuscart_secret_key"



@app.route("/")
def home():

    return render_template("index.html")



@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]

        email = request.form["email"]

        password = generate_password_hash(
            request.form["password"]
        )

        phone = request.form["phone"]

        college = request.form["college"]

        year = request.form["year"]

        branch = request.form["branch"]


        connection = sqlite3.connect("campuscart.db")

        cursor = connection.cursor()


        cursor.execute("""
        INSERT INTO users
        (name, email, password, phone, college, year, branch)

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            name,
            email,
            password,
            phone,
            college,
            year,
            branch
        ))


        connection.commit()

        connection.close()


        return "Registration Successful"


    return render_template("register.html")





@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]


        connection = sqlite3.connect("campuscart.db")

        cursor = connection.cursor()


        cursor.execute(
            "SELECT * FROM users WHERE email = ?",
            (email,)
        )


        user = cursor.fetchone()


        connection.close()



        if user and check_password_hash(user[3], password):


            session["user_id"] = user[0]

            session["user_name"] = user[1]

            return redirect("/")


        else:

            return "Invalid Email or Password"



    return render_template("login.html")




@app.route("/logout")
def logout():

    session.clear()

    return redirect("/")

@app.route("/sell", methods=["GET", "POST"])
def sell():

    if "user_id" not in session:

        return redirect("/login")


    if request.method == "POST":


        name = request.form["name"]

        category = request.form["category"]

        price = request.form["price"]

        description = request.form["description"]

        condition = request.form["condition"]



        connection = sqlite3.connect("campuscart.db")

        cursor = connection.cursor()



        cursor.execute("""
        INSERT INTO products
        (user_id, name, category, price, description, condition)

        VALUES (?, ?, ?, ?, ?, ?)

        """,
        (
            session["user_id"],
            name,
            category,
            price,
            description,
            condition
        ))



        connection.commit()

        connection.close()



        return "Product Added Successfully"



    return render_template("sell.html")

if __name__ == "__main__":

    app.run(debug=True)