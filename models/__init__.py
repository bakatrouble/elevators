class Models:
    instance = None

    def __init__(self):
        from .application import ApplicationModel
        from .application_type import ApplicationTypeModel
        from .client import ClientModel
        from .specialist import SpecialistModel

        self.applications = ApplicationModel()
        self.application_types = ApplicationTypeModel()
        self.clients = ClientModel()
        self.specialists = SpecialistModel()

    @classmethod
    def get(cls) -> 'Models':
        if not cls.instance:
            cls.instance = cls()
        return cls.instance
