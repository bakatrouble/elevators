from models.base_model import BaseModel
from models.items.contract import Contract


class ContractModel(BaseModel):
    _items = []
    url = 'api/contracts/'
    item_class = Contract
