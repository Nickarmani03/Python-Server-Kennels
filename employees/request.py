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
    """this is getting all EMPLOYEES"""
    return EMPLOYEES

    # Function with a single parameter


def get_single_employee(id):
    """this is getting a single employee"""
    # Variable to hold the found employee, if it exists
    requested_employee = None

    # Iterate the EMPLOYEES list above. Very similar to the
    # for..of loops you used in JavaScript.
    for employee in EMPLOYEES:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee


def create_employee(employee):
    """this is creating a new employee"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)

    return employee

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

def update_employee(id, new_employee):
    """this is editing an employee"""
    # Iterate the employeeS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            # Found the employee. Update the value.
            EMPLOYEES[index] = new_employee
            break
