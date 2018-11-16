from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from ..db import db


shop_product = db.Table(
    'shop_product',
    Column('shop_id', Integer, ForeignKey('shop.id')),
    Column('product_id', Integer, ForeignKey('product.id'))
)
