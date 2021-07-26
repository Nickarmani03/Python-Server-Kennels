import sqlite3
import json
from models import Location

LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "8422 Johnson Pike"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "209 Emory Drive"
    },
    {
        "id": 3,
        "name": "Lebanon Pike Kennels",
        "address": "123 Wakanda St."
    },
    {
        "id": 4,
        "name": "Murfreesboro Kennels",
        "address": "123 Fake St."
    }
]


def get_all_locations():
    """this is getting all locations"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:  # connection to the db file

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()  # allows to execute quieries

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        """)

        # Initialize an empty list to hold all location representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()  # returns a list

        # Iterate list of data returned from database. iterating though the dataset dictionaries
        for row in dataset:

            # Create an location instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # location class above.
            location = Location(row['id'], row['name'], row['address'])

            # turns location object into a dictionary
            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON. turnes it into a nicer looking dictionary
    return json.dumps(locations)


def get_single_location(id):
    """this is getting a single location"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            l.id,
            l.name,
            l.address
        FROM Location l
        WHERE l.id = ? 
        """, (id, ))  # replaces the question mark with an id  uses a sequal query
        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an location instance from the current row.
        location = Location(data['id'], data['name'], data['address'])

        return json.dumps(location.__dict__)


def create_location(location):
    """this is creating a new location"""
    max_id = LOCATIONS[-1]["id"]
    new_id = max_id + 1
    location["id"] = new_id
    LOCATIONS.append(location)

    return location


def delete_location(id):
    """this is removing an location"""
    # Initial -1 value for location index, in case one isn't found
    location_index = -1

    # Iterate the LOCATIONS list, but use enumerate() so that you
    # can access the index value of each item
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Store the current index.
            location_index = index

    # If the location was found, use pop(int) to remove it from list
    if location_index >= 0:
        LOCATIONS.pop(location_index)


def update_location(id, new_location):
    """this is editing an location"""
    # Iterate the locationS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the location. Update the value.
            LOCATIONS[index] = new_location
            break
