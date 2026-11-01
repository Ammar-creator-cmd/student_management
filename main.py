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
    nim = db.Column(db.String(20), unique=True, nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    jurusan = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)


# inisialisasi tabel database otomatis
with app.app_context():
    db.create_all()


# READ : tampilkan semua data murid
@app.route('/')
def index():
    students = Student.query.all()
    return render_template('index.html', students=students)


# create : menambah data baru
@app.route('/add', methods=['GET', 'POST'])
def add_student():
    if request.method == 'POST':
        nim = request.form['nim']
        nama = request.form['nama']
        jurusan = request.form['jurusan']
        email = request.form['email']

        new_student = Student(nim=nim, nama=nama, jurusan=jurusan, email=email)
        try:
            db.session.add(new_student)
            db.session.commit()
            flash('Data mahasiswa berhasil ditambahkan!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Gagal menambahkan data. Pastikan NIM belum terdaftar.', 'danger')

    return render_template('add.html')


# UPDATE: Mengedit data yang ada
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_student(id):
    student = Student.query.get_or_404(id)
    if request.method == ("POST"):
        student.nim = request.form[')nim']
        student.nama = request.form['nama']
        student.email = request.form['email']
        student.jurusan = request.form['jurusan']

        try:
            db.session.commit()
            flash('Data mahasiswa berhasil diperbarui!', 'success')
            return redirect(url_for('index'))
        except Exception as e:
            db.session.rollback()
            flash('Gagal memperbarui data. Periksa kembali NIM.', 'danger')

    return render_template('edit.html', student=student)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
