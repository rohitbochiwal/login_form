from flask import Flask, render_template, request, redirect, session, url_for

app = Flask(__name__)
app.secret_key = 'secret_key'  


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        
        user_type = request.form['user_type']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        
        
        
        session['user'] = {
            'user_type': user_type,
            'first_name': first_name,
            'last_name': last_name,
            'username': username,
            'email': email,
            
        }
        
        
        return redirect(url_for('dashboard'))

    return render_template('signup.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        
        username = request.form['username']
        password = request.form['password']
       
        
        
        return redirect(url_for('dashboard'))

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    
    user = session.get('user')
    if not user:
        return redirect(url_for('index'))  
    
    
    if user['user_type'] == 'patient':
        return render_template('patient_dashboard.html', user=user)
    elif user['user_type'] == 'doctor':
        return render_template('doctor_dashboard.html', user=user)

    return redirect(url_for('index')) 

@app.route('/logout')
def logout():
    
    session.pop('user', None)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
