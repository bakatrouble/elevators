from models.items.account import Account
from .base_model import BaseModel


class AccountModel(BaseModel):
    _items = []
    url = 'api/accounts/'
    item_class = Account
