from models.items.order import Order
from .base_model import BaseModel


class OrderModel(BaseModel):
    _items = []
    url = 'api/orders/'
    item_class = Order
