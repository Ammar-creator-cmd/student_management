from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "kunci-rahasia-flask-crud"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# model db
class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nim = db.Column(db.String(20),unique = True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    jurusan = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)

#inisialisasi tabel database otomatis
with app.app_context():
    db.create_all()

#READ : tampilkan semua data murid
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
