class Membership:
    def __init__(self, member_id, hobby_code, percentage, level_of_ability):
        self.member_id = member_id
        self.hobby_code = hobby_code
        self.percentage = percentage
        self.level_of_ability = level_of_ability

    def toDBCollection(self):
        return {
            'member_id': self.member_id,
            'hobby_code': self.hobby_code,
            'percentage': self.percentage,
            'level_of_ability': self.level_of_ability
        }
