import traceback
import sys
import pickle
import os.path
from models import Models


def excepthook(etype, value, tb):
    traceback.print_exception(etype, value, tb)
    die()

sav_path = os.path.join(os.path.expanduser('~'), '.elevators.sav')


class OptionsStructure:
    def __init__(self):
        self.server_url = '127.0.0.1:8000'
        self.autonomy_available = False
        self.autonomy_mode = False

        self.username = ''
        self.token = ''

        self.cache_application_types = []
        self.cache_clients = []
        self.cache_specialists = []

        self.local_applications = []
        self.local_clients = []


class Options:
    instance = None

    @classmethod
    def dump(cls):
        cls.instance.cache_application_types = Models.get().application_types.items()
        cls.instance.cache_clients = Models.get().clients.items()
        cls.instance.cache_specialists = Models.get().specialists.items()
        cls.instance.local_applications = list(filter(lambda x: not x.id, Models.get().applications.items()))
        cls.instance.local_clients = list(filter(lambda x: not x.id, Models.get().clients.items()))

        cls.instance.autonomy_available = True
        cls.instance.autonomy_mode = False

        with open(os.path.join(os.path.expanduser('~'), '.elevators.sav'), 'wb') as f:
            pickle.dump(cls.instance, f)

    @classmethod
    def get(cls) -> OptionsStructure:
        if not cls.instance:
            if os.path.exists(sav_path):
                try:
                    with open(sav_path, 'rb') as f:
                        cls.instance = pickle.load(f)
                except (IOError, pickle.UnpicklingError):
                    cls.instance = OptionsStructure()
            else:
                cls.instance = OptionsStructure()
        return cls.instance


def die():
    Options.dump()
    sys.exit()
