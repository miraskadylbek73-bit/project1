from flask import Flask, render_template, request, redirect

app = Flask(__name__)

users = {
    "admin": {"role": "Администратор", "name": "Zhanibek Zhankulov"},
    "parent": {"role": "Родитель", "name": "Zhassulan Issov"},
    "student": {"role": "Ученик", "name": "Miras Kadylbek"}
}

@app.route('/')
def login():
    return render_template('index.html', page='login')

@app.route('/dashboard', methods=['POST'])
def dashboard():
    role = request.form.get('role')
    user_data = users.get(role)
    return render_template('index.html', page='dashboard', user=user_data)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
