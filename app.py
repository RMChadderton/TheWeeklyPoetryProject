import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Helper function to get a database connection
def get_db_connection():
    conn = sqlite3.connect('poetry.db')
    conn.row_factory = sqlite3.Row # This lets us access columns by name
    return conn

# --- Page Routes ---

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit')
def submit_page():
    return render_template('submit.html')

@app.route('/archive')
def archive():
    conn = get_db_connection()
    # Query to get all winning poems, ordered by most recent first
    winners = conn.execute('''
        SELECT p.poem_title, p.author_name, c.week_identifier
        FROM poems p
        JOIN contests c ON p.id = c.winning_poem_id
        WHERE c.winning_poem_id IS NOT NULL
        ORDER BY c.end_date DESC
    ''').fetchall()
    conn.close()
    # Pass the list of winners to the HTML template
    return render_template('archive.html', winners=winners)


# --- Form Handling ---

@app.route('/submit', methods=['POST'])
def handle_submission():
    author = request.form['author_name']
    title = request.form['poem_title']
    body = request.form['poem_body']

    # TODO: Save the submission to the database
    print(f"Received poem '{title}' by {author}")

    return "Thank you for your submission!"
