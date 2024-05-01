from flask import Flask, jsonify, request
import studySchedule  # Import your existing studySchedule module if it's separate

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Study Schedule App!"

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    login_system = studySchedule.LoginSchedule()
    message, status = login_system.user_login(data['email'], data['password'])
    return jsonify({'message': message, 'status': status})

# Add other routes as necessary

if __name__ == '__main__':
    app.run(debug=True)
