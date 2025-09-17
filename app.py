from flask import Flask, render_template, request

# Initialize the Flask application
app = Flask(__name__)

# --- Page Routes ---

@app.route('/')
def home():
    """Renders the homepage."""
    return render_template('index.html')

@app.route('/submit')
def submit_page():
    """Renders the submission page."""
    return render_template('submit.html')

# --- Form Handling ---

@app.route('/submit', methods=['POST'])
def handle_submission():
    """Handles the form submission from submit.html."""
    author = request.form['author_name']
    title = request.form['poem_title']
    body = request.form['poem_body']

    # --- TODO: ---
    # 1. Connect to your SQLite database here.
    # 2. Save the author, title, and body to the 'poems' table.
    # 3. Redirect the user to a 'Thank You' page.

    print(f"Received poem '{title}' by {author}") # You'll see this in your Render logs

    return "Thank you for your submission!"


if __name__ == '__main__':
    app.run(debug=True)
