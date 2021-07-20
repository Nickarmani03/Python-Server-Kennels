import sqlite3
import json
from models import Customer

CUSTOMERS = [
    {
        "id": 1,
        "name": "Clark Kent",
        "address": "7200 Nowland Ave",
        "email": "clark@gmail.com"
    },
    {
        "id": 2,
        "name": "Chuck Norris",
        "address": "5700 Benford Blvd",
        "email": "chuck@gmail.com"
    },
    {
        "id": 3,
        "name": "Bruce Lee",
        "address": "4102 Baker St",
        "email": "bruce@gmail.com"
    }
]


def get_all_customers():
    """this is getting all customers"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.db") as conn:  # connection to the db file

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()  # allows to execute quieries

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email
        FROM customer c
        """)

        # Initialize an empty list to hold all customer representations
        customers = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()  # returns a list

        # Iterate list of data returned from database. iterating though the dataset dictionaries
        for row in dataset:

            # Create an customer instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # customer class above.
            customer = Customer(row['id'], row['name'],
                                row['address'], row['email'])

            # turns customer object into a dictionary
            customers.append(customer.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(customers)


def get_single_customer(id):
    """this is getting a single customer"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            c.id,
            c.name,
            c.address,
            c.email
        FROM Customer c
        WHERE c.id = ? 
        """, (id, ))  # replaces the question mark with an id  uses a sequal query
        # Load the single result into memory
        data = db_cursor.fetchone()  # returns one row

        # Create an customer instance from the current row
        customer = Customer(data['id'], data['name'],
                            data['address'], data['email'])

        return json.dumps(customer.__dict__)


def create_customer(customer):
    """this is creating a new customer"""
    max_id = CUSTOMERS[-1]["id"]
    new_id = max_id + 1
    customer["id"] = new_id
    CUSTOMERS.append(customer)

    return customer


def delete_customer(id):
    """this is removing an customer"""
    # Initial -1 value for customer index, in case one isn't found
    customer_index = -1

    # Iterate the customerS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Store the current index.
            customer_index = index

    # If the customer was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)


def update_customer(id, new_customer):
    """this is editing a customer"""
    # Iterate the customerS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the customer. Update the value.
            CUSTOMERS[index] = new_customer
            break

def get_customers_by_email(email):
    """this is getting a customer by their email"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, (email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_customer_by_name(name):
    """this is getting a customer by their name"""
    with sqlite3.connect("./kennel.db") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.name = ?
        """, (name, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(
                row['id'], row['name'], row['address'], row['email'], row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
