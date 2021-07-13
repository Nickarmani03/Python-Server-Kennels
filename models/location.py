class Location():
    """The design. For the location dictionaries that are currently hard-coded in your locationS list"""
    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
def __init__(self, id, name, address):
    self.id = id
    self.name = name
    self.address = address

new_location = Location(1, "Murfreesboro Kennels", "123 Fake St.", 1)
