class Specialist:
    def __init__(self):
        self.id = None
        self.last_name = ''
        self.first_name = ''
        self.patr_name = ''

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.last_name = data['last_name']
        obj.first_name = data['first_name']
        obj.patr_name = data['patr_name']
        return obj

    def fullName(self):
        return '%s %s. %s.' % (self.last_name.capitalize(), self.first_name[0].upper(), self.patr_name[0].upper())