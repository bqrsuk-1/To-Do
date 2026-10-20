from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ToDo.db"
db = SQLAlchemy



@app.route("/")
def main():
    return render_template("main.html")

@app.route("/ToDo")
def To_Do():
    return render_template("ToDo.html")

if __name__ == "__main__":
    app.run(debug = True)
