from sqlalchemy import Column, String, Integer

from example.core.entity.exchange import Exchange
from example.configuration.database import DatabaseBase


class ExchangeModel(DatabaseBase):
    __tablename__ = "exchange"

    id = Column("id", Integer, primary_key=True)
    code = Column("code", String)
    name = Column("name", String)
    post_code = Column("post_code", String)

    def to_entity(self):
        return Exchange(code=self.code, name=self.name, post_code=self.post_code,)
