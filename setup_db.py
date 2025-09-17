import sqlite3

# Connect to (or create) the database file
connection = sqlite3.connect('poetry.db')
cursor = connection.cursor()

# --- Create the tables ---
print("Creating tables...")
cursor.execute('''
CREATE TABLE IF NOT EXISTS contests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    week_identifier TEXT NOT NULL UNIQUE,
    start_date TIMESTAMP NOT NULL,
    end_date TIMESTAMP NOT NULL,
    winning_poem_id INTEGER,
    FOREIGN KEY (winning_poem_id) REFERENCES poems (id)
);
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS poems (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    contest_id INTEGER NOT NULL,
    author_name TEXT NOT NULL,
    poem_title TEXT,
    poem_body TEXT NOT NULL,
    submission_timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ai_score REAL,
    status TEXT NOT NULL DEFAULT 'submitted',
    FOREIGN KEY (contest_id) REFERENCES contests (id)
);
''')

# --- Insert some dummy data ---
print("Inserting dummy data...")
try:
    # Insert a couple of poems
    cursor.execute("INSERT INTO poems (contest_id, author_name, poem_title, poem_body) VALUES (?, ?, ?, ?)",
                   (1, 'Eleanor Vance', 'Sundown at the Estuary', 'The water held its breath...'))
    cursor.execute("INSERT INTO poems (contest_id, author_name, poem_title, poem_body) VALUES (?, ?, ?, ?)",
                   (1, 'Samuel Reed', 'Footnotes to a Rainy Day', 'The city wept in grayscale...'))

    # Insert a contest
    cursor.execute("INSERT INTO contests (week_identifier, start_date, end_date, winning_poem_id) VALUES (?, ?, ?, ?)",
                   ('2025-W37', '2025-09-08', '2025-09-14', 1)) # Mark poem with id=1 as the winner
except sqlite3.IntegrityError:
    print("Dummy data may already exist. Skipping insertion.")


# Save the changes and close the connection
connection.commit()
connection.close()

print("Database setup complete. 'poetry.db' is ready.")
