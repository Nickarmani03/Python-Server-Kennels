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
    return CUSTOMERS

def get_single_customer(id):
    """this is getting a single"""
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer

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
