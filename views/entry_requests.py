import sqlite3
import json
from models import Entry

def get_all_entries():
    # Open a connection to the database
    with sqlite3.connect("./dailyjournal.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.subject,
            e.date,
            e.time_spent,
            e.moods_id
            
        FROM entries e    
        """)

        # Initialize an empty list to hold all animal representations
        entries = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
    for row in dataset:

    # Create an animal instance from the current row
        entry = Entry(row['id'], row['subject'], row['date'], row['time_spent'],
                    row['moods_id'])

  

    # Add the dictionary representation of the animal to the list
        entries.append(entry.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(entries)


def get_single_entry(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.subject,
            e.date,
            e.time_spent,
            e.moods_id
            
        FROM entries e    
        """, ( id, ))

        # Load the single result into memory
        data = db_cursor.fetchone()

        # Create an animal instance from the current row
        entry = Entry(data['id'], data['subject'], data['date'], data['time_spent'],
                    data['moods_id'])

        return json.dumps(entry.__dict__)
    
    
def create_entry(new_entry):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO ENTRY
            ( subject, date, time_spent, moods_id )
        VALUES
            ( ?, ?, ?, ?, ?);
        """, (new_entry['subject'], new_entry['date'],
              new_entry['time_spent'], new_entry['moods_id'],
             ))

        # The `lastrowid` property on the cursor will return
        # the primary key of the last thing that got added to
        # the database.
        id = db_cursor.lastrowid

        # Add the `id` property to the animal dictionary that
        # was sent by the client so that the client sees the
        # primary key in the response.
        new_entry['id'] = id


    return json.dumps(new_entry)
