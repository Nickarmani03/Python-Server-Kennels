class Customer():
    """The design. For the customer dictionaries that are currently hard-coded in your customerS list"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
def __init__(self, id, name, address, email):
    self.id = id
    self.name = name
    self.address = address
    self.email = email
    

new_customer = Customer(1, "Clark Kent", "7200 Nowland Ave", "clark@gmail.com")
