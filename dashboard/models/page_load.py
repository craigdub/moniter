from dashboard.models import Base
from sqlalchemy import Column
from sqlalchemy import Unicode
from sqlalchemy import Integer

class PageLoad(Base):
    __tablename__ = 'page_load'
    id = Column(Integer, primary_key=True)
    url = Column(Unicode(255), unique=True)

    def __init__(self, url):
        self.url = url
