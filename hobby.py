class Hobby:
    def __init__(self, hobby_code, hobby_description):
        self.hobby_code = hobby_code
        self.hobby_description = hobby_description

    def toDBCollection(self):
        return {
            'hobby_code': self.hobby_code,
            'hobby_description': self.hobby_description
        }
