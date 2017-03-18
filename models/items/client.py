class Client:
    def __init__(self):
        self.id = None
        self.full_name = ''
        self.short_name = ''
        self.registration_address = ''
        self.location_address = ''
        self.phone = ''
        self.inn = ''
        self.kpp = ''
        self.account_number = ''
        self.bank = ''
        self.bik = ''
        self.ogrn = ''
        self.person_name = ''
        self.person_post = ''

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.full_name = data['full_name']
        obj.short_name = data['short_name']
        obj.registration_address = data['registration_address']
        obj.location_address = data['location_address']
        obj.phone = data['phone']
        obj.inn = data['inn']
        obj.kpp = data['kpp']
        obj.account_number = data['account_number']
        obj.bank = data['bank']
        obj.bik = data['bik']
        obj.ogrn = data['ogrn']
        obj.person_name = data['person_name']
        obj.person_post = data['person_post']
        return obj

    def toDict(self):
        return {
            'id': self.id,
            'full_name': self.full_name,
            'short_name': self.short_name,
            'registration_address': self.registration_address,
            'location_address': self.location_address,
            'phone': self.phone,
            'inn': self.inn,
            'kpp': self.kpp,
            'account_number': self.account_number,
            'bank': self.bank,
            'bik': self.bik,
            'ogrn': self.ogrn,
            'person_name': self.person_name,
            'person_post': self.person_post,
        }