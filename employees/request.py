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
      "location": "Nashville",
      "locationId": 1,
      "customerId": 3,
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
    return EMPLOYEES


    # Function with a single parameter
def get_single_employee(id):
    """this is getting a single employee"""
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the employeeS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
