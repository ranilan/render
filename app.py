from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# הגדרת חיבור לבסיס נתונים SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'  # הקובץ יישמר בתיקיה המקומית
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# יצירת מודל למשתמשים
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'<User {self.name}>'

# יצירת בסיס נתונים אם לא קיים
with app.app_context():
    db.create_all()

# Route לדף הראשי
@app.route('/')
def home():
    return render_template("index.html")

# API שיחזיר מידע על משתמש
@app.route('/api/user')
def get_user():
    user = User.query.first()  # מקבל את המשתמש הראשון
    if user:
        return jsonify({
            'name': user.name,
            'age': user.age,
            'email': user.email
        })
    return jsonify({'message': 'No user found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
