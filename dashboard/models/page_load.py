from dashboard.models import Base
from sqlalchemy import Column
from sqlalchemy import Unicode
from sqlalchemy import Integer

class PageLoad(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(255), unique=True)

    def __init__(self, name):
        self.name = name
