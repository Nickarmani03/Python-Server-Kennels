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

# def create_customer(customer):
#     max_id = CUSTOMERS[-1]["id"]
#     new_id = max_id + 1
#     customer["id"] = new_id
#     CUSTOMERS.append(customer)

#     return customer
