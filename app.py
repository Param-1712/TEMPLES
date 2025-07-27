from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Database initialization function
def init_db():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Example: create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Home page
@app.route('/')
def index():
    return render_template('index.html')

# Register route
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
        conn.commit()
        conn.close()
        return redirect(url_for('login'))
    return render_template('register.html')

# Login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE username = ? AND password = ?', (username, password))
        user = cursor.fetchone()
        conn.close()
        
        if user:
            return redirect(url_for('loggedin'))
        else:
            return 'Invalid credentials'
    return render_template('login.html')

# Logged in page
@app.route('/loggedin')
def loggedin():
    return render_template('loggedin.html')

# Other pages from your templates
@app.route('/k')
def k():
    return render_template('k.html')

@app.route('/kd')
def kd():
    return render_template('kd.html')

@app.route('/sc')
def sc():
    return render_template('sc.html')

@app.route('/sk')
def sk():
    return render_template('sk.html')
@app.route('/ss')
def ss():
    return render_template('ss.html')

@app.route('/ttd')
def ttd():
    return render_template('ttd.html')

# Initialize database before running
if __name__ == '__main__':
    init_db()
    app.run(debug=True)
