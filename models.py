from sqlalchemy import Column, Integer, String, Float
from database import Base

class Company(Base):
    __tablename__ = 'companies'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), unique=False)
    symbol = Column(String(10), unique=True)
    price = Column(Float, unique=False)
    dps = Column(Float, unique=False)
    eps = Column(Float, unique=False)
    dpr = Column(Float, unique=False)

    def __init__(self, name=None, symbol=None, price=None, dps=None, eps=None, dpr=None):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.dps = dps
        self.eps = eps
        self.dpr = dpr

    def __repr__(self):
        return '<Company %r>' % (self.symbol)
        # jsonify(json_list = qryresult.all())