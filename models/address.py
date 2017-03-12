class Address:
    def __init__(self):
        self.oblast = ''
        self.raion = ''
        self.city = ''
        self.street = ''
        self.house = ''
        self.building = ''
        self.letter = ''

    def __str__(self):
        return ', '.join(part for part in [self.oblast,
                                           self.raion,
                                           self.city,
                                           self.street,
                                           'д. %s' % self.house if self.house else '',
                                           'к. %s' % self.building if self.building else '',
                                           'литера %s' % self.letter if self.letter else ''] if part) or '<не задано>'
