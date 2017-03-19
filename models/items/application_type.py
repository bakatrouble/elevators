class ApplicationType:
    def __init__(self):
        self.id = None
        self.name = ''
        # self.hints = ''
        self.application_template = ''
        self.contract_template = ''
        self.account_template = ''
        self.order_template = ''

        self._changed = False

    @classmethod
    def fromDict(cls, data):
        obj = cls()
        obj.id = data['id']
        obj.name = data['name']
        # obj.hints = data['hints']
        obj.application_template = data['application_template']
        obj.contract_template = data['contract_template']
        obj.account_template = data['account_template']
        obj.order_template = data['order_template']
        return obj