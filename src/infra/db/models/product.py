import sqlalchemy as sa

from src.infra.db.models.common import Base


class Product(Base):
    __tablename__ = 'products'

    title = sa.Column(sa.String(128))
    description =  sa.Column(sa.String)
    price = sa.Numeric(precision=10, scale=2)
    total = sa.Column(sa.Integer)
