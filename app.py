from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail, Message
import random
import string

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['MAIL_SERVER'] = 'smtp.example.com'  # Настройте ваш почтовый сервер
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'your-email@example.com'
app.config['MAIL_PASSWORD'] = 'your-email-password'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

db = SQLAlchemy(app)
mail = Mail(app)

# Модель пользователя
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    is_active = db.Column(db.Boolean, default=False)
    confirmation_code = db.Column(db.String(6), unique=True, nullable=True)

    def __repr__(self):
        return f'<User {self.email}>'

# Инициализация базы данных
with app.app_context():
    db.create_all()

# Генерация случайного кода
def generate_confirmation_code():
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

# Регистрация
@app.route('/api/v1/users/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'User already exists'}), 400

    confirmation_code = generate_confirmation_code()
    new_user = User(email=email, password=password, confirmation_code=confirmation_code)
    db.session.add(new_user)
    db.session.commit()

    # Отправка письма с кодом подтверждения
    msg = Message('Confirm your email', sender='your-email@example.com', recipients=[email])
    msg.body = f'Your confirmation code is {confirmation_code}'
    mail.send(msg)

    return jsonify({'message': 'User registered, please check your email to confirm your account'}), 201

# Подтверждение пользователя
@app.route('/api/v1/users/confirm/', methods=['POST'])
def confirm_user():
    data = request.get_json()
    email = data.get('email')
    confirmation_code = data.get('confirmation_code')

    user = User.query.filter_by(email=email, confirmation_code=confirmation_code).first()
    if not user:
        return jsonify({'message': 'Invalid confirmation code or email'}), 400

    user.is_active = True
    user.confirmation_code = None
    db.session.commit()

    return jsonify({'message': 'User confirmed successfully'}), 200

# Авторизация
@app.route('/api/v1/users/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email, password=password).first()
    if user and user.is_active:
        return jsonify({'message': 'Login successful'}), 200
    elif user and not user.is_active:
        return jsonify({'message': 'Account not confirmed'}), 403
    else:
        return jsonify({'message': 'Invalid email or password'}), 401

if __name__ == '__main__':
    app.run(debug=True)
