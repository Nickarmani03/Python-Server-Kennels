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
      "name": "Murfreesboro Kennels",
      "address": "123 Fake St.",
      "id": 4
    }
  ]

def get_all_locations():
    return LOCATIONS

    # Function with a single parameter
def get_single_location(id):
    # Variable to hold the found location, if it exists
    requested_location = None

    # Iterate the locationS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for location in LOCATIONS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if location["id"] == id:
            requested_location = location

    return requested_location