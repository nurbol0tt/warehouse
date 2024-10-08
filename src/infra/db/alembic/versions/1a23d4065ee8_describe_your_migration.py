"""Describe your migration

Revision ID: 1a23d4065ee8
Revises: 706b3fd7df7a
Create Date: 2024-09-22 18:26:38.589807

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '1a23d4065ee8'
down_revision: Union[str, None] = '706b3fd7df7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('products', sa.Column('total', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('products', 'total')
    # ### end Alembic commands ###
