import sqlite3
import json
from models import Employee, Location

EMPLOYEES = [
    {
        "id": 1,
        "name": "Jeremy Bakker",
        "locationId": 1
    },
    {
        "id": 2,
        "name": "Cassius Clay",
        "locationId": 1
    },
    {
        "id": 3,
        "name": "Travis Barker",
        "locationId": 3
    },
    {
        "id": 4,
        "name": "Sean Combs",
        "locationId": 2
    },
    {
        "name": "Ron Swanson",
        "locationId": 1,
        "id": 5
    },
    {
        "name": "Homer Simpson",
        "locationId": 3,
        "id": 6
    },
    {
        "name": "Clark Kent",
        "locationId": 4,
        "id": 7
    }
]


def get_all_employees():
    """this is getting all employees"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:  # connection to the db file

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()  # allows to execute quieries

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id,
            l.name location_name,
            l.address location_address
        FROM Employee e
        JOIN Location l
            ON l.id = e.location_id
        """)

        # Initialize an empty list to hold all employee representations
        employees = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()  # returns a list

        # Iterate list of data returned from database. iterating though the dataset dictionaries
        for row in dataset:

            # Create an employee instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # employee class above.
            employee = Employee(row['id'], row['name'], row['location_id'])

            location = Location(row['location_id'], row['location_name'], row['location_address'])

            employee.location = location.__dict__

            # turns employee object into a dictionary
            employees.append(employee.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(employees)


def get_single_employee(id):
    """this is getting a single employee"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM Employee e
        WHERE e.id = ?
        """, ( id, ))  # replaces the question mark with an id  uses a sequal query
        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an employee instance from the current row
        employee = Employee(data['id'], data['name'], data['location_id'])

        return json.dumps(employee.__dict__)


def create_employee(employee):
    """this is creating a new employee"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)

    return employee


def update_employee(id, new_employee):
    """this is editing an employee"""
    # Iterate the employeeS list, but use enumerate() so that
    # you can access the index value of each item.
    with sqlite3.connect("./kennel.db") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE employee
            SET
                name = ?,
                location_id = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['location_id'], id, ))


        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True


def get_employees_by_location_id(location_id):
    """this is getting an employee by their location_id"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.location_id
        FROM Employee e
        WHERE e.location_id = ?
        """, ( location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)

        return json.dumps(employees)

def delete_employee(id):
    """this is removing an employee"""
    # Initial -1 value for employee index, in case one isn't found
    employee_index = -1

    # Iterate the employeeS list, but use enumerate() so that you
    # can access the index value of each item
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Store the current index.
            employee_index = index

    # If the employee was found, use pop(int) to remove it from list
    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)
