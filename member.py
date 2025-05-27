class Member:
    def __init__(self, first_name, last_name, address, other_details):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.other_details = other_details

    def toDBCollection(self):
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'address': self.address,
            'other_details': self.other_details
        }
