from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Route לדף הראשי
@app.route('/')
def home():
    return render_template("index.html")

# API שיחזיר נתונים על משתמש
@app.route('/api/user')
def get_user():
    user = {
        'name': 'John Doe',
        'age': 30,
        'email': 'john.doe@example.com'
    }
    return jsonify(user)

if __name__ == '__main__':
    app.run(debug=True)
