from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.utils import redirect

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///ToDo.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db: SQLAlchemy = SQLAlchemy(app)
app.app_context().push()

class ToDos(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.Text, nullable = False)
    status = db.Column(db.String, nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)

@app.route("/")
def main():
    todos = ToDos.query.order_by(ToDos.created_at.desc()).all()
    return render_template("main.html", todos=todos)

@app.route("/ToDo", methods=["POST","GET"])
def To_Do():
    if request.method =="POST":
        name = request.form.get("name", "").strip()

        if not name:
            return render_template("ToDo.html", error="Please enter at least something, better with idea!")

        todo = ToDos(name = name, status  = "Planned")

        try:
            db.session.add(todo)
            db.session.commit()
            return redirect("/")
        except:
            return "Error"
    else:
        return render_template("ToDo.html")

@app.route("/update/<int:id>", methods=["POST"])
def update_status(id):
    todo = ToDos.query.get_or_404(id)
    new_status = request.form.get("status")

    if new_status:
        todo.status = new_status
        try:
            db.session.commit()
        except:
            return "Error"

    return redirect("/")

@app.route("/delete/<int:id>", methods=["POST"])
def delete_task(id):
    todo = ToDos.query.get_or_404(id)

    try:
        db.session.delete(todo)
        db.session.commit()
        return redirect("/")
    except:
        return "Error"

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug = True)
