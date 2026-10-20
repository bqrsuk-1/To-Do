from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class USER_TO_DO_INFO(db.Model):
    user_name = db.Column(db.String(100), nullable=True)
    user_password = db.Column(db.Integer, primary_key=True)
    user_planned_task = db.Column(db.String(100), nullable=True)
    user_in_progress_task = db.Column(db.String(100), nullable=True)
    user_finished_task = db.Column(db.String(100), nullable=True)
    

def __repr__(self):
    return f"USER_TO_DO_INFO('{self.user_name}', '{self.user_password}', '{self.user_planned_task}', '{self.user_in_progress_task}', '{self.user_finished_task}')"
    
    
@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
else:
    print("App is running in production mode.")